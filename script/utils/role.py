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
    obs = 0

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

    @classmethod
    def obstacles(cls):
        """越障"""
        moves = ['a', 'd']
        cls.obs ^= 1
        d = moves[cls.obs]
        pyautogui.keyDown('s')
        time.sleep(1)
        pyautogui.keyUp('s')
        pyautogui.keyDown(d)
        time.sleep(0.8)
        pyautogui.keyUp(d)

    @classmethod
    def stop_move(cls):
        """
        停止角色移动
        """
        pyautogui.keyUp(cls.direct)

    @classmethod
    def set_angle(cls, current: int, target: int):
        """传入当前角度和期望角度，该方法将计算需要移动的角度"""
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
