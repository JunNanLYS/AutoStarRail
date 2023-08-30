import os
import time
from math import atan, sqrt
from threading import Thread
from typing import Tuple
from copy import deepcopy

import pyautogui
import numpy as np
import cv2
import win32api
import win32con

import config
import threadpool
from config import config as cfg
from widgets import log
from utils.role import Role, MoveDirection
from utils import window, path, func, ocr
from world import road, fight
from world.data import BALL_NAME, AREA_NAME, AREA_POINT, AREA_SCROLL

img_filename = path.ImagePath


def to_map():
    """进入地图"""
    if not func.to_game_main():
        return False
    pyautogui.press(cfg.open_map)
    time.sleep(1.5)
    return True


def mouse_scroll(count: int):
    """
    鼠标滚轮
    """
    for _ in range(count):
        for _ in range(6):
            pyautogui.scroll(-10)


def rotate_search_img(img, template, add_angle: int, thresholds: float):
    """
    :param img: cv图像
    :param template: 要查找的模板图
    :param add_angle: 每次旋转的角度
    :param thresholds: 遇到该阈值直接返回
    """
    angle = 0
    val, loc = 0, (0, 0)
    h, w = template.shape[:2]
    while val < thresholds and angle < 365:
        matrix = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)  # 获取旋转矩阵
        rotated_arrow = cv2.warpAffine(template, matrix, (w, h))  # 获取旋转后的图像
        res = cv2.matchTemplate(img, rotated_arrow, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc1 = cv2.minMaxLoc(res)

        # 找到更大相似度，更新val和loc
        if max_val > val:
            val = max_val
            loc = max_loc1

        log.transmitDebugLog(f"val={val}, loc={loc}, angle={angle}")
        angle += add_angle

    return val, loc


def calculate_angle(pos1: Tuple[int, int], pos2: Tuple[int, int]) -> int:
    """
    计算坐标点与在角色哪个方向, 0度为正y轴，90度为负x轴
    :param pos1: 角色坐标
    :param pos2: 目的地坐标
    :return:
    """
    x, y = pos2[0] - pos1[0], -(pos2[1] - pos1[1])
    if y == 0:
        # 正x轴
        if x > 0:
            return 270
        # 原点
        elif x == 0:
            return 0
        # 负x轴
        else:
            return 90
    elif x == 0:
        if y > 0 or y == 0:
            return 0
        else:
            return 180
    angle = int(abs(atan(y / x)) * (180 / 3.1415926535))
    if x > 0:
        # 第一象限
        if y > 0:
            angle += 270
        # 第四象限
        else:
            angle = 180 + (90 - angle)
    # x < 0
    else:
        # 第二象限
        if y > 0:
            angle = 90 - angle
        # 第三象限
        else:
            angle += 90
    return angle


def align_angle():
    """
    校准鼠标误差，在不同DPI，分辨率，缩放下误差不相同。
    移动角色60度，根据实际移动了几度计算出误差比。
    参考自Github项目Auto_Simulated_Universe。
    """
    from config import config as cfg
    def f():
        time.sleep(0.5)
        pyautogui.press('ctrl')
        time.sleep(0.1)
        pyautogui.press('w')
        pyautogui.press('ctrl')
        time.sleep(0.5)

    m = Map()
    m.capture_minimap()
    cfg.angle = 1.0  # 调整为默认值
    # 初始化角色当前角度
    init_angle = Role.get_angle(m.minimap)
    log.transmitDebugLog(f"初始角度={init_angle}", level=2)
    last_angle = init_angle
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, 0, 3000)  # 将视角向下拉
    for i in [1, 1, 3]:
        angle_list = []
        for j in range(i):
            Role.move_view(60)
            f()
            m.capture_minimap()
            now_angle = Role.get_angle(m.minimap)
            sub = last_angle - now_angle  # 计算实际移动角度与应该移动角度误差
            while sub < 0:
                sub += 360
            angle_list.append(sub)
            last_angle = now_angle
        angle_list = np.array(angle_list)
        log.transmitDebugLog(f"angle_list={angle_list}", level=2)
        ax, ay = 0, 0
        for j in angle_list:
            if abs(j - np.median(angle_list)) <= 5:
                ax += 60
                ay += j
        cfg.angle *= ax / ay
        log.transmitDebugLog(f"ax={ax}, ay={ay}")
    log.transmitDebugLog(f"计算得出误差={cfg.angle}")
    cfg.dump()


