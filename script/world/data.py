import time
from typing import Dict, List, Optional

import cv2
import numpy as np
from numpy import ndarray

from script.utils import (mouse, wait_img, template_path, get_text_position, window, template_in_img, match_template)

# key星球编号 value星球名称
BALL_NAME: Dict[int, str] = {
    1: "空间站",
    2: "雅利洛",
    3: "仙舟",
}
# key为星球编号 value为该星球中所有含有怪物的区域名
AREA_NAME: Dict[int, List[str]] = {
    1: ["基座舱段", "收容舱段", "支援舱段"],
    2: ["城郊雪原", "边缘通路", "残响回廊", "永冬岭", "大矿区", "铆钉镇", "机械聚落"],
    3: ["流云渡", "迴星港", "太卜司", "工造司", "丹鼎司", "鳞渊境"],
}
# key为地区名 value是该地区传送点个数
# 例如 {"城郊雪原": 2} 意思是有 1-1 和 1-2 如果加上前面的星球就是 1-1-1 ~ 1-1-2
#                    第一个1是地区编号(在下标0处)
#                    第二个1是传送点1
AREA_POINT: Dict[str, int] = {
    "主控舱段": 1,
    "城郊雪原": 2,
}


class Map:
    def __init__(self, map_path):
        from collections import deque
        self.map_path = map_path

        self.last_ball = ""
        self.last_area = ""

        self.cur_ball = ""
        self.cur_area = ""

        self.data = deque()
        self.reload_cnt = 0

        # current map image
        self.default: Optional[ndarray] = None
        self.binary: Optional[ndarray] = None
        self.line: Optional[ndarray] = None
        self.target: Optional[ndarray] = None
        self.point: Optional[ndarray] = None
        self.spare_point: Optional[ndarray] = None
        self.select: Optional[ndarray] = None

        self.load()

    @classmethod
    def change_ball(cls, ball: str):
        import game
        pos = get_text_position(game.get_screenshot(), "星轨航图")
        mouse.click_positions(pos, game_pos=True)
        wait_img(template_path.BALL_NAVIGATION)
        pos = get_text_position(game.get_screenshot(), ball)
        mouse.click_positions(pos, direction="topLeft", val=100, game_pos=True)
        wait_img(template_path.AREA_NAVIGATION)

    @classmethod
    def change_area(cls, area: str):
        import game
        # (1470 300) 这个地图第一个区域的位置
        x1, y1, _, _ = game.get_rect()
        mouse.click_position((x1 + 1470, y1 + 300))
        while True:
            pos = get_text_position(game.get_screenshot(), area)
            if pos.size == 0:
                mouse.mouse_scroll(2)
                continue
            mouse.click_positions(pos, game_pos=True)
            time.sleep(0.2)
            break

    def change_point(self, p_img: ndarray):
        import game
        x1, y1, _, _ = game.get_rect()
        map_center = (x1 + 800, y1 + 600)
        mouse.click_position(map_center)
        move = 400
        h, w = p_img.shape[:2]

        def click_point_and_send(p):
            mouse.click_position((p[0] + w // 2, p[1] + h // 2))
            time.sleep(0.5)
            # 部分传送点点击后会出现菜单让你再次确定
            if self.select is not None:
                select_p = match_template(game.get_screenshot(), self.select)
                mouse.click_position(select_p, game_pos=True)
            wait_img(template_path.SEND_TEXT)
            send_p = match_template(game.get_screenshot(), template_path.SEND_TEXT)
            mouse.click_position(send_p, game_pos=True)
            wait_img(template_path.MANDATE, mode='gray')
            time.sleep(2)

        # 不移动查找
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向上查找1
        mouse.down_move(map_center, (map_center[0], map_center[1] - move))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向上查找2
        mouse.down_move(map_center, (map_center[0], map_center[1] - move))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

        # 向下查找1
        mouse.down_move(map_center, (map_center[0], map_center[1] + move))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向下查找2
        mouse.down_move(map_center, (map_center[0], map_center[1] + move))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

        # 向左查找1
        mouse.down_move(map_center, (map_center[0] - move, map_center[1]))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向左查找2
        mouse.down_move(map_center, (map_center[0] - move, map_center[1]))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

        # 向右查找1
        mouse.down_move(map_center, (map_center[0] + move, map_center[1]))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return
        # 向右查找2
        mouse.down_move(map_center, (map_center[0] + move, map_center[1]))
        pos = match_template(window.get_screenshot(), p_img)
        if pos != (-1, -1):
            click_point_and_send(pos)
            return

    @classmethod
    def open_game_map(cls):
        import pyautogui
        import game
        from config import cfg
        game.to_game_main()
        pyautogui.press(cfg.get(cfg.open_map))
        wait_img(template_path.AREA_NAVIGATION)
        mouse.mouse_scroll(3)  # 地图缩放至最小

    def reload_current_map(self):
        """重新进入当前地图"""
        self.reload_cnt += 1
        self.open_game_map()
        self.change_point(self.point)


    def load(self):
        """load my game map images"""
        import os
        from collections import deque
        self.data = deque()
        balls = os.listdir(self.map_path)
        for ball_str in balls:
            areas = os.listdir(os.path.join(self.map_path, ball_str))
            ball_int = int(ball_str)
            for area_str in areas:
                points = os.listdir(os.path.join(self.map_path, ball_str, area_str))
                area_int = int(area_str)
                area_name = AREA_NAME[ball_int][area_int - 1]
                ball_name = BALL_NAME[ball_int]
                for point_str in points:
                    path = os.path.join(self.map_path, ball_str, area_str, point_str)
                    self.data.appendleft((ball_name, area_name, path))

    def next(self) -> bool:
        """进入下一场地图"""
        import os
        import log
        # 已经锄完了
        if not self.data:
            log.info("没有待锄地图")
            return False
        ball_name, area_name, img_path = self.data.pop()
        log.info(f"星球：{ball_name}，地区：{area_name}，传送点：{img_path[-1]}")
        # 加载地图图片
        get_path = os.path.join
        self.default = cv2.imread(get_path(img_path, 'default.png'))
        self.binary = cv2.imread(get_path(img_path, 'binary.png'))
        self.line = cv2.imread(get_path(img_path, 'line.png'))
        self.line = cv2.cvtColor(self.line, cv2.COLOR_BGR2GRAY)
        self.target = cv2.imread(get_path(img_path, 'target.png'))
        self.point = cv2.imread(get_path(img_path, 'point.png'))
        if os.path.exists(get_path(img_path, 'sparePoint.png')):
            self.spare_point = cv2.imread(get_path(img_path, "sparePoint.png"))
        else:
            self.spare_point = None
        if os.path.exists(get_path(img_path, 'select.png')):
            self.select = cv2.imread(get_path(img_path, 'select.png'))
        else:
            self.select = None

        if self.cur_ball != ball_name:
            self.open_game_map()
            self.change_ball(ball_name)
            self.change_area(area_name)
            self.change_point(self.point)
        elif self.cur_area != area_name:
            self.open_game_map()
            self.change_area(area_name)
            self.change_point(self.point)
        else:
            self.open_game_map()
            self.change_point(self.point)
        self.last_ball = self.cur_ball
        self.last_area = self.cur_area
        self.cur_ball = ball_name
        self.cur_area = area_name
        self.reload_cnt = 0  # 置零

    @classmethod
    def in_map(cls):
        """判断是否地图界面"""
        return template_in_img(template_path.AREA_NAVIGATION, window.get_screenshot())


if __name__ == '__main__':
    m = Map(r"F:\AutoStarRail\script\world\map")
    print(m.data)
    while m.data:
        m.next()
