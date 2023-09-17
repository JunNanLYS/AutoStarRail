import heapq
import os

import config
import game
import log
from script.utils.interface import WorldUtils
from script.world.data import BALL_NAME, AREA_NAME


class World:
    utils = WorldUtils()
    ball_id = 1
    area_id = 1

    @classmethod
    def auto(cls, path: str):
        cls.utils.set_map_path(path)
        cls.utils.load_maps()  # 加载地图
        ball_name = BALL_NAME[cls.ball_id]
        area_name = AREA_NAME[cls.ball_id][cls.area_id - 1]
        log.info(f"星球名称: {ball_name}, 区域名称: {area_name}")
        cls.utils.into_ball(ball_name)
        cls.utils.into_area(area_name)
        cls.utils.into_point(cls.utils.point_img)

        # 开始寻路

    @classmethod
    def run(cls):
        game.set_foreground()
        path = os.path.join(config.abspath, 'script', 'world', 'map')
        files_and_folders = os.listdir(path)
        world_ids = [file for file in files_and_folders if os.path.isdir(os.path.join(path, file))]
        for world_id in world_ids:
            cls.ball_id = int(world_id)
            word_path = os.path.join(path, world_id)
            files_and_folders = os.listdir(word_path)
            area_ids = [file for file in files_and_folders if os.path.isdir(os.path.join(word_path, file))]
            for area_id in area_ids:
                cls.area_id = int(area_id)
                area_path = os.path.join(word_path, area_id)
                files_and_folders = os.listdir(area_path)
                point_ids = [file for file in files_and_folders if os.path.isdir(os.path.join(area_path, file))]
                for point_id in point_ids:
                    point_path = os.path.join(area_path, point_id)
                    default = os.path.join(point_path, 'default.png')
                    binary = os.path.join(point_path, 'binary.png')
                    target = os.path.join(point_path, 'target.png')
                    point = os.path.join(point_path, 'point.png')
                    check = os.path.exists
                    # 运行锄大地需要 原图 二值化图 怪点图 传送点图
                    if check(default) and check(binary) and check(target) and check(point):
                        cls.auto(point_path)


class Graph:
    def __init__(self, image):
        self.img = image

    def neighbors(self, point):
        x, y = point
        return [
            (x + 1, y),
            (x - 1, y),
            (x, y + 1),
            (x, y - 1),
            (x + 1, y + 1),
            (x + 1, y - 1),
            (x - 1, y + 1),
            (x - 1, y - 1)
        ]


def heuristic(a, b):
    return abs(b[0] - a[0]) + abs(b[1] - a[1])


def a_star(graph, start, goal):
    """启发式算法 A*"""
    frontier = []
    heapq.heappush(frontier, (0, start))
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0

    while frontier:
        _, current = heapq.heappop(frontier)

        if current == goal:
            break

        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + 1  # 游戏中网格代价永远为1
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + heuristic(goal, next)
                heapq.heappush(frontier, (priority, next))
                came_from[next] = current

    return came_from, cost_so_far


if __name__ == '__main__':
    World.run()
