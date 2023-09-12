import time
from threading import Thread, Lock
from typing import Optional

import cv2
import pyautogui
import win32gui
from numpy import ndarray

import game
import log
from config import cfg
from script.utils import (window, match_template, match_template_gray, template_path, mouse, text_in_img,
                          get_text_position, where_img, calculate)


class AutoUtils:
    def __init__(self):
        self.thread: Optional[Thread] = None
        self.screenshot_lock = Lock()
        self.in_game_lock = Lock()
        self._in_game = False
        self._stop = False
        self._screenshot: Optional[ndarray] = None

    def auto(self):
        """2 sec update screenshot"""
        while not self._stop:
            text = win32gui.GetWindowText(win32gui.GetForegroundWindow())
            if text != "崩坏：星穹铁道":
                with self.in_game_lock:
                    self._in_game = False
                log.debug("游戏并不是活动窗口，请将游戏设置为活动窗口")
                time.sleep(0.2)
                continue
            with self.in_game_lock:
                self._in_game = True
            self._update_screenshot()
            time.sleep(0.2)

    @property
    def in_game(self) -> bool:
        with self.in_game_lock:
            return self._in_game

    def in_book(self) -> bool:
        return text_in_img(self.screenshot, "星际和平指南")

    def into_book(self):
        """into a book interface"""
        self.wait_game()

        game.to_game_main()
        pos = match_template_gray(self.screenshot, template_path.BOOK)  # get template position
        pyautogui.keyDown('alt')
        mouse.click_position(pos)
        pyautogui.keyUp('alt')

    def into_daily(self):
        """daily task in book interface"""
        self.wait_game()

        # you must in book interface
        if not self.in_book():
            self.into_book()
        time.sleep(1.5)

        pos = match_template(self.screenshot, template_path.DAILY_TASK)
        if pos == (-1, -1):
            log.debug("匹配不到未选中的每日任务，判断已经在该界面")
            return
        pyautogui.keyDown('alt')
        mouse.click_position(pos)
        pyautogui.keyUp('alt')

    def into_index(self):
        """Survival index in book interface"""
        self.wait_game()

        # you must in book interface
        if not self.in_book():
            self.into_book()
        time.sleep(1.5)

        pos = match_template(self.screenshot, template_path.INDEX)
        if pos == (-1, -1):
            log.debug("匹配不到未选中的生存索引，判断已经在该界面")
            return
        pyautogui.keyDown('alt')
        mouse.click_position(pos)
        pyautogui.keyUp('alt')

    @property
    def screenshot(self) -> ndarray:
        """get window screenshot"""
        with self.screenshot_lock:
            return self._screenshot

    def start(self):
        """start auto utils"""
        self._stop = False
        self.thread = Thread(target=self.auto)
        self.thread.start()

    def stop(self):
        """stop auto utils"""
        self._stop = True

    def wait_game(self):
        """wait game window"""
        while not self.in_game:
            time.sleep(0.2)

    def _update_screenshot(self):
        """update window screenshot"""
        with self.screenshot_lock:
            self._screenshot = window.get_screenshot()


class AbyssUtils(AutoUtils):
    def __init__(self):
        super().__init__()

    def into_abyss(self):
        """abyss in index interface"""
        self.wait_game()

        # you must in index interface
        if not self.in_book():
            self.into_index()

        time.sleep(1.5)
        try:
            universe_text_pos = get_text_position(self.screenshot, "模拟宇宙")
            mouse.click_positions(universe_text_pos)
            mouse.mouse_scroll(3)
        except Exception:
            # reload your book
            game.to_game_main()
            return self.into_abyss()

        time.sleep(1)
        abyss_text_pos = get_text_position(self.screenshot, "忘却之庭")
        mouse.click_positions(abyss_text_pos)

        time.sleep(1)
        pos = get_text_position(self.screenshot, "传送")
        mouse.click_positions(pos)


class DailyTaskUtils(AutoUtils):
    def __init__(self):
        super().__init__()
        self.daily_task = ...


class StaminaUtils(AutoUtils):
    def __init__(self):
        super().__init__()


class UniverseUtils(AutoUtils):
    def __init__(self):
        super().__init__()
        self.NUMBER_TO_TEXT = {3: "三", 4: "四", 5: "五", 6: "六", 7: "七"}

    def into_universe(self):
        """into a universe interface"""
        self.wait_game()

        # you must in book interface
        if not self.in_book():
            self.into_index()

        time.sleep(1.5)
        try:
            universe_text_pos = get_text_position(self.screenshot, "模拟宇宙")
            mouse.click_positions(universe_text_pos)
        except Exception:
            # reload your book
            game.to_game_main()
            return self.into_universe()

        time.sleep(1)
        week_pos = get_text_position(self.screenshot, "本周积分")
        week_pos = week_pos[0]
        mouse.click_position((week_pos[0] - 50, week_pos[1]))
        mouse.mouse_scroll(2)

        try:
            target_text = self.NUMBER_TO_TEXT[cfg.get(cfg.universe_number)]
        except Exception:
            target_text = self.NUMBER_TO_TEXT[6]
        log.info(f"查找模拟宇宙{target_text}")
        while not text_in_img(self.screenshot, target_text):
            mouse.mouse_scroll(3)
        target_pos = get_text_position(self.screenshot, target_text)[0]

        transmission = where_img(window.get_screenshot(), template_path.TRANSMISSION)  # 获取所有传送按钮坐标
        positions = []
        for i in range(len(transmission[0])):
            positions.append((transmission[1][i], transmission[0][i]))
        shortest_pos = calculate.calculate_shortest_position(target_pos, positions)
        h, w = cv2.imread(template_path.TRANSMISSION).shape[:2]
        mouse.click_position((shortest_pos[0] + w // 2, shortest_pos[1] + h // 2))
        time.sleep(2)


if __name__ == "__main__":
    abyss_utils = UniverseUtils()
    abyss_utils.start()
    abyss_utils.into_universe()
    abyss_utils.stop()
