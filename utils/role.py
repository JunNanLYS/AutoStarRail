"""
该模块放置控制角色用的一些方法
"""
import time
from enum import Enum
from copy import deepcopy

import cv2
import numpy as np
import win32api
import win32con
import pyautogui

from utils import path, cv_tool

filename = path.ImagePath


class Direction(Enum):
    UP = 'up'
    DOWN = 'down'
    LEFT = 'left'
    RIGHT = 'right'


class MoveDirection(Enum):
    ONWARD = 'onward'  # 前
    BACKWARD = 'backward'  # 后
    LEFT = 'left'  # 左
    RIGHT = 'right'  # 右
    FORWARD_LEFT = 'forward_left'  # 左前
    FORWARD_RIGHT = 'forward_right'  # 右前
    BACKWARD_LEFT = 'backward_left'  # 左后
    BACKWARD_RIGHT = 'backward_right'  # 右后


def _mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSE_MOVED, x, y)


class Role:
    angle = 0

    @classmethod
    def move_view(cls, direction: Direction, angle: int):
        """
        :param direction: 方向
        :param angle: 角度
        """

        point = int(28 * angle)
        dic = {
            Direction.UP: (0, -point),
            Direction.DOWN: (0, point),
            Direction.LEFT: (-point, 0),
            Direction.RIGHT: (point, 0)
        }
        if direction not in dic:
            raise ValueError(f"direction {direction} not in {dic}")
        _mouse_move(*dic[direction])

    @classmethod
    def move_position(cls, direction: MoveDirection, point: int):
        """
        0.5s = [7, 7, 7, 7, 8, 8, 8, 8, 8, 7, 7, 8, 8, 8, 8, 7, 7, 7, 7, 8]
        1s = [17, 17, 17, 18, 18, 18, 18, 17, 17, 17, 17, 18, 18, 17, 17, 17, 17, 17, 17, 17]
        1.5s = [26, 27, 27, 27, 27, 27, 27, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 26, 26, 27]
        0.5s走9格像素点
        :param direction: 移动方向枚举类
        :param point:  要移动的像素点数量
        """
        dic = {
            MoveDirection.ONWARD: ('w',),
            MoveDirection.BACKWARD: ('s',),
            MoveDirection.LEFT: ('a',),
            MoveDirection.RIGHT: ('d',),
            MoveDirection.FORWARD_LEFT: ('w', 'a'),
            MoveDirection.FORWARD_RIGHT: ('w', 'd'),
            MoveDirection.BACKWARD_LEFT: ('s', 'a'),
            MoveDirection.BACKWARD_RIGHT: ('s', 'd')
        }
        if direction not in dic:
            raise ValueError(f"direction {direction} not in {dic}")
        second = round(point / 9, 2) * 0.5
        pyautogui.keyDown(*dic[direction])
        time.sleep(second)
        pyautogui.keyUp(*dic[direction])

    @classmethod
    def get_angle(cls, map_screen) -> int:
        """
        传入小地图或者大地图截图，返回角色朝向角度
        :param map_screen: 大地图或小地图
        :return: 角色朝向角度
        """
        lower_blue = np.array([234, 191, 4])  # 蓝色下限
        upper_blue = np.array([255, 209, 73])  # 上限
        arrow = cv2.imread(filename.ARROW)
        screen = deepcopy(map_screen)
        screen[np.sum(screen - lower_blue, axis=-1) < 0] = [0, 0, 0]
        screen[np.sum(screen - upper_blue, axis=-1) > 0] = [0, 0, 0]

        val = 0
        angle = 0

        for i in range(360):
            rotated = cv_tool.rotate_image(arrow, i)
            res = cv2.matchTemplate(screen, rotated, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val > val:
                val = max_val
                angle = i
        cls.angle = angle
        return angle

    @classmethod
    def set_angle(cls, current: int, target: int):
        """
        :param current:
        :param target:
        """
        angle = target - current
        if angle < 0:
            # angle = abs(angle)
            # if angle > 90:
            #     cnt = angle // 90
            #     angle = angle % 90
            #     for _ in range(cnt):
            #         cls.move_view(Direction.RIGHT, 90)
            cls.move_view(Direction.RIGHT, -angle)
        else:
            # if angle > 90:
            #     cnt = angle // 90
            #     angle = angle % 90
            #     for _ in range(cnt):
            #         cls.move_view(Direction.LEFT, 90)
            cls.move_view(Direction.LEFT, angle)
        time.sleep(0.5)
        pyautogui.press('ctrl')
        time.sleep(0.1)
        pyautogui.press('w')
        pyautogui.press('ctrl')
        time.sleep(0.1)
        cls.angle = target



if __name__ == '__main__':
    Role.set_angle(90, 180)