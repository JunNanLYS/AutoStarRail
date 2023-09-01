import os

import win32con
import win32api
import win32gui
import pygetwindow
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


def get_game_window():
    """获取游戏"""
    return pygetwindow.getWindowsWithTitle("崩坏：星穹铁道")[0]


def get_screenshot() -> ndarray:
    """获取屏幕截图"""
    import cv2
    import numpy as np
    img = ImageGrab.grab()
    img = np.array(img)
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    return img


def save_game_screenshot(name="game_screenshot") -> str:
    """
    截取游戏截图并保存,保存格式为.png
    :return: 路径
    """
    import config
    root = config.abspath
    target_path = os.path.join(root, "temp", name + '.png')
    game = get_game_window()
    scaling = get_scaling()
    left, top = game.left * scaling, game.top * scaling
    width, height = game.width * scaling, game.height * scaling
    img = ImageGrab.grab(bbox=(left, top, left + width, top + height))
    img.save(target_path)
    return target_path
