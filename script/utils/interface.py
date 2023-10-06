import os
import time
from copy import deepcopy
from threading import Thread, Lock
from typing import Optional, Tuple, Callable

import cv2
import pyautogui
import win32gui
from numpy import ndarray

import game
import log
from config import cfg
from script.utils import (window, match_template, match_template_gray, template_path, mouse, text_in_img,
                          get_text_position, where_img, calculate, template_in_img, wait_img)

import numpy as np


class ListenerUtils:
    """
    监听键盘和鼠标
    """

    def __init__(self):
        from pynput import keyboard, mouse
        self.keyboard_listener = keyboard.Listener()
        self.mouse_listener = mouse.Listener()

    def set_on_press(self, call: Callable):
        self.keyboard_listener.on_press = call

    def set_on_release(self, call: Callable):
        self.keyboard_listener.on_release = call

    def set_on_click(self, call: Callable):
        self.mouse_listener.on_click = call

    def start(self):
        self.keyboard_listener.start()
        self.mouse_listener.start()

    def stop(self):
        self.keyboard_listener.stop()
        self.mouse_listener.stop()


class RoleListener(ListenerUtils):
    """
    监听角色操作
    """

    def __init__(self):
        super().__init__()
        self._is_firing = False
        self.key_status = {'w': False, 'a': False, 's': False, 'd': False}

        self.set_on_press(self._on_press)
        self.set_on_release(self._on_release)
        self.set_on_click(self._on_click)

    @property
    def is_moving(self):
        return sum(self.key_status.values()) != 0

    @property
    def is_firing(self):
        return self._is_firing

    def _on_press(self, key):
        try:
            if key.char in self.key_status:
                self.key_status[key.char] = True
        except AttributeError:
            pass

    def _on_release(self, key):
        try:
            if key.char in self.key_status:
                self.key_status[key.char] = False
                if not self.is_moving:
                    log.debug("监听到停止移动")
        except AttributeError:
            pass

    def _on_click(self, x, y, button, pressed):
        try:
            if button.name == 'left':
                self._is_firing = pressed
        except AttributeError:
            pass


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
            time.sleep(0.1)

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

        positions = where_img(window.get_screenshot(), template_path.TRANSMISSION)  # 获取所有传送按钮坐标
        shortest_pos = calculate.calculate_shortest_position(target_pos, positions)
        h, w = cv2.imread(template_path.TRANSMISSION).shape[:2]
        mouse.click_position((shortest_pos[0] + w // 2, shortest_pos[1] + h // 2))
        time.sleep(2)


class WorldUtils(AutoUtils):
    # 移动时缩放
    # 动图放大 1.256 匹配
    def __init__(self):
        super().__init__()
        self.last_pos = (0, 0)
        self.cur_pos = (0, 0)
        self.local_map = None

        # 监听游戏角色状态
        self.role_state = RoleListener()
        self.role_state.start()

    def get_local_map(self) -> ndarray:
        """get top left map"""
        local = game.get_screenshot()
        local = local[131:131 + 128, 88: 88 + 128]
        w, h = local.shape[:2]
        center = (w // 2, h // 2)
        radius = 44  # 精准裁剪88 * 88 大小，以角色为中心
        x1, y1 = center[0] - radius, center[1] - radius
        x2, y2 = center[0] + radius, center[1] + radius
        local = local[y1:y2, x1:x2]
        self.local_map = local
        return local

    def get_angle(self):
        """get current arrow angle"""
        from script.utils import rotate_image, template_path
        local = self.get_local_map()
        only_arrow = self.only_arrow(local)
        arrow_template = cv2.imread(template_path.ARROW)

        val = 0
        angle = 0
        for i in range(0, 360):
            img = rotate_image(arrow_template, i)
            res = cv2.matchTemplate(only_arrow, img, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val > val:
                val = max_val
                angle = i

        return angle

    def get_match_pos(self, m_line, m_default=None, cnt=0, model=0, is_fighting=None):
        """
        :param m_line:  只有线条的地图
        :param m_default:  地图未经处理的原图
        :param cnt:  递归查询次数
        :param model:  查询模式    0：线条图查询  1：原图查询
        :param is_fighting: 查询方法，若正在战斗则会返回(0, 0)
        当模式为1时，但是m_default为None则切换至模式0
        """
        from .role import Role
        if is_fighting is not None:
            while is_fighting():
                time.sleep(1)
                continue
        local_map = self.get_local_map()
        local_map = self.only_arrow(local_map, nt=True)
        # 角色移动时小地图被缩小，需要将小地图放大再匹配
        if self.role_state.is_moving:
            local_map = cv2.resize(local_map, (0, 0), fx=1.256, fy=1.256)
        h, w = local_map.shape[:2]
        # 没有传入原图
        if model and m_default is None:
            log.debug("没有传入原图，将模式切换至0")
            model = 0

        if model:
            res = cv2.matchTemplate(m_default, local_map, cv2.TM_CCOEFF_NORMED)
        else:
            local_map = self.local_map_to_line(local_map)
            res = cv2.matchTemplate(m_line, local_map, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        # 阈值达不到递归查询
        if max_val < 0.4:
            log.debug(f"当前阈值: {max_val}, 阈值未达0.4开始递归查询")
            if cnt % 5 == 0:
                log.debug("尝试随机移动再查询")
                Role.random_move()
                model ^= 1
                log.debug(f"切换模式至 {model}")
            time.sleep(0.8)
            return self.get_match_pos(m_line, m_default, cnt + 1, model)

        return w, h, max_loc

    def locate_role_pos(self, m_line, m_default=None, model=0, is_fighting=None) -> Tuple[int, int]:
        """get current role position on big map"""
        w, h, top_left = self.get_match_pos(m_line, m_default, model=model, is_fighting=is_fighting)

        pos = (top_left[0] + w // 2, top_left[1] + h // 2)
        self.last_pos = self.cur_pos
        self.cur_pos = pos

        return pos

    @classmethod
    def local_map_to_line(cls, local_map):
        """返回的是灰度图"""
        white = np.array([210, 210, 210])
        gray = np.array([55, 55, 55])
        find = 1
        bw_map = np.zeros(local_map.shape[:2], dtype=np.uint8)
        # 灰块、白线：小地图中的可移动区域、可移动区域的边缘
        # b_map：当前像素点是否是灰块。只允许灰块附近（2像素）的像素被识别为白线
        b_map = deepcopy(bw_map)
        b_map[
            np.sum((local_map - gray) ** 2, axis=-1) <= 3200 + find * 1600
            ] = 255
        kernel = np.zeros((5, 5), np.uint8)  # 设置kenenel大小
        kernel += 1
        b_map = cv2.dilate(b_map, kernel, iterations=1)
        bw_map[
            (np.sum((local_map - white) ** 2, axis=-1) <= 3200 + find * 1600)
            & (b_map > 200)
            ] = 255
        return bw_map

    @classmethod
    def only_arrow(cls, img: ndarray, nt=False) -> ndarray:
        """
        nt False get only arrow map
        nt True get only deleted arrow map
        """
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # 转HSV
        lower = np.array([93, 90, 60])  # 90 改成120只剩箭头，但是角色移动过的印记会消失
        upper = np.array([97, 255, 255])
        mask = cv2.inRange(hsv, lower, upper)  # 创建掩膜
        if not nt:
            arrow = cv2.bitwise_and(img, img, mask=mask)
        else:
            arrow = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))
            # 将角色箭头和角色移动过的路径颜色设置成马路颜色
            zero = np.array([0, 0, 0])
            black = np.array([57, 57, 57])
            res = np.where(np.all(arrow == zero, axis=-1))
            coords = np.stack(res, axis=-1)
            arrow[tuple(coords.T)] = black
        return arrow


if __name__ == "__main__":
    pass
