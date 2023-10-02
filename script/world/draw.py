import os.path
import time
from copy import deepcopy

import cv2
import numpy as np
from pynput import keyboard

from script.utils import template_path, where_img
from script.utils.interface import WorldUtils


class Image:
    def __init__(self, path):
        self.path = path
        self.default = cv2.imread(os.path.join(path, "default.png"))

    @property
    def binary(self):
        return cv2.imread(os.path.join(self.path, 'binary.png'))

    def save_binary(self, img):
        cv2.imwrite(os.path.join(self.path, 'binary.png'), img)

    def save_line(self, img):
        cv2.imwrite(os.path.join(self.path, 'line.png'), img)

    def save_target(self, img):
        cv2.imwrite(os.path.join(self.path, 'target.png'), img)

    def reload(self):
        self.default = cv2.imread(os.path.join(self.path, "default.png"))


class DrawMap(WorldUtils):
    def __init__(self, m: Image):
        super().__init__()
        self._stop = False
        self._pause = False

        self.draw_listener = keyboard.Listener()
        self.draw_listener.on_press = self._on_press
        self.img = m

    def draw(self):
        black = np.array([0, 0, 0])
        gray = np.array([55, 55, 55])
        white = np.array([210, 210, 210])
        find = 1
        big_map = self.img.default
        bw_map = np.zeros(big_map.shape[:2], dtype=np.uint8)
        # 灰块、白线：小地图中的可移动区域、可移动区域的边缘
        # b_map：当前像素点是否是灰块。只允许灰块附近（2像素）的像素被识别为白线
        b_map = deepcopy(bw_map)
        b_map[
            np.sum((big_map - gray) ** 2, axis=-1) <= 3200 + find * 1600
            ] = 255
        kernel = np.zeros((5, 5), np.uint8)  # 设置kenenel大小
        kernel += 1
        b_map = cv2.dilate(b_map, kernel, iterations=1)
        bw_map[
            (np.sum((big_map - white) ** 2, axis=-1) <= 3200 + find * 1600)
            & (b_map > 200)
            ] = 255
        # 创建一个和arr形状相同的布尔数组，其中arr中的0被标记为True，255被标记为False
        mask = b_map == 0

        # 使用布尔索引将arr中的0替换为255，255替换为0
        b_map[mask] = 255
        b_map[~mask] = 0

        # 查找传送点将其所在位置设置为黑
        upper = np.array([0, 0, 228])
        lower = np.array([0, 0, 137])
        m = deepcopy(self.img.default)
        hsv = cv2.cvtColor(m, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, lower, upper)
        m[np.where(mask != 0)] = [57, 57, 57]
        send_paths = [template_path.SEND1, template_path.SEND2, template_path.SEND3, template_path.SEND4]
        for send_path in send_paths:
            send = where_img(m, send_path, threshold=0.68)
            positions = send
            for top_left in positions:
                width = 40
                bottom_right = (top_left[0] + width, top_left[1] + width)
                b_map[top_left[1]:bottom_right[1], top_left[0]:bottom_right[0]] = 0
        self.img.save_line(bw_map)
        self.img.save_binary(b_map)  # 保存黑白图

        target = self.img.binary

        while not self._stop:
            if self._pause:
                time.sleep(0.3)
                continue
            w, h, top_left = self.get_match_pos(big_map)
            x1, y1 = top_left[0], top_left[1]
            x2, y2 = x1 + w, y1 + h
            changed = deepcopy(target[y1: y2, x1: x2])

            # 找小地图上的怪点
            lower = np.array([46, 46, 214])
            upper = np.array([120, 110, 233])
            mask = cv2.inRange(self.local_map, lower, upper)

            changed[mask > 0] = [46, 46, 214]
            # 创建一个新的mask，将changed中不为白色的部分设置为True
            not_white = np.all(changed != [255, 255, 255], axis=-1)
            # 使用numpy的逻辑与运算符找到同时满足两个条件的像素
            mask_black = np.logical_and(mask == 0, not_white)
            # 将这些像素设置为黑色
            changed[mask_black] = [0, 0, 0]
            target[y1: y2, x1: x2] = changed

            cv2.imshow("big map", changed)
            cv2.moveWindow("big map", 0, 0)
            cv2.waitKey(100)

        self.img.save_target(target)  # 保存怪点

    def start(self):
        self.draw_listener.start()
        self.draw()

    def stop(self):
        self._stop = True
        self.draw_listener.stop()

    def pause(self):
        self._pause = not self._pause
        if self._pause:
            print("已暂停")

    def _on_press(self, key):
        try:
            if key == keyboard.Key.f8:
                self.stop()
            elif key == keyboard.Key.f7:
                self.pause()
        except AttributeError:
            pass
        except Exception:
            pass


if __name__ == '__main__':
    my_map = Image(r"F:\AutoStarRail\script\world\map\2\2\2")  # 修改地图路径则可以绘制地图
    draw = DrawMap(my_map)
    draw.start()
