"""
截取地图图片并保存
1. 原图
2. 灰度图
3. 二值化图
"""
import os
import time

import cv2
import config
from utils import window

root = config.abspath


def map_shot_and_save(filename) -> None:
    """
    截取大地图1000*1400(w*h),并保存各种图.
    :return:
    """
    game_shot = window.save_game_screenshot()
    img = cv2.imread(game_shot)
    img = img[:1000, :1400]  # 截取宽1400高1000的部分
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 灰度图
    _, img_binary = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)

    cv2.imwrite(os.path.join(filename, 'default.png'), img)
    cv2.imwrite(os.path.join(filename, 'gray.png'), img_gray)
    cv2.imwrite(os.path.join(filename, 'binary.png'), img_binary)


def main(world_number: int, map_name: str):
    """
    请确保自己以及打开地图并且在传送点默认位置，地图需要最小化
    :param world_number: 星球
    :param map_name: 星球里面的地点以及传送点，例如城郊雪原传送点1
    :return:
    """
    print("1s后开始截图")
    time.sleep(1)
    map_path = os.path.join(root,
                            r"world\map",
                            str(world_number),
                            map_name
                            )
    os.makedirs(map_path, exist_ok=True)  # 若不存在则创建
    map_shot_and_save(map_path)
    print(f"截图完成，保存至{map_path}")


if __name__ == '__main__':
    main(2, '1-1')
