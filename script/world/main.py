import heapq
import os
import time
from collections import defaultdict
from math import atan
from typing import Tuple, Union, List

import numpy as np
from numpy import ndarray

import config
import game
import log
from script.utils.cv_utils import remove_same_position
from script.utils.interface import WorldUtils
from script.utils import (fight, Role, wait_img, template_path, cv_utils)
from script.world.data import Map


def a_star(graph, start, goal) -> Union[list, None]:
    """启发式算法 A*"""
    log.info("a-star")
    frontier = list()
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
            log.info("a-star end")
            return road

        for nex in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(nex)
            if nex not in cost_so_far or new_cost < cost_so_far[nex]:
                priority = new_cost + heuristic(goal, nex)
                heapq.heappush(frontier, (priority, nex))
                cost_so_far[nex] = new_cost
                came_from[nex] = current

    log.error(f"未找到路线, start={start}, goal={goal}")
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


def heuristic(a, b):
    """计算两点直线距离"""
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def sort_mst_targets(start, targets):
    """对怪点进行由近到远排序"""
    pos_cost = dict()
    log.info(f"对目标点进行排序, start = {start},  targets = {targets}")
    for pos in targets:
        cost = heuristic(start, pos)
        pos_cost[pos] = cost

    res = sorted(targets, key=lambda x: pos_cost[x])
    return res


def init_road(road, err_val=8):
    """
    获取路线转折点，例如当前是行走90度的路，前方是120度的路则记录，不断的将这些点记录下来用于寻路。
    err_val是误差角度，比如err_val=10，行走90度的路，前方是100度的路则认为他们是同一路线
    """
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


def wait_fight_end():
    """若当前处于战斗则阻塞当前线程至战斗结束"""
    flag = True
    while fight.is_fighting():
        if flag:
            log.debug("等待战斗结束")
            flag = False
        time.sleep(1)
        continue


class Graph:
    def __init__(self, image: ndarray):
        self.img = image

    def cost(self, point: tuple):
        """
        在point为中心范围15不得有边界墙，否则增加代价
        """
        radius = 15
        x, y = point
        top_left = (x - radius, y - radius)
        bottom_right = (x + radius, y + radius)
        img_selection = self.img[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]]
        if np.any(img_selection == [255, 255, 255]):
            return 15
        return 1

    def is_road(self, pos: tuple) -> bool:
        white = np.array([255, 255, 255])
        return (self.img[pos[1], pos[0]] != white).all()

    def neighbors(self, point: tuple):
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


