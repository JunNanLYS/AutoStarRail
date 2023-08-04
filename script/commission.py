import time

import cv2
import numpy as np
import pyautogui
from pydantic import BaseModel

from utils import func, path
from widgets import log


class Commission(BaseModel):
    name: str
    picture_filename: str


COMMISSION_TITLE_COUNT = 3  # 有3个委托标题 | 若后期米哈游更新新的标题可以直接在这里修改


def enter_commission(is_pending: bool = False) -> bool:
    """
    进入委托界面
    """
    log.transmitDebugLog("enter_commission运行")
    pyautogui.press('esc')
    time.sleep(1)
    commission_filename = path.ImagePath.COMMISSION_PENDING if is_pending else path.ImagePath.COMMISSION
    commission_point = func.cv_find_image(commission_filename)
    if commission_point == (-1, -1):
        return False
    p = (commission_point[0] + 25, commission_point[1] + 25)
    pyautogui.moveTo(*p)
    pyautogui.click()
    log.transmitRunLog("已进入委托界面")
    return True


def in_commission() -> bool:
    """
    判断是否在委托界面
    """
    log.transmitRunLog("判断是否在委托界面")
    res = func.cv_find_image(path.ImagePath.IS_COMMISSION)
    return res != (-1, -1)


def get_pending_point() -> list:
    """
    查找所有感叹号的位置
    """
    screenshot_filename = func.screenshot()  # 截图保存地址
    screenshot = cv2.imread(screenshot_filename)
    template = cv2.imread(path.ImagePath.PENDING)
    w, h, _ = template.shape  # 获取模板图宽和高

    # 定义红色和白色的颜色范围
    lower_red = np.array([0, 0, 200])
    upper_red = np.array([0, 0, 255])
    lower_white = np.array([210, 210, 210])
    upper_white = np.array([255, 255, 255])

    # 创建红色和白色掩膜
    mask_red = cv2.inRange(template, lower_red, upper_red)
    mask_white = cv2.inRange(template, lower_white, upper_white)

    # 合并掩膜
    mask = cv2.bitwise_or(mask_red, mask_white)

    # 应用模板匹配
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED, mask=mask)

    # 设定阈值
    threshold = 0.97

    # 找到所有匹配位置
    loc = np.where(result >= threshold)
    point = []  # 存储感叹号全局坐标

    for pt in zip(*loc[::-1]):
        top_left = pt
        point.append(top_left)

    return point


def receive_commission() -> bool:
    """
    接收委托
    """
    pass


def receive_commissioning_reward() -> bool:
    """
    接收委托奖励
    """
    log.transmitDebugLog("receive_commissioning_reward运行")
    point = func.cv_find_image(path.ImagePath.RECEIVE_COMMISSIONING_REWARD)
    if point == (-1, -1):
        log.transmitDebugLog("找不到领取奖励", level=2, debug=True)
        return False
    p = (point[0] + 25, point[1] + 25)
    pyautogui.moveTo(*p)
    pyautogui.click()
    time.sleep(0.5)
    pyautogui.moveTo(point[0] - 50, point[1] - 50)
    pyautogui.click()  # 此时有个弹窗，点击一下关闭
    return True


def re_commission() -> bool:
    """
    重新委托
    """
    log.transmitDebugLog("re_commission运行")
    point = func.cv_find_image(path.ImagePath.RE_COMMISSION)
    if point == (-1, -1):
        log.transmitDebugLog("找不到重新委托按钮", level=2, debug=True)
        return False
    p = (point[0] + 25, point[1] + 25)
    pyautogui.moveTo(*p)
    pyautogui.click()
    return True


if __name__ == '__main__':
    enter_commission()
