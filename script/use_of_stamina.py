import time

import pyautogui

from script.stamina import STRING_TO_CALLBACK
from script.start_game import start_game
from utils.path import ImagePath
from utils import func, check
from widgets import log


def use_of_stamina(copies: dict):
    """
    用于清理体力的方法
    :param copies: 保存着各个副本要进行的次数
    copies = {name: count}
    副本名称对应着次数
    """
    start_game()  # 开启游戏
    func.wait_image(ImagePath.MANDATE)  # 等待进入游戏

    for c, cnt in copies.items():
        method, param = STRING_TO_CALLBACK.get(c, None)
        if method is None:
            log.transmitRunLog(f"警告：出现不存在的字符串({c}) [use_of_stamina]", debug=True)
            continue
        # 打副本，直到达成目标或出现意外(体力不够等情况)
        while cnt > 0:
            res = method(*param)
            if not res:  # 没有进入副本界面
                log.transmitRunLog(f"警告：没有进入副本界面({c}) []use_of_stamina")
                break

            # 进入副本界面后增加挑战次数，因为默认是1次，所以鼠标点击cnt-1次就行了。
            diff = 1  # 减少的挑战次数
            if cnt > 6:
                if func.add_challenge(5):
                    diff = 6
            else:
                if func.add_challenge(cnt - 1):
                    diff = cnt
            cnt -= diff

            # 进入挑战
            func.challenge()
            log.transmitAllLog("进入挑战")
            # 开始挑战
            func.start_challenge()
            log.transmitRunLog("开始挑战")
            # 判断是否还在主界面(有些副本需要自己主动攻击怪物)
            log.transmitRunLog("判断是否需要主动攻击怪物")
            if func.find_image(ImagePath.MANDATE):
                time.sleep(1)
                pyautogui.keyDown('w')
                time.sleep(0.5)
                pyautogui.keyUp('w')
                pyautogui.click()
            # 等待挑战完成(阻塞主线程)
            log.transmitRunLog("等待挑战完成")
            check.wait_challenge_completed()
            # 退出副本界面
            func.exit_copies()
            log.transmitAllLog("退出副本")

    log.transmitAllLog("体力清理完成")
