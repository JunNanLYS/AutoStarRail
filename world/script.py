import os
import time
from math import atan, sqrt
from typing import Tuple, Optional
from copy import deepcopy

import pyautogui
import numpy as np
import cv2

import config
from widgets import log
from utils.role import Role, MoveDirection, Direction
from utils import window, path, func
from world import road, map

stop = False

img_filename = path.ImagePath


def to_map():
    """进入地图"""
    if not func.to_game_main():
        return False
    pyautogui.press('m')
    time.sleep(1.5)
    return True


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
        return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def update_road(self):
        pass

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

    def set_world_number(self, world_number: int):
        self.world_number = world_number

    def set_map_name(self, map_name: str):
        self.map_name = map_name


class World:
    def __init__(self):
        pass

    def is_fight(self):
        """
        判断是否正在战斗
        """
        pass

    def fight(self):
        """
        战斗攻击..
        """
        pass


# 初始化星球以及地区
WORLD = 3  # 星球
WORLD_TO_MAP_NAME = {
    1: [],
    2: ['1-1'],
    3: [],
}


def main():
    for world_number in range(1, WORLD + 1):
        for map_name in WORLD_TO_MAP_NAME[world_number]:
            # 初始化
            m = Map()
            m.set_world_number(world_number)
            m.set_map_name(map_name)
            m.road = road.get_road(m.get_road_map_img())
            m.shot_map()  # 更新大地图截图
            role_pos = m.locate_role(m.cur_map)  # 定位角色坐标并更新big_map
            log.transmitDebugLog(f"角色坐标:{role_pos}", level=2)
            role_angle = Role.get_angle(m.big_map)  # 获取角色当前角度
            target_angle = calculate_angle(role_pos, m.road[0])
            log.transmitDebugLog(f"需要设置角色角度为:{target_angle}", level=2)
            func.to_game_main()
            Role.set_angle(role_angle, target_angle)  # 设置角度

            # 将角色移动到起点
            start_pos = m.road[0]
            length = m.calculate_length(role_pos, start_pos)  # 两点距离
            length = int(round(length, 0))  # 转int
            Role.move_position(MoveDirection.ONWARD, length)
            # 到此为止初始化结束，开始正常路线模式

            i = 1  # 下标0是起点，正常情况下是已经移动到起点了
            roads: list[tuple] = []  # tuple有3元素,存储点1,点2,点1到点2的角度
            start = m.road[0]  # 起点
            end = m.road[1]  # 终点
            pre_angle = calculate_angle(start, end)  # 上一个角度
            added = False
            while i < len(m.road):
                added = False
                angle = calculate_angle(start, m.road[i])
                if pre_angle == angle:
                    end = m.road[i]
                    i += 1
                else:
                    added = True
                    roads.append((start, end, pre_angle))  # 同一角度路线
                    start = end
                    end = m.road[i]
                    pre_angle = calculate_angle(start, end)
                    i += 1
            # 若直到循环结束角度依旧一样则需要在这添加
            if not added:
                roads.append((start, end, pre_angle))
            for pos1, pos2, angle in roads:
                Role.set_angle(Role.angle, angle)
                length = m.calculate_length(pos1, pos2)
                length = int(round(length, 0))
                Role.move_position(MoveDirection.ONWARD, length)
                time.sleep(0.5)


if __name__ == "__main__":
    main()
