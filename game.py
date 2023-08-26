import ctypes
import time

import win32gui


def get_somthing():
    """获取游戏窗口宽度以及高度，这是缩放后的"""
    while True:
        hwnd = win32gui.GetForegroundWindow()
        text = win32gui.GetWindowText(hwnd)
        x1, y1, x2, y2 = win32gui.GetClientRect(hwnd)
        w = x2 - x1
        h = y2 - y1
        s = ctypes.windll.user32.GetDpiForWindow(hwnd) / 96.0
        if text != "崩坏：星穹铁道":
            time.sleep(0.3)
        else:
            time.sleep(1)
            return w, h, s


__w, __h, scale = get_somthing()
width = scale * __w
height = scale * __h

if __name__ == '__main__':
    print(width, height, scale)
