import ctypes
import time

import win32gui

import log


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
    from script.utils import window
    while True:
        hwnd = win32gui.GetForegroundWindow()
        text = win32gui.GetWindowText(hwnd)
        x1, y1, x2, y2 = win32gui.GetWindowRect(hwnd)
        s = window.get_scaling()
        x1, y1 = x1 * s, y1 * s
        x2, y2 = x2 * s, y2 * s
        if text != "崩坏：星穹铁道":
            time.sleep(0.3)
            print("等待游戏界面")
        else:
            return x1, y1, x2, y2


def get_screenshot():
    """
    :return: np.ndarray
    """
    from PIL import ImageGrab
    import cv2
    import numpy as np
    img = ImageGrab.grab(bbox=get_rect())
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


def set_foreground():
    """将游戏设置为前台"""
    import pythoncom
    import win32com.client
    pythoncom.CoInitialize()
    shell = win32com.client.Dispatch("WScript.Shell")
    shell.SendKeys("")  # Undocks my focus from Python IDLE
    hwnd = win32gui.FindWindow("UnityWndClass", "崩坏：星穹铁道")
    win32gui.SetForegroundWindow(hwnd)
    time.sleep(0.3)


def to_game_main():
    """返回游戏主界面"""
    import cv2
    import pyautogui
    from script.utils import template_path, match_template_gray
    cnt = 1
    template = cv2.imread(template_path.PHONE)
    while True:
        img = get_screenshot()  # 获取游戏内截图
        if match_template_gray(img, template) != (-1, -1):
            break
        log.info(f"尝试回到主界面，这是第{cnt}次尝试")
        pyautogui.press('esc')
        time.sleep(0.8)
        cnt += 1


if __name__ == '__main__':
    set_foreground()