class World:
    def __init__(self):
        self.util = WorldUtils()
        self.map = Map(os.path.join(config.abspath, "script/world", "map"))

        self._stop = False

    def run(self, start=None, white=None, debug=False) -> None:
        """
        start这个参数后面用来自定义起点地图
        """
        game.set_foreground()
        self._stop = False
        # 下一个地图不为空且没有设置_stop为True
        while not self.map.data.empty() and not self._stop:
            Role.stop_move()
            self._next_map()
            cur_pos = self.util.locate_role_pos(self.map.line)
            if cur_pos == (-1, -1):
                log.error("无法定位出生地坐标，进入下一张图")
                continue
            mst_targets = self._get_targets()
            log.info(f"去重后怪点数量: {mst_targets}")
            # 对怪物坐标排序 近->远
            mst_targets = sort_mst_targets(cur_pos, mst_targets)
            fight.start()
            target_idx = 0
            while target_idx < len(mst_targets) and self.map.reload_cnt < 2:
                wait_fight_end()
                mst_target = mst_targets[target_idx]
                road, p_err, a_err = self._get_road(mst_target)
                # 处理特殊情况（无法获取到路线）
                if road is None:
                    # 获取坐标错误那么直接重载地图并且跳过当前怪点
                    if p_err:
                        target_idx += 1
                        self.map.reload_current_map()
                        continue
                    # 规划路线错误则尝试规划直接规划下一个怪点，若依旧规划错误则重载地图
                    elif a_err:
                        target_idx += 1
                        mst_target = mst_targets[target_idx]
                        road, _, _ = self._get_road(mst_target)
                        if road is None:
                            self.map.reload_current_map()
                            continue
                    else:
                        log.debug("不应该出现这种情况，重载地图")
                        self.map.reload_current_map()
                        continue
                road = init_road(road)
                road = remove_same_position(road, 10)
                # 移动前先调整一下视角
                cur_pos = self.util.locate_role_pos(self.map.line)
                if cur_pos == (-1, -1):
                    target_idx += 1  # 跳过这个可能到达不了的怪点
                    self.map.reload_current_map()
                    continue

                target_angle = calculate_angle(cur_pos, road[0])
                Role.set_angle(self.util.get_angle(), target_angle)
                Role.move()
                road_idx = 0
                obs_positions = dict()
                while road_idx < len(road):
                    if fight.is_fighting():
                        Role.stop_move()
                        wait_fight_end()
                        Role.move()
                    road_pos = road[road_idx]
                    cur_pos = self.util.locate_role_pos(self.map.line, self.map.default)
                    if cur_pos == (-1, -1):
                        Role.stop_move()
                        target_idx += 1
                        self.map.reload_current_map()
                        break
                    cur_angle = self.util.get_angle()
                    is_same = cv_utils.is_same_position(cur_pos, road_pos, 10)
                    # 移动到既定位置了，尝试移动到下一个既定位置
                    if is_same:
                        road_idx += 1
                        continue
                    else:
                        if cur_pos == self.util.last_pos:
                            log.debug("可能遇到障碍物了！")
                            Role.stop_move()
                            if cur_pos not in obs_positions:
                                obs_positions[cur_pos] = 1
                            else:
                                obs_positions[cur_pos] += 1
                            if obs_positions[cur_pos] == 3:
                                log.debug("尝试重新规划路线")
                                road, _, _ = self._get_road(mst_target)
                                if road is None:
                                    log.debug("规划失败，重载地图")
                                    Role.stop_move()
                                    self.map.reload_current_map()
                                    break
                                road = remove_same_position(init_road(road), 10)
                            elif obs_positions[cur_pos] == 5:
                                log.debug("多次在该地方遇到障碍物，重载地图")
                                Role.stop_move()
                                self.map.reload_current_map()
                                break
                            Role.obstacles()
                            Role.move()
                            continue
                        target_angle = calculate_angle(cur_pos, road_pos)
                        Role.set_angle(cur_angle, target_angle)
                if road_idx == len(road):
                    target_idx += 1
                Role.stop_move()
            fight.stop()
        fight.close()

    def stop(self) -> None:
        self._stop = True

    def _get_targets(self) -> list:
        red = np.array([46, 46, 214])

        # 查找所有怪点
        lis = np.where(np.all(self.map.target == red, axis=-1))
        targets = list(zip(*lis[::-1]))
        targets = remove_same_position(targets, 20)  # 去重
        return targets

    def _get_road(self, target) -> Tuple[Union[List, None], bool, bool]:
        """
        pos_err和a_star_err表示是否发生了坐标错误和A*寻路错误，便于对每种情况做出特殊处理
        """
        road = None
        graph = Graph(self.map.binary)
        err_cnt = 0
        pos_err = False
        a_star_err = False
        while err_cnt <= 4:
            wait_fight_end()
            cur_pos = self.util.locate_role_pos(self.map.line)
            if cur_pos == (-1, -1):
                err_cnt += 1
                pos_err = True
                log.error(f"无法定位坐标，1s后重新定位")
                time.sleep(1)
                continue
            pos_err = False
            road = a_star(graph, cur_pos, target)
            if road is not None:
                pos_err = False
                a_star_err = False
                break
            else:
                err_cnt += 1
                a_star_err = True
                log.error("获取路径出错，3S后重试")
                time.sleep(3)
        return road, pos_err, a_star_err

    def _next_map(self) -> bool:
        res = self.map.next()
        wait_img(template_path.PHONE, mode='gray')
        return res


if __name__ == '__main__':
    world = World()
    world.run()
