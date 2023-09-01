import os
import time

import cv2
import numpy as np

from widgets import log
from world.data import BALL_NAME, AREA_NAME, AREA_POINT, AREA_SCROLL
from utils.path import ImagePath

img_filename = ImagePath


def click_position(position):
    """鼠标移动至position并点击"""
    import win32api
    import win32con
    x, y = int(position[0]), int(position[1])
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)  # 过快的点击将导致游戏反应不过来最终导致点击失效
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_positions(positions):
    """
    传入单个值则点击该值，多个值则取索引为 元素个数/2 的坐标
    """
    length = len(positions)
    mid = length // 2 - 1
    if mid < 0:
        mid = 0
    pos = positions[mid]
    x, y = int(pos[0]), int(pos[1])
    click_position((x, y))


def wait_img(template, threshold=0.8):
    """等待模板图"""
    import game
    from utils.cv_tool import template_in_img
    screenshot = game.screenshot()
    while not template_in_img(screenshot, template, threshold=threshold):
        time.sleep(0.1)
        screenshot = game.screenshot()


def mouse_scroll(count: int):
    """
    鼠标滚轮
    """
    import pyautogui
    for _ in range(count):
        for _ in range(6):
            pyautogui.scroll(-10)


class Map:
    def __init__(self):
        from typing import Optional
        from numpy import ndarray
        self.img: Optional[ndarray] = None

    def update_img(self):
        """更新游戏内图像"""
        import game
        self.img = game.screenshot()


class WorldMap(Map):
    def __init__(self):
        super().__init__()
        import os
        import config
        self.map_img_root = os.path.join(
            config.abspath,
            "world",
            "map"
        )
        self.cur_ball: int = 0
        self.cur_area: int = 0
        self.cur_point: int = 0
        self.pre_ball: int = 0
        self.pre_area: int = 0
        self.pre_point: int = 0

    @classmethod
    def get_ball_name(cls, ball_id):
        return BALL_NAME[ball_id]

    @classmethod
    def get_area_name(cls, ball_id, area_id):
        return AREA_NAME[ball_id][area_id - 1]

    def update_map(self):
        """更新角色所处地图"""
        if self.cur_ball != self.pre_ball:
            self.into_ball(self.cur_ball)
            wait_img(img_filename.AREA_NAVIGATION)  # 等待进入
            self.into_area(self.cur_ball, self.cur_area)
            self.into_point(self.cur_ball, self.cur_area, self.cur_point)
        elif self.cur_area != self.pre_area:
            self.into_map()
            self.into_area(self.cur_ball, self.cur_area)
            self.into_point(self.cur_ball, self.cur_area, self.cur_point)
        else:
            self.into_map()
            self.into_point(self.cur_ball, self.cur_area, self.cur_point)

    @classmethod
    def into_map(cls):
        """
        进入地图界面
        """
        from utils.func import to_game_main
        from config import config as cfg
        import pyautogui
        open_key = cfg.open_map
        while not to_game_main():
            log.transmitDebugLog("没有进入主界面", debug=True)
            time.sleep(1)
        pyautogui.press(open_key)
        time.sleep(1.5)

    def into_ball(self, ball_id):
        """
        进入指定星球
        """
        from utils import ocr, window
        self.into_map()
        # 进入星轨航图
        screenshot = window.get_screenshot()
        positions = ocr.get_text_position(screenshot, "星轨航图")
        click_positions(positions)
        wait_img(img_filename.BALL_NAVIGATION)
        # 进入星球
        screenshot = window.get_screenshot()
        name = BALL_NAME[ball_id]  # 星球名称
        positions = ocr.get_text_position(screenshot, name)
        add = np.array([-80, -80])
        positions = positions + add
        click_positions(positions)

    def into_area(self, ball_id, area_id):
        """
        进入(点击)某星球中某区域
        """
        from utils import ocr, window
        import pyautogui
        area_name = self.get_area_name(ball_id, area_id)
        cnt = AREA_SCROLL.get(area_name, 0)
        if cnt:
            # 将鼠标移动至观景车厢
            log.transmitDebugLog(f"{area_name}需要滚动后查找", level=2)
            pos = ocr.get_text_position(window.get_screenshot(), "观景车厢")
            pyautogui.moveTo(pos[0][0], pos[0][1])
            mouse_scroll(cnt)  # 滚动
        positions = ocr.get_text_position(window.get_screenshot(), area_name)
        click_positions(positions)
        time.sleep(0.5)

    def into_point(self, ball_id, area_id, point_id):
        pass

    @property
    def map_path(self):
        path = os.path.join(
            self.map_img_root,
            str(self.cur_ball),
            f"{self.cur_area}-{self.cur_point}"
        )
        return path


if __name__ == '__main__':
    m = WorldMap()
    m.into_area(2, 8)
