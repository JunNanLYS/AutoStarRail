import time
import pyautogui

from widgets import log
from utils.path import ImagePath


def fight() -> bool:
    rect = find_image(ImagePath.CHALLENGE)
    if rect:
        pyautogui.moveTo(rect)
        pyautogui.click()
        return True
    return False


def renewed_fight() -> bool:
    pass


def challenge() -> bool:
    """
    挑战
    """
    rect = find_image(ImagePath.CHALLENGE)
    if rect:
        pyautogui.moveTo(rect)
        pyautogui.click()
        time.sleep(1)
        return True
    return False


def start_challenge() -> bool:
    """
    开始挑战
    """
    rect = find_image(ImagePath.START_CHALLENGE)
    if rect:
        pyautogui.moveTo(rect)
        pyautogui.click()
        time.sleep(1)
        return True
    return False


def add_challenge(cnt: int) -> bool:
    """
    添加副本挑战次数
    :param cnt: 要增加的次数
    """
    rect = find_image(ImagePath.ADD_CHALLENGE)
    if rect:
        pyautogui.moveTo(rect)
        for _ in range(cnt):
            pyautogui.click()
            time.sleep(0.2)
        return True
    return False


def exit_copies() -> bool:
    """
    退出副本
    """
    rect = find_image(ImagePath.EXIT_COPIES)
    if rect:
        pyautogui.moveTo(rect)
        pyautogui.click()
        time.sleep(2)
        return True
    return False


def closest_point(points, new_point):
    """
    计算最近点
    """
    min_distance = float('inf')
    res_point = None
    for point in points:
        distance = ((point[0] - new_point[0]) ** 2 + (point[1] - new_point[1]) ** 2) ** 0.5
        if distance < min_distance:
            min_distance = distance
            res_point = point
    return res_point


def find_image(image_name, max_count=3, confidence=0.85):
    log.transmitRunLog(f"查找图片{image_name}", output=True)
    for _ in range(max_count):
        rect = pyautogui.locateOnScreen(image_name, confidence=confidence)
        if rect:
            log.transmitRunLog("查找到图片", output=True)
            return rect
        time.sleep(1)
    log.transmitRunLog("未查找到图片", output=True)
    return None


def wait_image(image_name, confidence=0.8, max_time=100):
    log.transmitRunLog(f"等待图片{image_name}", output=True)
    count = 0
    while True:
        rect = pyautogui.locateOnScreen(image_name, confidence=confidence)
        if rect:
            log.transmitRunLog("找到图片", output=True)
            return rect
        time.sleep(1)
        count += 1

        # 超时了退出循环
        if count >= max_time:
            log.transmitRunLog("等待超过100秒", output=True)
            break
    log.transmitRunLog("未查找到图片", output=True)
    return None
