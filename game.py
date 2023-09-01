import ctypes
import time

import cv2
import win32gui


def get_somthing():
    """获取游戏窗口宽度以及高度，这是缩放后的"""
    while True:
        hwnd = win32gui.GetForegroundWindow()
        text = win32gui.GetWindowText(hwnd)
        x1, y1, x2, y2 = win32gui.GetClientRect(hwnd)
        w = x2 - x1
        h = y2 - y1
        print(x1, y1, x2, y2)
        s = ctypes.windll.user32.GetDpiForWindow(hwnd) / 96.0
        if text != "崩坏：星穹铁道":
            time.sleep(0.3)
        else:
            time.sleep(1)
            return w * s, h * s, s


def get_rect():
    """
    :return: (left, top, right, bottom)
    """
    from widgets import log
    from utils import window
    while True:
        hwnd = win32gui.GetForegroundWindow()
        text = win32gui.GetWindowText(hwnd)
        x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
        s = window.get_scaling()
        x1, y1 = x1 * s, y1 * s
        x2, y2 = x2 * s, y2 * s
        if text != "崩坏：星穹铁道":
            time.sleep(0.3)
            log.transmitDebugLog(f"等待游戏界面")
        else:
            return x1, y1, x2, y2


def screenshot():
    """
    :return: np.ndarray
    """
    from PIL import ImageGrab
    import numpy as np
    img = ImageGrab.grab(bbox=get_rect())
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


if __name__ == '__main__':
    i = screenshot()
    cv2.imshow("img", i)
    cv2.waitKey(0)
