"""
战斗模块
"""
import time
from threading import Thread
from typing import Callable, Optional

import cv2
import numpy as np
import pyautogui
from numpy import ndarray

import game
import log
from script.utils import template_path

fight_img: Optional[ndarray] = None
fight_callable: Optional[Callable] = None  # 接受bool值
switch = False
is_fighting = False


def close():
    global switch
    log.info("关闭战斗模块")
    switch = False


def fire():
    s = time.time()
    while time.time() - s <= 1:
        pyautogui.click()
        time.sleep(0.2)
    time.sleep(1.5)


def have_jar() -> bool:
    """
    查找是否有锁定罐子
    """
    from script.utils import in_range_color, template_in_img
    img = in_range_color(fight_img, [255, 255, 240], [255, 255, 255])
    template = cv2.imread(template_path.SELECT_JAR)
    return template_in_img(img, template, threshold=0.7)


def have_monster() -> bool:
    """
    1. 查找问号
    2. 查找感叹号
    3. 查找锁定敌人标志(暂时还没办法解决)
    """
    from script.utils import template_in_img
    template1 = cv2.imread(template_path.QUESTION_MASK)
    template2 = cv2.imread(template_path.WARNING)
    res1 = template_in_img(fight_img, template1, threshold=0.82)
    res2 = template_in_img(fight_img, template2, threshold=0.82)
    if res1 or res2:
        return True
    return False


def in_fighting() -> bool:
    """
    匹配未开启的自动战斗模板图
    匹配3种不同的自动战斗模板图
    匹配不到前自动战斗模板则匹配手机模板
    """
    global is_fighting
    from script.utils import template_in_img, match_template_gray
    templates = [template_path.AUTO_FIGHT, template_path.AUTO_FIGHT_2,
                 template_path.AUTO_FIGHT_3, template_path.AUTO_FIGHT_4]
    for template in templates:
        if template_in_img(fight_img, template):
            is_fighting = True
            return True
    res = match_template_gray(fight_img, template_path.PHONE)
    if res == (-1, -1):
        is_fighting = True
        return True
    is_fighting = False
    return False


def update_img():
    """
    更新游戏图像
    """
    global fight_img
    fight_img = game.get_screenshot()


def main():
    while switch:
        update_img()
        if have_jar():
            # fight_callable(True)
            fire()
        if have_monster():
            # fight_callable(True)
            fire()
        if in_fighting():
            # 战斗中直接休眠一会再查看
            # fight_callable(True)
            time.sleep(0.3)
            continue
        # fight_callable(False)


def start():
    global switch
    log.info("开启战斗模块")
    switch = True
    thread = Thread(target=main)
    thread.start()


def set_callable(call: Callable):
    """
    设置回调函数，该回调函数应当接收bool值
    """
    global fight_callable
    fight_callable = call


if __name__ == '__main__':
    def f(b):
        print(f"已设置为{b}")


    set_callable(f)
    start()
    # time.sleep(2)
    # close()
