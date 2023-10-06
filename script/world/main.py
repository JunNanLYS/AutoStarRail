import heapq
import os
import time
from collections import Counter
from functools import lru_cache
from math import atan
from typing import Tuple

import cv2
import numpy as np
import pyautogui

import config
import game
import log
from script.utils.cv_utils import remove_same_position
from script.utils.interface import WorldUtils
from script.utils import (fight, Role, wait_img, template_path, cv_utils)
from script.world.data import Map


class Graph:
    def __init__(self, image):
        self.img = image

    def cost(self, point):
        """
        在point为中心范围10不得有边界墙
        """
        radius = 10
        x, y = point
        top_left = (x - radius, y - radius)
        bottom_right = (x + radius, y + radius)
        img_selection = self.img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        if np.any(img_selection == [255, 255, 255]):
            return 10
        return 1

    def is_road(self, pos) -> bool:
        white = np.array([255, 255, 255])
        return (self.img[pos[1], pos[0]] != white).all()

    def neighbors(self, point):
        x, y = point
        res = []
        directions = [(x + 1, y),
                      (x - 1, y),
                      (x, y + 1),
                      (x, y - 1),
                      (x + 1, y + 1),
                      (x + 1, y - 1),
                      (x - 1, y + 1),
                      (x - 1, y - 1)]
        for direction in directions:
            # x 越界
            if direction[0] < 0 or direction[0] >= self.img.shape[1]:
                continue
            # y 越界
            elif direction[1] < 0 or direction[1] >= self.img.shape[0]:
                continue
            if self.is_road(direction):
                res.append(direction)
        return res


@lru_cache(50)
def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


@lru_cache(50)
def a_star(graph, start, goal):
    """启发式算法 A*"""
    log.debug("a-start")
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = dict()
    cost_so_far = dict()
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            pre = came_from[goal]
            road = [goal]
            # 获取最短路径
            while pre is not None:
                road.append(pre)
                pre = came_from[pre]
            road.reverse()
            log.debug("a-star end")
            return road, cost_so_far

        for nex in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(nex)
            if nex not in cost_so_far or new_cost < cost_so_far[nex]:
                priority = new_cost + heuristic(goal, nex)
                heapq.heappush(frontier, (priority, nex))
                cost_so_far[nex] = new_cost
                came_from[nex] = current

    log.debug(f"未找到路线, start={start}, goal={goal}")
    return None


