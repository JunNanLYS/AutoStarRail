"""
战斗模块
"""
from enum import Enum
import time
from threading import Thread
from typing import Callable, Optional, Iterator

import cv2
import pyautogui
import numpy as np
from numpy import ndarray

from widgets import log
from utils import path, cv_tool, dialog


class StateFlag(Enum):
    FIRE = "fire"
    FIGHTING = "fighting"
    MOVE = "move"


template_path = path.ImagePath
fight_img: Optional[ndarray] = None
fight_callable: Optional[Callable] = None  # 接受bool值
state: StateFlag = StateFlag.MOVE  # 状态
switch = False


def close():
    global switch
    switch = False
    window_message("已关闭")


def fire():
    set_state(StateFlag.FIRE)
    s = time.time()
    while time.time() - s <= 3:
        pyautogui.click()
        time.sleep(0.2)
    time.sleep(1.5)


def have_jar() -> bool:
    """
    查找是否有锁定罐子
    """
    img = cv_tool.in_range_color(fight_img, [255, 255, 240], [255, 255, 255])
    template = cv2.imread(template_path.SELECT_JAR)
    return cv_tool.template_in_img(img, template, threshold=0.7)


def have_monster() -> bool:
    """
    1. 查找问号
    2. 查找感叹号
    3. 查找锁定敌人标志(暂时还没办法解决)
    """
    template1 = cv2.imread(template_path.QUESTION_MASK)
    template2 = cv2.imread(template_path.WARNING)
    res1 = cv_tool.template_in_img(fight_img, template1, threshold=0.82)
    res2 = cv_tool.template_in_img(fight_img, template2, threshold=0.82)
    if res1 or res2:
        return True
    return False


def in_fighting() -> bool:
    """
    匹配未开启的自动战斗模板图
    匹配3种不同的自动战斗模板图
    匹配不到前自动战斗模板则匹配手机模板
    """
    templates = [template_path.AUTO_FIGHT, template_path.AUTO_FIGHT_2,
                 template_path.AUTO_FIGHT_3, template_path.AUTO_FIGHT_4]
    for template in templates:
        if cv_tool.template_in_img(fight_img, template):
            set_state(StateFlag.FIGHTING)
            return True
    res = cv_tool.match_template_gray(fight_img, template_path.PHONE)
    if res == (-1, -1):
        set_state(StateFlag.FIGHTING)
        return True
    return False


def update_img():
    """
    更新游戏图像
    """
    global fight_img
    from PIL import ImageGrab
    import win32gui
    import ctypes
    left, top, right, bottom = 0, 0, 0, 0
    while True:
        hwnd = win32gui.GetForegroundWindow()
        text = win32gui.GetWindowText(hwnd)
        s = ctypes.windll.user32.GetDpiForWindow(hwnd) / 96.0
        try:
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        except Exception as e:
            log.transmitDebugLog(f"更新图像错误: {e}")
            continue
        if text != "崩坏：星穹铁道":
            continue
        break
    img = ImageGrab.grab(bbox=(left * s, top * s, right * s, bottom * s))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    fight_img = img
    # cv2.imwrite(config.abspath + r'\temp\fight.png', fight_img)


def main():
    while switch:
        update_img()
        if have_jar():
            log.transmitDebugLog("匹配到罐头")
            fight_callable(True)
            fire()
        if have_monster():
            log.transmitDebugLog("匹配到怪物")
            fight_callable(True)
            fire()
        if in_fighting():
            # 战斗中直接休眠一会再查看
            log.transmitDebugLog("正在战斗")
            fight_callable(True)
            time.sleep(0.3)
            continue
        fight_callable(False)
        set_state(StateFlag.MOVE)


def start():
    global switch
    switch = True
    thread = Thread(target=main)
    thread.start()
    window_message("已开启")


def set_callable(call: Callable):
    """
    设置回调函数，该回调函数应当接收bool值
    """
    global fight_callable
    fight_callable = call


def set_state(flag: StateFlag):
    global state
    state = flag


def window_message(content: str):
    dialog.new_win_message("战斗模块", content)


if __name__ == '__main__':
    def f(b):
        print(f"已设置为{b}")


    set_callable(f)
    start()
    # time.sleep(2)
    # close()
