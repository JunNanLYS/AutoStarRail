import os
import time
import win32gui
import pyautogui

from utils.tool import JsonTool
from utils.path import ImagePath
from utils import func
from widgets import log
from threadpool import script_thread


def start_game() -> bool:
    """
    用于启动游戏和启动脚本时调用
    :return: None
    """
    log.transmitRunLog("\n开始检测", output=True)
    game_name = "崩坏：星穹铁道"
    game_id = win32gui.FindWindow(None, game_name)
    # 游戏没启动，根据配置文件中游戏路径来开启游戏
    if game_id == 0:
        log.transmitRunLog("检测到游戏并未启动，正在根据配置的游戏路径开启游戏", output=True)
        game_path = JsonTool.get_config_json().get("game_path", "")
        if not game_path:
            log.transmitRunLog("没有设置游戏路径", output=True)
            return False
        os.startfile(game_path)
        log.transmitRunLog("启动游戏", output=True)

        # 等待启动器开启
        log.transmitRunLog("等待启动器启动", output=True)
        while win32gui.FindWindow(None, game_name) != 0:
            break

        log.transmitRunLog("查找开始游戏按钮", output=True)
        start_game_rect = func.wait_image(ImagePath.START_GAME)  # 查找开启游戏按钮的位置
        pyautogui.moveTo(start_game_rect)
        pyautogui.click()

        # 等待游戏启动
        log.transmitGameLog("等待游戏运行", output=True)
        rect = func.wait_image(ImagePath.ENTER_GAME)
        pyautogui.moveTo(rect)
        pyautogui.click()
        log.transmitRunLog("检查完毕，游戏已经成功运行", output=True)
        return True

    # 游戏启动了，将游戏设置为活动窗口，并启动游戏
    else:
        log.transmitRunLog("检测到游戏已启动，将其设置为活动窗口", output=True)
        win32gui.SetForegroundWindow(game_id)
        time.sleep(1)
        start_game_rect = pyautogui.locateOnScreen(ImagePath.START_GAME, confidence=0.8)  # 查找开启游戏按钮的位置
        if start_game_rect is not None:
            pyautogui.moveTo(start_game_rect)
            pyautogui.click()
        pyautogui.click()
        return True