def calculate_angle(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    """
    计算坐标点与在角色哪个方向, 0度为正y轴，90度为负x轴
    :param pos1: 角色坐标
    :param pos2: 目的地坐标
    :return:
    """
    x, y = pos2[0] - pos1[0], -(pos2[1] - pos1[1])
    if y == 0:
        # 正x轴
        if x > 0:
            return 270
        # 原点
        elif x == 0:
            return 0
        # 负x轴
        else:
            return 90
    elif x == 0:
        if y > 0 or y == 0:
            return 0
        else:
            return 180
    angle = int(abs(atan(y / x)) * (180 / 3.1415926535))
    if x > 0:
        # 第一象限
        if y > 0:
            angle += 270
        # 第四象限
        else:
            angle = 180 + (90 - angle)
    # x < 0
    else:
        # 第二象限
        if y > 0:
            angle = 90 - angle
        # 第三象限
        else:
            angle += 90
    return angle


def init_road(road, err_val=10):
    res = []
    start = road[0]
    end = road[1]
    i = 1
    pre_angle = calculate_angle(start, end)
    flag = False

    while i < len(road) - 1:
        cur_angle = calculate_angle(start, road[i])
        if pre_angle - err_val <= cur_angle <= pre_angle + err_val:
            flag = True
        else:
            flag = False
            res.append(end)
            start = end
            pre_angle = cur_angle

        end = road[i]
        i += 1

    if flag:
        res.append(end)
    return res


def sort_target_pos(graph, start, targets):
    """对怪点进行由近到远排序"""
    pos_cost = dict()
    log.info(f"对目标点进行排序, start = {start},  targets = {targets}")
    print(start, targets)
    for pos in targets:
        _, cost = a_star(graph, start, pos)
        pos_cost[pos] = cost[pos]

    res = sorted(targets, key=lambda x: pos_cost[x])
    return res


def wait_fight_end(cnt=1):
    while fight.is_fighting():
        if cnt:
            log.info("等待战斗结束")
            cnt = 0
        time.sleep(1)
        continue


class World:
    def __init__(self):
        self.utils = WorldUtils()
        self.map = Map(os.path.join(config.abspath, "script/world", "map"))

        self._stop = False

    def run(self, debug=False):
        game.set_foreground()
        self._stop = False
        # 锄大地
        while self.map.data and not self._stop:
            self.next_map()
            graph = Graph(self.map.binary)
            targets = self.get_targets()
            log.info(f"去重后怪点数量: {targets}")

            # 对怪物由近到远排序
            targets = sort_target_pos(graph, self.utils.locate_role_pos(self.map.line), targets)
            fight.start()  # 战斗模块开启
            target_idx = 0
            while target_idx < len(targets) and self.map.reload_cnt <= 2:
                wait_fight_end()
                target_pos = targets[target_idx]
                road = None
                # 战斗时以及获取当前角色坐标时有时会出错，导致程序抛出TypeError这个错误
                while road is None:
                    try:
                        road, _ = a_star(graph, self.utils.locate_role_pos(self.map.line), target_pos)
                    except TypeError:
                        log.error("获取路径出错，2S后重试，若正在战斗则等待战斗结束")
                        time.sleep(2)
                        wait_fight_end()
                        road, _ = a_star(graph, self.utils.locate_role_pos(self.map.line), target_pos)
                road = remove_same_position(init_road(road, err_val=8), 5)  # 初始化路径并去除重复节点

                # 移动前先调整一下视角
                target_angle = calculate_angle(self.utils.locate_role_pos(self.map.line), road[0])
                Role.set_angle(self.utils.get_angle(), target_angle)
                Role.move()
                time.sleep(2)
                road_idx = 0
                obs_positions = Counter()
                # 遍历路径节点
                while road_idx < len(road):
                    if fight.is_fighting():
                        # 停止移动直到结束战斗
                        Role.stop_move()
                        wait_fight_end()
                        Role.move()
                    road_pos = road[road_idx]
                    cur_pos = self.utils.locate_role_pos(self.map.line,
                                                         self.map.default,
                                                         is_fighting=fight.is_fighting)
                    cur_angle = self.utils.get_angle()
                    is_same = cv_utils.is_same_position(cur_pos, road_pos, 15)
                    if is_same:
                        road_idx += 1
                        continue
                    else:
                        # 可能遇到障碍物了
                        if cur_pos == self.utils.last_pos:
                            log.debug("可能遇到障碍物了")
                            Role.stop_move()
                            obs_positions[cur_pos] += 1
                            if obs_positions[cur_pos] == 3:
                                road, _ = a_star(graph, cur_pos, target_pos)
                                road = remove_same_position(init_road(road, err_val=8), 5)  # 初始化路径并去除重复节点
                                road_idx = 0
                            elif obs_positions[cur_pos] >= 5:
                                log.info("多次在该地方遇到障碍物，重载地图")
                                self.map.reload_current_map()
                                break
                            Role.obstacles()
                            Role.move()
                        target_angle = calculate_angle(cur_pos, road_pos)
                        Role.set_angle(cur_angle, target_angle)
                if road_idx == len(road):
                    target_idx += 1
                Role.stop_move()
            fight.stop()
        fight.close()

    def get_targets(self):
        red = np.array([46, 46, 214])

        # 查找所有怪点
        lis = np.where(np.all(self.map.target == red, axis=-1))
        targets = list(zip(*lis[::-1]))
        targets = remove_same_position(targets, 20)  # 去重
        return targets

    def next_map(self):
        self.map.next()
        wait_img(template_path.PHONE, mode='gray')

    def stop(self):
        self._stop = True

    def show_road(self, road):
        img = self.map.default.copy()
        for pos in road:
            img[pos[1], pos[0]] = [0, 255, 0]

        cv2.imshow('road', img)
        cv2.moveWindow('road', 0, 0)
        cv2.waitKey(1000)


if __name__ == '__main__':
    world = World()
    world.run()
