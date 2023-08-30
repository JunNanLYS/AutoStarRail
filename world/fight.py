"""
战斗模块
"""

import time
from threading import Thread
from typing import Callable, Optional, Iterator

import cv2
import pyautogui
import numpy as np
from numpy import ndarray

from widgets import log
from utils import path, cv_tool, dialog

template_path = path.ImagePath
fight_img: Optional[ndarray] = None
fight_callable: Optional[Callable] = None  # 接受bool值
switch = False


def close():
    global switch
    switch = False
    window_message("已关闭")


def fire():
    s = time.time()
    while time.time() - s <= 3:
        pyautogui.click()
        time.sleep(0.2)


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
    if cv_tool.template_in_img(fight_img, template1) or cv_tool.template_in_img(fight_img, template2):
        return True
    return False


def in_fighting() -> bool:
    """
    查询未开启的自动战斗模板图
    查询3种不同的自动战斗模板图
    """
    templates = [template_path.AUTO_FIGHT, template_path.AUTO_FIGHT_2,
                 template_path.AUTO_FIGHT_3, template_path.AUTO_FIGHT_4]
    for template in templates:
        if cv_tool.template_in_img(fight_img, template):
            return True
    return False


def update_img():
    """
    更新游戏图像
    """
    global fight_img
    from PIL import ImageGrab
    import win32gui
    while True:
        hwnd = win32gui.GetForegroundWindow()
        text = win32gui.GetWindowText(hwnd)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        if text != "崩坏：星穹铁道":
            continue
        break
    img = ImageGrab.grab(bbox=(left, top, right, bottom))
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    fight_img = img
    # cv2.imwrite(config.abspath + r'\temp\fight.png', fight_img)


def main():
    while switch:
        update_img()
        if have_jar() or have_monster():
            fight_callable(True)
            fire()
        if in_fighting():
            # 战斗中直接休眠一会再查看
            fight_callable(True)
            time.sleep(0.3)
            continue
        fight_callable(False)


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


def window_message(content: str):
    dialog.new_win_message("战斗模块", content)


if __name__ == '__main__':
    def f(b):
        print(f"已设置为{b}")
    set_callable(f)
    start()
    # time.sleep(2)
    # close()
