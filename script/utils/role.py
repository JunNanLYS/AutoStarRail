import time
from enum import Enum
from copy import deepcopy

import cv2
import numpy as np
import win32api
import win32con
import pyautogui

import threadpool
from script.utils import template_path
from config import cfg


class MoveDirection(Enum):
    ONWARD = 'onward'  # 前
    BACKWARD = 'backward'  # 后
    LEFT = 'left'  # 左
    RIGHT = 'right'  # 右


def _mouse_move(x, y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, x, y)


class Role:
    angle = 0
    direct = 'w'

    @classmethod
    def move_view(cls, angle):
        """
        移动角色视角，正angle右转，负angle左转。
        本代码参考自github项目Auto_Simulated_Universe
        :param angle: 角度
        """
        import game

        if angle > 30:
            y = 30
        elif angle < -30:
            y = -30
        else:
            y = angle
        # 分多次移动，防止鼠标移动离开游戏窗口
        _, _, s = game.get_somthing()
        dx = int(16.5 * y * cfg.get(cfg.world_angle) * s)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, 0)  # 进行视角移动
        time.sleep(0.05)
        if angle != y:
            Role.move_view(angle - y)

    @classmethod
    def move_position(cls, point: int, direction: MoveDirection = MoveDirection.ONWARD):
        """
        0.5s = [7, 7, 7, 7, 8, 8, 8, 8, 8, 7, 7, 8, 8, 8, 8, 7, 7, 7, 7, 8]
        1s = [17, 17, 17, 18, 18, 18, 18, 17, 17, 17, 17, 18, 18, 17, 17, 17, 17, 17, 17, 17]
        1.5s = [26, 27, 27, 27, 27, 27, 27, 26, 26, 26, 26, 26, 27, 27, 27, 27, 27, 26, 26, 27]
        0.5s走9格像素点
        :param direction: 移动方向枚举类
        :param point:  要移动的像素点数量
        :return: 线程future
        """
        dic = {
            MoveDirection.ONWARD: 'w',
            MoveDirection.BACKWARD: 's',
            MoveDirection.LEFT: 'a',
            MoveDirection.RIGHT: 'd',
        }
        if direction not in dic:
            raise ValueError(f"direction {direction} not in {dic}")
        cls.direct = dic[direction]
        second = round(point / 9, 2) * 0.5

        def move():
            pyautogui.keyDown(dic[direction])
            time.sleep(second)
            pyautogui.keyUp(dic[direction])

        future = threadpool.function_thread.submit(move)
        return future

    @classmethod
    def move(cls):
        pyautogui.keyDown('w')
        pyautogui.press('shift')
        cls.direct = 'w'

    @classmethod
    def random_move(cls):
        """
        随便移动
        """
        from random import randint
        moves = ['w', 'a', 's', 'd']
        d = moves[randint(0, 3)]
        pyautogui.keyDown(d)
        time.sleep(1)
        pyautogui.keyUp(d)
        cls.direct = d

    @classmethod
    def obstacles(cls):
        """越障"""
        from random import randint
        moves = ['a', 'd']
        d = moves[randint(0, 1)]
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        pyautogui.keyDown(d)
        time.sleep(1)
        pyautogui.keyUp(d)
        cls.direct = d

    @classmethod
    def stop_move(cls):
        """
        停止角色移动
        """
        pyautogui.keyUp(cls.direct)

    @classmethod
    def get_angle(cls, map_screen) -> int:
        """
        传入小地图或者大地图截图，返回角色朝向角度。（已不使用）
        :param map_screen: 大地图或小地图
        :return: 角色朝向角度
        """
        # 这里需要改成使用HSV的方式
        from script.utils import rotate_image
        lower_blue = np.array([234, 191, 4])  # 蓝色下限
        upper_blue = np.array([255, 209, 73])  # 上限
        arrow = cv2.imread(template_path.ARROW)
        screen = deepcopy(map_screen)
        screen[np.sum(screen - lower_blue, axis=-1) < 0] = [0, 0, 0]
        screen[np.sum(screen - upper_blue, axis=-1) > 0] = [0, 0, 0]

        val = 0
        angle = 0

        for i in range(360):
            rotated = rotate_image(arrow, i)
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

        if angle > 0:
            if angle <= 180:
                cls.move_view(-angle)
            else:
                cls.move_view(360 - angle)
        else:
            angle = abs(angle)
            if angle <= 180:
                cls.move_view(angle)
            else:
                cls.move_view(-(360 - angle))

        cls.angle = target