class Map:
    def __init__(self):
        self.road = []  # 要走的路像素点
        self.map_name = "1-1"  # 地图名称
        self.world_number = 1  # 大地图
        self.cur_map = None  # 当前地图
        self.minimap = None  # 小地图
        self.big_map = None  # 大地图
        self.player_position = (0, 0)  # 玩家坐标

    def capture_minimap(self):
        """截取小地图"""
        func.to_game_main()
        map_size = 160  # 要截取的小地图的宽度
        # 读取模板图
        template_phone = cv2.imread(img_filename.PHONE)
        phone_h, phone_w = template_phone.shape[:2]
        # 灰度图
        template_phone = cv2.cvtColor(template_phone, cv2.COLOR_BGR2GRAY)
        # 获取游戏截图
        game_img = cv2.imread(window.save_game_screenshot())
        game_img_gray = cv2.cvtColor(game_img, cv2.COLOR_BGR2GRAY)  # 游戏截图的灰度图
        # 匹配
        phone_res = cv2.matchTemplate(game_img_gray, template_phone, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(phone_res)

        x1 = max_loc[0] + phone_w
        y1 = max_loc[1] + (phone_h // 2)

        # 读取任务模板图(流程与上面一样)
        template_mandate = cv2.imread(img_filename.MANDATE)
        mandate_h, mandate_w = template_mandate.shape[:2]
        template_mandate = cv2.cvtColor(template_mandate, cv2.COLOR_BGR2GRAY)
        mandate_res = cv2.matchTemplate(game_img_gray, template_mandate, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(mandate_res)

        x2 = max_loc[0] + mandate_w + map_size
        y2 = max_loc[1] + (mandate_h // 2)

        game_img = game_img[y1:y2, x1:x2]  # 截取小地图部分
        write_path = os.path.join(config.abspath, "temp", "minimap.png")
        cv2.imwrite(write_path, game_img)
        self.minimap = game_img
        return write_path

    def capture_atlas(self, radius: int = 80):
        """截取大地图中玩家坐标为中心辐射radius截图"""
        if not to_map():
            log.transmitDebugLog("没有进入地图", level=4)
            raise Exception("没有进入地图")
        img = deepcopy(self.shot_map())  # 获取地图并拷贝
        center = self.locate_role(img)  # 获取角色中心点
        capture_p1 = (center[0] - radius, center[1] - radius)
        capture_p2 = (center[0] + radius, center[1] + radius)

        self.big_map = img[capture_p1[1]:capture_p2[1], capture_p1[0]:capture_p2[0]]
        return self.big_map

    def locate_role(self, img, radius=50):
        """
        给一张图，定位角色位置的同时截取角色为中心范围为radius的截图
        :return: 角色矩形中心点
        """
        # 排除一些干扰因素
        lower_blue = np.array([234, 191, 4])  # 蓝色下限
        upper_blue = np.array([255, 209, 73])  # 上限
        img2 = deepcopy(img)
        img2[np.sum(img2 - lower_blue, axis=-1) < 0] = [0, 0, 0]
        img2[np.sum(img2 - upper_blue, axis=-1) > 0] = [0, 0, 0]

        thresholds = 0.65  # 阈值
        arrow = cv2.imread(img_filename.ARROW)
        h, w = arrow.shape[:2]

        # 先查找特殊角度
        val, loc = rotate_search_img(img2, arrow, 45, thresholds)

        # 未满足阈值，开启全角度搜索
        if val < thresholds:
            log.transmitDebugLog("开启全角度搜索")
            new_val, new_loc = rotate_search_img(img2, arrow, 2, thresholds)
            if new_val > val:
                val = new_val
                loc = new_loc

        top_left = loc
        center = (top_left[0] + w // 2, top_left[1] + h // 2)
        capture_p1 = (center[0] - radius, center[1] - radius)
        capture_p2 = (center[0] + radius, center[1] + radius)
        self.player_position = center
        self.big_map = img[capture_p1[1]:capture_p2[1], capture_p1[0]:capture_p2[0]]
        return center

    @classmethod
    def calculate_length(cls, pos1: Tuple[int, int], pos2: Tuple[int, int]):
        """
        计算两点距离
        :param pos1:
        :param pos2:
        :return:
        """
        x1, y1 = pos1
        x2, y2 = pos2
        return sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))

    def update_road(self):
        self.road = road.get_road(self.get_road_map_img())

    def shot_map(self):
        """获取当前地图截图更新cur_map"""
        if not to_map():
            log.transmitDebugLog("没有进入地图", level=4)
            raise Exception("没有进入地图")
        img = cv2.imread(window.save_game_screenshot())
        img = img[:1000, :1400]
        self.cur_map = img
        return self.cur_map

    def get_big_map_img(self, read_all=False):
        """
        :read_all: 设置为True读取原图，灰度图，二值图
        :return: cv2.img
        """
        root = config.abspath
        filename = os.path.join(
            root,
            r"world\map",
            str(self.world_number),
            self.map_name
        )
        img = cv2.imread(os.path.join(filename, 'default.png'))
        if read_all:
            # 读取全部
            gray = cv2.imread(os.path.join(filename, 'gray.png'))
            binary = cv2.imread(os.path.join(filename, 'binary.png'))
            return img, gray, binary
        else:
            return img

    def get_road_map_img(self):
        """
        :return: 路线图的cv2.img
        """
        root = config.abspath
        filename = os.path.join(
            root,
            r"world\map",
            str(self.world_number),
            self.map_name
        )
        img = cv2.imread(os.path.join(filename, 'road.png'))
        return img

    def get_send_point_img(self):
        """
        获取地区传送点图像
        """
        root = config.abspath
        filename = os.path.join(
            root,
            r"world\map",
            str(self.world_number),
            self.map_name
        )
        img = cv2.imread(os.path.join(filename, 'point.png'))
        return img

    def set_world_number(self, world_number: int):
        self.world_number = world_number

    def set_map_name(self, map_name: str):
        self.map_name = map_name


class World:
    def __init__(self):
        self.is_stop = False
        self.is_close = False
        self.map = Map()
        self.cur_ball: int = 1  # 当前星球
        self.cur_area: int = 1  # 当前区域
        self.cur_point: int = 1  # 传送点

        self.pre_ball_name = ""
        self.pre_area_name = ""
        self.flag = False

    def auto(self, ball_name, area_name):
        # 不是同一个星球需要更换星球和区域
        if ball_name != self.pre_ball_name:
            self.change_ball(ball_name)
            self.change_area(area_name)
            self.into_send_point()
        # 只有区域不同只需要更换当前区域
        elif area_name != self.pre_area_name:
            to_map()
            self.change_area(area_name)
            self.into_send_point()
        self.pre_ball_name = ball_name
        self.pre_area_name = area_name
        if self.is_close:
            return

        # 开始初始化
        self.map.update_road()  # 更新路线图
        self.map.shot_map()  # 截取游戏大地图
        role_pos = self.map.locate_role(self.map.cur_map)  # 定位角色坐标
        role_angle = Role.get_angle(self.map.big_map)  # 获取角色当前角度
        target_angle = calculate_angle(role_pos, self.map.road[0])
        func.to_game_main()  # 回到游戏主界面
        Role.set_angle(role_angle, target_angle)  # 设置角色角度
        start_pos = self.map.road[0]
        length = self.map.calculate_length(role_pos, start_pos)  # 两点距离
        length = int(round(length, 0))  # 转int
        Role.move_position(MoveDirection.ONWARD, length)
        # 到此为止初始化结束，开始添加路线

        i = 1  # 下标0是起点，正常情况下已经移动到起点了
        roads: list[tuple] = []  # (p1, p2, angle) 存储路线
        start = self.map.road[0]
        end = self.map.road[1]
        pre_angle = calculate_angle(start, end)
        added = False
        while i < len(self.map.road):
            added = False
            angle = calculate_angle(start, self.map.road[i])
            if pre_angle == angle:
                end = self.map.road[i]
                i += 1
            else:
                added = True
                roads.append((start, end, pre_angle))
                start = end
                end = self.map.road[i]
                pre_angle = calculate_angle(start, end)
                i += 1
        # 直到循环结束角度依旧一样则需要在这添加一次
        if not added:
            roads.append((start, end, pre_angle))

        i = 0
        while i < len(roads):
            if self.is_close:
                return
            pos1, pos2, angle = roads[i]
            if self.flag:
                self.flag = False
                self.map.shot_map()  # 截取大地图
                self.map.locate_role(self.map.cur_map)  # 更新big_map
                img = self.map.get_big_map_img()
                template = self.map.big_map
                res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
                _, max_val, _, max_loc = cv2.minMaxLoc(res)
                role_pos = max_loc[0] + template.shape[1] // 2, max_loc[1] + template.shape[0] // 2
                role_angle = Role.get_angle(self.map.big_map)
                target_angle = calculate_angle(role_pos, pos2)
                func.to_game_main()  # 回到主界面
                Role.set_angle(role_angle, target_angle)
                thread = threadpool.function_thread.submit(Role.move_position, MoveDirection.ONWARD, length)
                # thread = Thread(target=Role.move_position, args=(MoveDirection.ONWARD, length))
                # thread.start()
            else:
                length = self.map.calculate_length(pos1, pos2)
                Role.set_angle(Role.angle, angle)
                thread = threadpool.function_thread.submit(Role.move_position, MoveDirection.ONWARD, length)
                # thread = Thread(target=Role.move_position, args=(MoveDirection.ONWARD, length))
                # thread.start()  # 移动角色将阻塞线程，所以使用子线程

            # 等待线程结束
            while not thread.done():
                time.sleep(1)
            # 若is_stop被设置为True则等待被设置为False
            while self.is_stop:
                time.sleep(1)
            if not self.flag:
                i += 1

    def change_ball(self, ball_name):
        """
        打开星球
        """
        self.to_star_rail_map()
        screenshot_path = func.screenshot()
        pos = ocr.get_text_position(screenshot_path, ball_name)
        add = np.array([-50, -80])
        pos = pos + add  # 由于星球在字体上方，所以需要坐标需要微调
        self.click_pos(pos)
        self.wait_img(img_filename.AREA_NAVIGATION)

    def change_area(self, area_name):
        cnt = AREA_SCROLL.get(area_name, 0)
        if cnt:
            # 将鼠标移动至观景车厢
            log.transmitDebugLog(f"{area_name}需要滚动后查找", level=2)
            pos = ocr.get_text_position(func.screenshot(), "观景车厢")
            pyautogui.moveTo(pos[0][0], pos[0][1])
            mouse_scroll(cnt)  # 滚动
        positions = ocr.get_text_position(func.screenshot(), area_name)
        self.click_pos(positions)
        time.sleep(0.5)

    def click_pos(self, positions):
        """
        传入单个值则点击该值，多个值则取索引为 元素个数/2 的坐标
        :param positions: numpy.array,二维数组[[], []]
        """
        length = len(positions)
        mid = length // 2 - 1
        if mid < 0:
            mid = 0
        pos = positions[mid]
        x, y = int(pos[0]), int(pos[1])
        win32api.SetCursorPos((x, y))
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
        time.sleep(0.1)  # 过快的点击将导致游戏反应不过来最终导致点击失效
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

    def close(self):
        """
        关闭自动寻路
        """
        self.is_close = True
        fight.close()  # 关闭战斗模块

    def into_send_point(self):
        template = self.map.get_send_point_img()
        max_val = 0
        top_left = (0, 0)
        for i in range(5):
            img = cv2.imread(func.screenshot())
            res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            top_left = max_loc
            if max_val >= 0.8:
                break
        if max_val < 0.8:
            log.transmitDebugLog(f"匹配值低于0.8,当前匹配值:{max_val},脚本退出.", level=3)
            raise Exception("匹配不到传送点")
        center = (top_left[0] + template.shape[1] // 2, top_left[1] + template.shape[0] // 2)
        pyautogui.click(*center)  # 点击传送点

        positions = ocr.get_text_position(func.screenshot(), "传送")
        self.click_pos(positions)

    @property
    def map_name(self):
        return f"{self.cur_area}-{self.cur_point}"

    def re_back(self):
        """
        当前地图重走一遍
        """
        self.auto(self.pre_ball_name, self.pre_area_name)

    def start(self):
        """
        开始运行自动寻路
        """
        self.is_stop = False
        self.is_close = False
        fight.start()
        fight.set_callable(self.set_stop)
        for ball_number, ball_name in BALL_NAME.items():
            area_names = AREA_NAME[ball_number]  # 地区名
            for i, area_name in enumerate(area_names):
                points = AREA_POINT.get(area_name, 0)
                for point in (1, points + 1):
                    if self.is_close:
                        return
                    # 初始化
                    self.cur_ball = ball_number
                    self.cur_area = i + 1
                    self.cur_point = point
                    self.map.set_world_number(self.cur_ball)
                    self.map.set_map_name(self.map_name)

                    self.auto(ball_name, area_name)
        fight.close()  # 自动寻路结束关闭战斗模块

    def set_stop(self, stop: bool):
        if stop:
            self.is_stop = stop
            self.flag = True  # 标记一下
            Role.stop_move()
        else:
            self.is_stop = stop

    def to_star_rail_map(self):
        """
        进入星轨航图
        """
        if not to_map():
            log.transmitDebugLog("进入地图失败", level=4)
            raise Exception("进入地图失败")
        screenshot_path = func.screenshot()
        pos = ocr.get_text_position(screenshot_path, "星轨航图")
        self.click_pos(pos)
        self.wait_img(img_filename.BALL_NAVIGATION)

    def wait_img(self, template: str):
        log.transmitDebugLog(f"等待图片{template}")
        template = cv2.imread(template)
        star = time.time()
        end = 20
        while time.time() - star <= end:
            screenshot = cv2.imread(window.save_game_screenshot())
            res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.8:
                return max_loc
        log.transmitRunLog("等待超时，开启兜底")
        screenshot = cv2.imread(window.save_game_screenshot())
        res = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
        _, max_val, _, max_loc = cv2.minMaxLoc(res)
        if max_val > 0.8:
            return max_loc
        log.transmitDebugLog("等待不到图片，程序退出", level=3)
        raise Exception("等待不到图片")


if __name__ == "__main__":
    w = World()
    w.map.set_world_number(2)
    w.map.set_map_name("1-1")
    fight.start()
    w.auto("雅利洛", "城郊雪原")
