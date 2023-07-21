import time
import pyautogui
import win32api
import win32con
import json

from pynput import keyboard
from pynput.keyboard import Key, KeyCode

"""
录制工具
w, a, s, d 移动角色
x 角色攻击
上下左右键是控制角色视角, 例如按 <- 或 -> 等价于鼠标向左或者向右移动
"""

is_stop = False
key_board = ['w', 'a', 's', 'd', 'x', 'shift']  # 角色移动按键
key_move_view = ['left', 'right', 'up', 'down']  # 视角按键 | 上下左右键控制角色视角
key_list = []
is_curren_key = None


def move_view(k: str):
    k_to_int = {'left': (-500, 0),
                'right': (500, 0),
                'up': (0, -500),
                'down': (0, 500)}
    if k not in k_to_int:
        raise ValueError("请输入正确的方向")
    x, y = k_to_int[k]
    win32api.mouse_event(win32con.MOUSE_MOVED, x, y)  # 移动视角


def on_press(key):
    global is_stop, is_curren_key
    if isinstance(key, Key) and key.name == 'f7':
        is_stop = False if is_stop else True
        return None
    if is_stop:
        print("你已暂停录制请按f7恢复录制")
        return None

    if isinstance(key, Key):
        key = key.name
        # f8暂停录制
        if key == 'f8':
            return False
        if key in key_move_view:
            move_view(key)
    elif isinstance(key, KeyCode):
        key = key.char
        if key == 'x':
            pyautogui.click()
    if key not in key_board and key not in key_move_view:
        return None
    # 同一个按键不重复记录，等释放
    if key == is_curren_key and key not in key_move_view:
        return None
    elif key == is_curren_key and key in key_move_view:
        key_list[-1][1] += 1
        return None
    # 移动
    if key in key_board:
        key_list.append([key, time.time()])
    # 视角
    elif key in key_move_view:
        key_list.append([key, 1])
    is_curren_key = key


def on_release(key):
    global is_curren_key
    if is_stop:
        return None
    if isinstance(key, Key):
        key = key.name
    elif isinstance(key, KeyCode):
        key = key.char
    if key in key_board:
        start_time = key_list[-1][1]
        key_list[-1][1] = time.time() - start_time
    is_curren_key = None


# 启动录制，f8关闭录制
with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()

print(key_list)
map_name = "大世界"
with open(fr'..\map\{map_name}.json', 'w') as f:
    json.dump(key_list, f)
