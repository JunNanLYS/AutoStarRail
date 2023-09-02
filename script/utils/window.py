import win32con
import win32api
import win32gui
import win32print
from numpy import ndarray
from PIL import ImageGrab


def get_read_size():
    """获取真实分辨率"""
    hDC = win32gui.GetDC(0)
    w = win32print.GetDeviceCaps(hDC, win32con.DESKTOPHORZRES)
    h = win32print.GetDeviceCaps(hDC, win32con.DESKTOPVERTRES)
    return w, h


def get_screen_size():
    """缩放后的分辨率"""
    w = win32api.GetSystemMetrics(0)
    h = win32api.GetSystemMetrics(1)
    return w, h


def get_scaling():
    """获取缩放率"""
    return round(get_read_size()[0] / get_screen_size()[0], 2)


def get_screenshot() -> ndarray:
    """获取屏幕截图"""
    import cv2
    import numpy as np
    img = ImageGrab.grab()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img
