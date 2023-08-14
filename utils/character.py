"""
该模块放置控制角色用的一些方法
"""
from enum import Enum

import win32api, win32con
import pyautogui


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


def move_view(direction: Direction):
    point = 2400  # 90度转角
    dic = {
        Direction.UP: (0, -point),
        Direction.DOWN: (0, point),
        Direction.LEFT: (-point, 0),
        Direction.RIGHT: (point, 0)
    }
    if direction not in dic:
        raise ValueError(f"direction {direction} not in {dic}")
    _mouse_move(*dic[direction])


def move_position(direction: MoveDirection, point: int):
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
    for _ in range(point):
        pyautogui.press(*dic[direction])


if __name__ == '__main__':
    import time
    import pyautogui

    time.sleep(1)
    # move_view(Direction.LEFT)
    # time.sleep(0.3)
    move_position(MoveDirection.LEFT, 10)
