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

        transmission = where_img(window.get_screenshot(), template_path.TRANSMISSION)  # 获取所有传送按钮坐标
        positions = []
        for i in range(len(transmission[0])):
            positions.append((transmission[1][i], transmission[0][i]))
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

        self.map_path = ""
        self.big_map = np.array([])
        self.big_map_binary = np.array([])
        self.big_map_target = np.array([])
        self.local_map = np.array([])  # 小地图
        self.point_img = np.array([])  # 传送点

        self.world_name = 1
        self.area_name = 1

        # 监听游戏角色状态
        self.role_state = RoleListener()
        self.role_state.start()

    @classmethod
    def in_area_navigation(cls):
        return template_in_img(template_path.AREA_NAVIGATION, game.get_screenshot())

    @classmethod
    def in_ball_navigation(cls):
        return template_in_img(template_path.BALL_NAVIGATION, game.get_screenshot())

    def into_map(self):
        game.to_game_main()
        pyautogui.press(cfg.get(cfg.open_map))
        wait_img(template_path.AREA_NAVIGATION)

    def into_ball(self, world_name):
        if not self.in_ball_navigation():
            self.into_map()
        pos = get_text_position(window.get_screenshot(), "星轨航图")
        mouse.click_positions(pos)
        wait_img(template_path.BALL_NAVIGATION)
        pos = get_text_position(window.get_screenshot(), world_name)
        mouse.click_positions(pos, direction="topLeft", val=100)
        wait_img(template_path.AREA_NAVIGATION)

    def into_area(self, area_name):
        if not self.in_area_navigation():
            self.into_map()
        car_pos = get_text_position(window.get_screenshot(), "观景车厢")
        if car_pos.size != 0:
            mouse.click_positions(car_pos)
        while True:
            pos = get_text_position(window.get_screenshot(), area_name)
            if pos.size == 0:
                mouse.mouse_scroll(2)
                continue
            mouse.click_positions(pos)
            break

    def into_point(self, point_img):
        """
        地图缩放至最小
        鼠标移动至游戏界面的 (800, 600)
        查找不到坐标则尝试上下左右拉扯查找传送点
        """
        if not self.in_area_navigation():
            self.into_map()
        x1, y1, _, _ = game.get_rect()
        map_center = (x1 + 800, y1 + 600)
        mouse.click_position(map_center)
        mouse.mouse_scroll(3)
        move = 400
        h, w = point_img.shape[:2]

        def click_point_and_send(p):
            mouse.click_position((p[0] + w // 2, p[1] + h // 2))
            time.sleep(0.2)
            send_p = get_text_position(window.get_screenshot(), "传送")
            mouse.click_positions(send_p)

        # 不移动查找
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向上查找1
        mouse.down_move(map_center, (map_center[0], map_center[1] - move))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向上查找2
        mouse.down_move(map_center, (map_center[0], map_center[1] - move))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

        # 重新初始化地图
        self.into_map()
        # 向下查找1
        mouse.down_move(map_center, (map_center[0], map_center[1] + move))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向下查找2
        mouse.down_move(map_center, (map_center[0], map_center[1] + move))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

        # 重新初始化地图
        self.into_map()
        # 向左查找1
        mouse.down_move(map_center, (map_center[0] - move, map_center[1]))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向左查找2
        mouse.down_move(map_center, (map_center[0] - move, map_center[1]))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

        # 重新初始化地图
        self.into_map()
        # 向右查找1
        mouse.down_move(map_center, (map_center[0] + move, map_center[1]))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向右查找2
        mouse.down_move(map_center, (map_center[0] + move, map_center[1]))
        pos = match_template(point_img, window.get_screenshot())
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

    def get_local_map(self) -> ndarray:
        """get top left map"""
        local = game.get_screenshot()
        local = local[131:131 + 128, 88: 88 + 128]
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

    def get_match_pos(self):
        local_map = self.get_local_map()
        local_map = self.only_arrow(local_map, nt=True)
        # 角色移动时小地图被缩小，需要将小地图放大再匹配
        if self.role_state.is_moving:
            local_map = cv2.resize(local_map, (0, 0), fx=1.256, fy=1.256)
            self.local_map = local_map
        h, w = local_map.shape[:2]

        # 灰度图
        local_map_gray = cv2.cvtColor(local_map, cv2.COLOR_BGR2GRAY)
        big_map_gray = cv2.cvtColor(self.big_map, cv2.COLOR_BGR2GRAY)

        # 二值化
        _, local_map_binary = cv2.threshold(local_map_gray, 165, 255, cv2.THRESH_BINARY)
        _, big_map_binary = cv2.threshold(big_map_gray, 210, 255, cv2.THRESH_BINARY)

        # 膨胀
        kernel = np.ones((2, 2), np.uint8)
        big_binary = cv2.dilate(big_map_binary, kernel, iterations=1)
        local_map_binary = cv2.dilate(local_map_binary, kernel, iterations=1)

        res = cv2.matchTemplate(big_binary, local_map_binary, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)

        # 阈值达不到递归查询
        if max_val < 0.5:
            log.debug(f"当前阈值: {max_val}, 阈值未达0.5开始递归查询")
            time.sleep(0.5)
            return self.get_match_pos()

        return w, h, max_loc

    def locate_role_pos(self) -> Tuple[int, int]:
        """get current role position on big map"""
        w, h, top_left = self.get_match_pos()

        pos = (top_left[0] + w // 2, top_left[1] + h // 2)
        self.last_pos = self.cur_pos
        self.cur_pos = pos

        return pos

    def load_maps(self):
        """load maps"""
        get_img = os.path.join
        log.info("加载地图")
        self.big_map = cv2.imread(get_img(self.map_path, "default.png"))
        self.big_map_binary = cv2.imread(get_img(self.map_path, "binary.png"))
        self.big_map_target = cv2.imread(get_img(self.map_path, "target.png"))
        self.point_img = cv2.imread(get_img(self.map_path, "point.png"))
        log.info("地图加载完成")

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
        return arrow

    def set_big_map(self, path: str):
        """set big map"""
        self.big_map = cv2.imread(path)

    def set_map_path(self, path: str):
        """set map path"""
        self.map_path = path
        self.set_big_map(os.path.join(path, "default.png"))


if __name__ == "__main__":
    utils = WorldUtils()
    utils.into_point(cv2.imread(r"F:\AutoStarRail\script\world\map\2\1\1\point.png"))
