import os.path
from copy import deepcopy

import cv2
import numpy as np
from pynput import keyboard

from script.utils.interface import WorldUtils


class DrawMap(WorldUtils):
    def __init__(self):
        super().__init__()
        self._stop = False

        self.draw_listener = keyboard.Listener()
        self.draw_listener.on_press = self._on_press

    def draw(self):
        self.set_big_map(os.path.join(self.map_path, "default.png"))  # 设置原图
        gray = cv2.cvtColor(self.big_map, cv2.COLOR_BGR2GRAY)
        _, binary = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)  # 大地图二值化
        kernel = np.ones((2, 2), np.uint8)
        binary = cv2.dilate(binary, kernel, iterations=1)
        cv2.imwrite(os.path.join(self.map_path, "binary.png"), binary)  # 保存
        binary = cv2.cvtColor(binary, cv2.COLOR_GRAY2BGR)

        while not self._stop:
            w, h, top_left = self.get_match_pos()
            x1, y1 = top_left[0], top_left[1]
            x2, y2 = x1 + w, y1 + h
            changed = deepcopy(binary[y1: y2, x1: x2])

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
            cv2.cvtColor(changed, cv2.COLOR_BGR2GRAY)
            binary[y1: y2, x1: x2] = changed

            cv2.imshow("big map", changed)
            cv2.moveWindow("big map", 0, 0)
            cv2.waitKey(100)

        cv2.imwrite(os.path.join(self.map_path, "target.png"), binary)  # 保存怪点

    def start(self):
        self.draw_listener.start()
        self.draw()

    def stop(self):
        self._stop = True
        self.draw_listener.stop()

    def _on_press(self, key):
        try:
            if key == keyboard.Key.f8:
                self.stop()
        except AttributeError:
            pass
        except Exception:
            pass


if __name__ == '__main__':
    draw = DrawMap()
    draw.set_map_path(r"F:\AutoStarRail\script\world\map\2\2\1")
    draw.start()
