import time
import pyautogui
import cv2
from typing import Tuple

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


def find_image(filename, max_count=3, confidence=0.85):
    image_name = filename.split('\\')[-1]
    log.transmitRunLog(f"查找图片{image_name}", debug=True)
    for _ in range(max_count):
        rect = pyautogui.locateOnScreen(filename, confidence=confidence)
        if rect:
            log.transmitRunLog("查找到图片", debug=True)
            return rect
        time.sleep(1)
    log.transmitRunLog("未查找到图片", debug=True)
    return None


def wait_image(filename: str, confidence=0.8, max_time=60):
    image_name = filename.split('\\')[-1]
    log.transmitRunLog(f"等待图片{image_name}", debug=True)
    count = 0
    while True:
        print("查找图片")
        rect = pyautogui.locateOnScreen(filename, confidence=confidence)
        if rect:
            log.transmitRunLog("找到图片", debug=True)
            return rect
        time.sleep(2)
        count += 1

        # 超时了退出循环
        if count >= max_time:
            log.transmitRunLog("等待超过100秒", debug=True)
            break
    log.transmitRunLog("未查找到图片", debug=True)
    return None


def use_fuel(number: int):
    """
    使用燃料
    """
    # 点击燃料
    fuel_rect = find_image(ImagePath.FUEL, confidence=0.7)
    pyautogui.moveTo(fuel_rect)
    pyautogui.click()
    # 点击确定
    confirm_rect = find_image(ImagePath.CONFIRM)
    pyautogui.moveTo(confirm_rect)
    pyautogui.click()

    # 添加使用数量
    add_rect = find_image(ImagePath.ADD_CHALLENGE)
    pyautogui.moveTo(add_rect)
    for _ in range(number):
        pyautogui.click()
        time.sleep(0.2)

    # 确认
    confirm_rect = find_image(ImagePath.CONFIRM)
    pyautogui.moveTo(confirm_rect)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()


def use_explore():
    """
    使用开拓力
    """
    # 点击星穹
    stellar_jade_rect = find_image(ImagePath.STELLAR_JADE)
    pyautogui.moveTo(stellar_jade_rect)
    pyautogui.click()
    # 点击确定
    confirm_rect = find_image(ImagePath.CONFIRM)
    pyautogui.moveTo(confirm_rect)
    pyautogui.click()
    time.sleep(0.5)

    # 此时会弹出是否要使用，确认使用
    confirm_rect = find_image(ImagePath.CONFIRM)
    pyautogui.moveTo(confirm_rect)
    pyautogui.click()
    time.sleep(0.2)
    pyautogui.click()


def screenshot() -> str:
    """
    截取全屏
    """
    from PIL import ImageGrab
    from utils.tool import PathTool
    img = ImageGrab.grab()
    root = PathTool.get_root_path()
    filename = root + r"\temp\screenshot.png"
    img.save(filename)
    return filename


def cv_find_image(filename: str) -> Tuple[int, int]:
    """
    相比于直接使用pyautogui，cv2更加准确精准
    返回模板图的全局坐标
    """
    log.transmitRunLog("截图全屏中")
    screenshot_filename = screenshot()
    # 读取截取和模板
    screen = cv2.imread(screenshot_filename)
    template = cv2.imread(filename)

    log.transmitRunLog("进行模板匹配")
    res = cv2.matchTemplate(screen, template, cv2.TM_CCOEFF_NORMED)
    # 获取最小匹配与位置，最大匹配与位置
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    # 不匹配
    if max_val < 0.95:
        log.transmitRunLog("匹配失败")
        log.transmitDebugLog("匹配值低于0.95", debug=True, level=2)
        return -1, -1
    log.transmitRunLog("匹配成功")
    return max_loc


def in_game_main() -> bool:
    """
    检测是否在游戏主界面
    """
    log.transmitDebugLog("in_game_main运行")
    return cv_find_image(ImagePath.MANDATE) != (-1, -1)


def to_game_main() -> bool:
    """
    尝试将游戏切换至主界面
    """
    log.transmitDebugLog("to_game_main运行")
    mandate = ImagePath.MANDATE
    cnt = 0
    max_cnt = 6
    press = 1
    while cv_find_image(mandate) == (-1, -1) and cnt <= max_cnt:
        log.transmitDebugLog(f"检测到不在主界面，尝试切回主界面，这是第{cnt}次尝试")
        for _ in range(press):
            pyautogui.press('esc')
            time.sleep(0.3)
        press = 2 if press == 1 else 1
        cnt += 1
        time.sleep(1)

    return in_game_main()
