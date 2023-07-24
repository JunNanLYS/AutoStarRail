import time
import pyautogui
import win32api
import win32con
import json

from time import perf_counter
from pynput import keyboard
from pynput.keyboard import Key, KeyCode

"""
录制工具
w, a, s, d 移动角色
x 角色攻击
上下左右键是控制角色视角, 例如按 <- 或 -> 等价于鼠标向左或者向右移动
f7暂停录制, f8关闭录制
"""

is_stop = False  # 暂停录制
is_release = True  # 用来判断按键是否释放
character_key = ['w', 'a', 's', 'd', 'x', 'shift']  # 角色移动按键
character_view = ['left', 'right', 'up', 'down']  # 视角按键 | 上下左右键控制角色视角
special_key = ['f7', 'f8']  # 特殊按键
event_list = []  # 事件
last_time = 0  # 键盘按压的时间
key_dict = {}  # 按键信息 {key: time}
filename = f"./map/world.json"  # 文件名


def key_to_str(key):
    """
    将按键转化成字符串
    """
    if isinstance(key, KeyCode):
        return key.char
    elif isinstance(key, Key):
        return key.name
    else:
        return ""


def move_view(k: str):
    """
    移动视角
    传入left就映射到鼠标向左移动
    """
    k_to_tuple = {'left': (-300, 0),
                  'right': (300, 0),
                  'up': (0, -300),
                  'down': (0, 300)}
    if k not in k_to_tuple:
        raise ValueError("请输入正确的方向")
    x, y = k_to_tuple[k]
    win32api.mouse_event(win32con.MOUSE_MOVED, x, y)  # 移动视角


def on_press(key):
    global last_time, is_stop, is_release
    key = key_to_str(key)
    if is_release:
        last_time = perf_counter()
    # 跳过不监听的按键
    if key not in character_key and key not in character_view and key not in special_key:
        return None
    # 暂停录制
    if key == 'f7':
        is_stop = False if is_stop else True
        return None
    # 退出录制
    if key == 'f8':
        return False
    if is_stop:
        print("您已暂停录制，按f7继续录制")
        return None

    if key in character_key:
        if key == 'x':
            pyautogui.click()
    elif key in character_view:
        # 移动角色视角
        move_view(key)
        # 记录
        event_list.append({'key': key, 'time': 0})
    is_release = False


def on_release(key):
    global is_release
    key = key_to_str(key)
    current_time = perf_counter()
    # 跳过不监听的按键
    if key not in character_key and key not in character_view and key not in special_key:
        return None
    if is_stop:
        print("您已暂停录制，按f7继续录制")
        return None

    if key in character_key:
        event_list.append({'key': key, 'time': current_time - last_time})

    is_release = True


def start():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == '__main__':
    print("录制将在2秒后开始")
    time.sleep(2)
    print("录制开始")
    start()
    json_dict = {"map_name": "",
                 "number": "",
                 "name": "NanJun",
                 "keys": event_list}
    print(event_list)
    with open(filename, 'w') as f:
        json.dump(json_dict, f)
