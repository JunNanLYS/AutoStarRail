import os
import time

import cv2
import pyautogui

from utils import path, window, func
from widgets import log
import config

filename = path.ImagePath


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

        angle += add_angle
        log.transmitDebugLog(f"val={val}, loc={loc}, angle={angle}")

    return val, loc


def capture_minimap():
    """截取小地图"""
    map_size = 160  # 要截取的小地图的宽度
    # 读取模板图
    template_phone = cv2.imread(filename.PHONE)
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
    template_mandate = cv2.imread(filename.MANDATE)
    mandate_h, mandate_w = template_mandate.shape[:2]
    template_mandate = cv2.cvtColor(template_mandate, cv2.COLOR_BGR2GRAY)
    mandate_res = cv2.matchTemplate(game_img_gray, template_mandate, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(mandate_res)

    x2 = max_loc[0] + mandate_w + map_size
    y2 = max_loc[1] + (mandate_h // 2)

    game_img = game_img[y1:y2, x1:x2]  # 截取小地图部分
    write_path = os.path.join(config.abspath, "temp", "minimap.png")
    cv2.imwrite(write_path, game_img)
    return write_path


def capture_atlas(radius: int = 90):
    """截取大地图中玩家坐标为中心辐射radius截图"""
    if not to_map():
        log.transmitDebugLog("没有进入地图", level=4)
        raise Exception("没有进入地图")
    time.sleep(1)
    img = cv2.imread(window.save_game_screenshot())
    arrow_p1, arrow_p2, img = locate_role(img)  # 获取角色指向标左上角和右下角以及定位后的img
    arrow_w = arrow_p2[0] - arrow_p1[0]  # 宽
    arrow_h = arrow_p2[1] - arrow_p1[1]  # 高
    center = (arrow_p1[0] + arrow_w // 2, arrow_p1[1] + arrow_h // 2)  # 中心点
    capture_p1 = (center[0] - radius, center[1] - radius)
    capture_p2 = (center[0] + radius, center[1] + radius)

    # cv2.rectangle(img, arrow_p1, arrow_p2, (0, 0, 255), 1)
    # cv2.rectangle(img, arrow_p1, center, (0, 0, 255), 1)
    # cv2.rectangle(img, capture_p1, capture_p2, (0, 0, 255), 2)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)

    return img[capture_p1[1]:capture_p2[1], capture_p1[0]:capture_p2[0]]


def locate_role(img):
    """给一张图，从这张图中定位玩家箭头位置"""
    img = img[:, :1416]  # 去掉右边的干扰因素
    thresholds = 0.8  # 阈值
    arrow = cv2.imread(filename.ARROW_DOWN)
    h, w = arrow.shape[:2]

    # 先查找特殊角度
    val, loc = rotate_search_img(img, arrow, 45, thresholds)

    # 未满足阈值，开启全角度搜索
    if val < thresholds:
        log.transmitDebugLog("开启全角度搜索")
        new_val, new_loc = rotate_search_img(img, arrow, 2, thresholds)
        if new_val > val:
            val = new_val
            loc = new_loc

    if val < thresholds:
        def move_search(direction: str):
            nonlocal img, val, loc, new_val, new_loc
            log.transmitDebugLog("定位失败,尝试乱走定位")
            func.to_game_main()
            pyautogui.keyDown(direction)
            time.sleep(1)
            pyautogui.keyUp(direction)
            time.sleep(0.5)
            to_map()

            img = cv2.imread(window.save_game_screenshot())
            img = img[:, :1416]
            new_val, new_loc = rotate_search_img(img, arrow, 2, thresholds)
            if new_val > val:
                val = new_val
                loc = new_loc
            return val >= thresholds

        moves = ['w', 'a', 'a', 's', 's', 'd', 'd']
        for direction in moves:
            if move_search(direction):
                break

    top_left = loc
    bottom_right = (loc[0] + w, loc[1] + h)
    # cv2.rectangle(img, loc, bottom_right, (0, 0, 255), 2)
    # cv2.imshow("img", img)
    # cv2.waitKey(0)

    return top_left, bottom_right, img


def remove_arrow(img):
    """删除小地图上角色指向标"""
    top_left, bottom_right, _ = locate_role(img)
    img[top_left[1]: bottom_right[1], top_left[0]: bottom_right[0]] = 32
    cv2.imshow("img", img)
    cv2.waitKey(0)
    return img


if __name__ == "__main__":
    # remove_arrow(cv2.imread(window.save_game_screenshot()))
    # img = cv2.imread(window.save_game_screenshot())
    # img = img[:, :1416]
    # locate_role(img)
    capture_atlas()
