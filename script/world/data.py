import os
import time
from collections import defaultdict
from typing import Tuple, Optional, Dict, List, Union

import cv2
from numpy import ndarray

import log
from script.utils import (mouse, wait_img, template_path, get_text_position, match_template)

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


class MapData:
    def __init__(self, root):
        """
        :param root: 存储地图的根目录
        """
        self._ball = defaultdict(list)  # ball name: area name
        self._area = defaultdict(list)  # area name: images path
        self._generator = None
        self._root = root
        self.__next_data: Optional[Tuple[str, str, str]] = None

        self.load()
        self.update_generator()

    def _add_area(self, ball: str, area: str) -> None:
        """将区域添加到星球字典中"""
        if area in self._ball[ball]:
            log.debug(f"星球[{ball}]已存在区域[{area}]")
            return
        self._ball[ball].append(area)

    def _add_path(self, area: str, path: str) -> None:
        """将图片路径添加到区域字典中"""
        if path in self._area[area]:
            log.debug(f"区域[{area}]已存在图片目录[{path}]")
            return
        self._area[area].append(path)

    def empty(self):
        """生成器若为空则self.__data为None"""
        return self.__next_data is None

    def load(self) -> None:
        """加载地图根目录下所有图片"""
        if not isinstance(self._root, str):
            raise TypeError("地图根目录必须是字符串类型")
        if not self._root:
            raise Exception("请给出正确的地图根目录")
        balls = os.listdir(self._root)
        for ball_str in balls:
            areas = os.listdir(os.path.join(self._root, ball_str))
            ball_int = int(ball_str)
            for area_str in areas:
                points = os.listdir(os.path.join(self._root, ball_str, area_str))
                area_int = int(area_str)
                area_name = AREA_NAME[ball_int][area_int - 1]
                ball_name = BALL_NAME[ball_int]
                self._add_area(ball_name, area_name)
                for point_str in points:
                    path = os.path.join(self._root, ball_str, area_str, point_str)
                    self._add_path(area_name, path)

    def update_generator(self) -> None:

        def func():
            for ball_name, area_names in self._ball.items():
                for area_name in area_names:
                    for path in self._area[area_name]:
                        yield ball_name, area_name, path

        self._generator = func()
        self.next()  # 初始化self.__next_data

    def next(self) -> Union[Tuple, None]:
        """返回下一张地图的数据。（星球名，区域名，图片路径）"""
        temp = self.__next_data
        try:
            self.__next_data = next(self._generator)
        except StopIteration:
            self.__next_data = None
        return temp


