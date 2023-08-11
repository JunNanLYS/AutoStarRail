import os
import time

import win32gui
import pyautogui

from utils.tool import JsonTool
from utils import func, path
from widgets import log


def run() -> bool:
    """
    用于启动游戏和启动脚本时调用
    """
    log.transmitRunLog("\n开始检测", debug=True)
    game_name = "崩坏：星穹铁道"
    game_id = win32gui.FindWindow(None, game_name)  # 查找游戏句柄号
    # 游戏没启动，根据配置文件中游戏路径来开启游戏
    if game_id == 0:
        log.transmitRunLog("检测到游戏并未启动，正在根据配置的游戏路径开启游戏", debug=True)
        game_path = JsonTool.get_config_json().get("game_path", "")
        if not game_path:
            log.transmitRunLog("笨蛋，你还没有设置游戏启动器路径嘞")
            raise Exception("停止运行，游戏未运行且未设置游戏路径")
        os.startfile(game_path)  # 根据路径打开
        log.transmitRunLog("启动游戏", debug=True)

        # 等待启动器开启
        log.transmitRunLog("等待启动器启动", debug=True)
        while win32gui.FindWindow(None, game_name) != 0:
            break

        log.transmitRunLog("查找开始游戏按钮", debug=True)
        start_game_rect = func.wait_image(path.ImagePath.START_GAME)  # 查找开启游戏按钮的位置
        pyautogui.moveTo(start_game_rect)
        pyautogui.click()

        # 等待游戏启动
        log.transmitGameLog("等待游戏运行", debug=True)
        rect = func.wait_image(path.ImagePath.ENTER_GAME)
        pyautogui.moveTo(rect)
        pyautogui.click()
        log.transmitRunLog("点击进入游戏", debug=True)
        if win32gui.FindWindow(None, game_name) == 0:
            log.transmitDebugLog("没有检测到游戏运行")
            return False
        return True
    # 游戏启动了，将游戏设置为活动窗口，并启动游戏
    else:
        log.transmitRunLog("检测到游戏已启动，将其设置为活动窗口", debug=True)
        log.transmitRunLog("请保证游戏未处于最小窗口化状态，否则设置将失效")
        win32gui.SetForegroundWindow(game_id)
        time.sleep(1)
        rect = func.find_image(path.ImagePath.MANDATE)
        pyautogui.moveTo(rect)
        pyautogui.click()
        return True
