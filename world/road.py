import os
from queue import Queue
from typing import Tuple, Optional, List

import numpy as np

import config
from widgets import log

import cv2


class Point(object):
    def __init__(self, point: Tuple[int, int]):
        self._point = point

    @property
    def tuple(self):
        return self._point

    @property
    def x(self):
        return self._point[0]

    @property
    def y(self):
        return self._point[1]

    @property
    def up_left(self):
        return Point((self.x - 1, self.y - 1))

    @property
    def up(self):
        return Point((self.x, self.y - 1))

    @property
    def up_right(self):
        return Point((self.x + 1, self.y - 1))

    @property
    def right(self):
        return Point((self.x + 1, self.y))

    @property
    def down_right(self):
        return Point((self.x + 1, self.y + 1))

    @property
    def down(self):
        return Point((self.x, self.y + 1))

    @property
    def down_left(self):
        return Point((self.x - 1, self.y + 1))

    @property
    def left(self):
        return Point((self.x - 1, self.y))

    def get_all_directions(self):
        return (
            self.up_left, self.up, self.up_right,
            self.left, self.right,
            self.down_left, self.down, self.down_right
        )


def a_star(graph, start, goal, heuristic):
    """
    A* 算法（A-star Algorithm）是一种用于图形遍历和路径查找的算法，它能够有效地找到从起点到终点的最短路径。
    它是一种启发式搜索算法，通过结合 Dijkstra 算法和最佳优先搜索算法的优点，能够在保证找到最短路径的同时，提高搜索速度。
    """
    pass


def get_road(filename: str):
    """
    返回路径
    :param filename: 地图路径
    """
    img = cv2.imread(filename)
    start_point = get_start_position(filename)  # 起点坐标
    move_set = {start_point}  # 访问过的像素
    road = [start_point]
    h, w = img.shape[:2]
    stack: List[Point] = [*Point(start_point).get_all_directions()]  # 模拟递归防止爆栈
    while stack:
        top = stack.pop()
        x, y = top.x, top.y
        if np.all(img[y][x] == [0, 0, 255]):
            road.append(top.tuple)
            move_set.add(top.tuple)
            # 获取四周没访问过的像素
            for nex in top.get_all_directions():
                if nex.x < 0 or nex.y < 0 or nex.x >= w or nex.y >= h:
                    continue
                if nex.tuple not in move_set:
                    stack.append(nex)

    return road


def get_start_position(filename: str) -> Tuple[int, int]:
    """
    起点颜色必须是[0, 255, 0] BGR格式
    :param filename: 地图
    :return: 返回地图中路线的起点(x, y)
    """
    img = cv2.imread(filename)
    # 查找所有绿色像素
    target = np.all(img == [0, 255, 0], axis=-1)
    matches = np.where(target)
    if matches[0].size == 0:
        log.transmitDebugLog(f"地图中没有起点[{filename}]", level=3)
        return -1, -1
    log.transmitDebugLog(f"查询到起点[{filename}],{matches[0][0]} {matches[1][0]}", level=2)
    return matches[1][0], matches[0][0]


if __name__ == '__main__':
    # import sys
    #
    # sys.setrecursionlimit(3000)
    root = config.abspath
    have_green = os.path.join(root, r'world\map\2', 'test.png')
    r = get_road(have_green)
    print(r)
    # print(len(r))
    # print(len(set(r)))
    # image = cv2.imread(have_green)
    # h, w = image.shape[:2]

    # print(image[10][10])
    # cv2.circle(image, (x, y), 0, (255, 0, 0))
    # cv2.imshow('image', image)
    # cv2.waitKey(0)