class Map:
    def __init__(self, map_path: str):
        self.last_ball = ""
        self.last_area = ""
        self.cur_ball = ""
        self.cur_area = ""
        self.reload_cnt = 0
        self.data = MapData(map_path)

        # current map image
        self.default: Optional[ndarray] = None  # 原图
        self.binary: Optional[ndarray] = None  # 路线图
        self.line: Optional[ndarray] = None  # 用于匹配的图
        self.target: Optional[ndarray] = None  # 怪点图
        self.point: Optional[ndarray] = None  # 传送点图
        self.spare_point: Optional[ndarray] = None  # 备用传送点图（有些传送点会因为角色当前所在层改变）
        self.select: Optional[ndarray] = None  # 选中传送点图（部分传送点点击后还需要再次点击选择）

    def change_ball(self):
        """切换星球"""
        import game
        pos = get_text_position(game.get_screenshot(), "星轨航图")
        mouse.click_positions(pos, game_pos=True)
        wait_img(template_path.BALL_NAVIGATION)
        time.sleep(1)
        pos = get_text_position(game.get_screenshot(), self.cur_ball)
        mouse.click_positions(pos, direction="topLeft", val=100, game_pos=True)
        wait_img(template_path.AREA_NAVIGATION)

    def change_area(self):
        """切换区域"""
        import game
        # (1470 300) 这个地图第一个区域的位置
        x1, y1, _, _ = game.get_rect()
        mouse.click_position((x1 + 1470, y1 + 300))
        while True:
            pos = get_text_position(game.get_screenshot(), self.cur_area)
            if pos.size == 0:
                mouse.mouse_scroll(2)
                continue
            mouse.click_positions(pos, game_pos=True)
            time.sleep(0.2)
            break

    def change_point(self):
        """在当前地图查找传送点并进入"""
        import game
        x1, y1, _, _ = game.get_rect()
        map_center = (x1 + 800, y1 + 600)
        mouse.click_position(map_center)
        move = 400
        h, w = self.point.shape[:2]

        def click_point_and_send(p):
            mouse.click_position((p[0] + w // 2, p[1] + h // 2), game_pos=True)
            time.sleep(0.5)
            # 部分传送点点击后会出现菜单让你再次确定
            if self.select is not None:
                select_p = match_template(game.get_screenshot(), self.select)
                mouse.click_position(select_p, direction='bottomRight', val=10, game_pos=True)
            wait_img(template_path.SEND_TEXT)
            send_p = match_template(game.get_screenshot(), template_path.SEND_TEXT)
            mouse.click_position(send_p, game_pos=True)
            wait_img(template_path.MANDATE, mode='gray')
            time.sleep(2)

        def find_point() -> bool:
            """查找传送点"""
            pos = match_template(game.get_screenshot(), self.point)
            if pos != (-1, -1):
                click_point_and_send(pos)
                return True
            if self.spare_point is not None:
                pos = match_template(game.get_screenshot(), self.spare_point)
                if pos != (-1, -1):
                    click_point_and_send(pos)
                    return True
            return False

        if find_point():
            return
        dic = {"left": (map_center[0], map_center[1] - move),
               "right": (map_center[0] + move, map_center[1]),
               "up": (map_center[0], map_center[1] - move),
               "under": (map_center[0], map_center[1] + move)}
        lis = ["left", "left", "right", "right", "up", "up", "under", "under"]
        idx = 0
        log.debug("开始拖动地图查找传送点")
        while True:
            k = lis[idx % len(lis)]
            target = dic[k]
            mouse.down_move(map_center, target)
            if find_point():
                return
            idx += 1

    @classmethod
    def open_game_map(cls):
        """进入游戏地图"""
        import pyautogui
        import game
        from config import cfg
        game.to_game_main()
        pyautogui.press(cfg.get(cfg.open_map))
        time.sleep(2)
        cnt = 0
        while True:
            pos = match_template(game.get_screenshot(), template_path.AREA_NAVIGATION)
            if pos != (-1, -1):
                break
            if cnt % 2 == 0:
                game.to_game_main()
            pyautogui.press(cfg.get(cfg.open_map))
            time.sleep(4)
        mouse.mouse_scroll(3)  # 地图缩放至最小

    def reload_current_map(self):
        """重新进入当前地图"""
        self.reload_cnt += 1
        self.open_game_map()
        self.change_point()

    def next(self) -> bool:
        """进入下一场地图"""
        temp = self.data.next()
        if temp is None:
            log.info("没有待锄地图")
            return False
        ball_name, area_name, img_path = temp
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
        self.last_ball = self.cur_ball
        self.last_area = self.cur_area
        self.cur_ball = ball_name
        self.cur_area = area_name
        self.reload_cnt = 0  # 置零

        if self.last_ball != ball_name:
            log.info("检测到不同星球")
            self.open_game_map()
            self.change_ball()
            self.change_area()
            self.change_point()
        elif self.last_area != area_name:
            log.info("检测到不同区域")
            self.open_game_map()
            self.change_area()
            self.change_point()
        else:
            log.info("检测到不同传送点")
            self.open_game_map()
            self.change_point()
        return True


if __name__ == '__main__':
    data = MapData(r"F:\AutoStarRail\script\world\map")
    while not data.empty():
        print(data.next())
