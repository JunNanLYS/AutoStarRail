import time

import pyautogui
import win32gui

from script.stamina import STRING_TO_CALLBACK
from script import start_game
from utils.path import ImagePath
from utils import func, check, tool, dialog
from widgets import log

is_stop = False  # 设置True就能关闭运行中的脚本(use_of_stamina)


def run(copies: dict):
    """
    用于清理体力的方法
    :param copies: 保存着各个副本要进行的次数
    copies = {name: count}
    副本名称对应着次数
    """
    global is_stop
    log.transmitAllLog("请确保自己使用管理员身份启动的脚本，否则一切操作将失效")
    start_game.run()  # 开启游戏
    if win32gui.FindWindow(None, "崩坏：星穹铁道") == 0:
        log.transmitAllLog("没有检测到游戏，请检查是否设置游戏路径，或者手动开启游戏")
        return
    func.wait_image(ImagePath.MANDATE)  # 等待进入游戏
    json_ = tool.JsonTool.get_config_json()

    for c, cnt in copies.items():
        method, param = STRING_TO_CALLBACK.get(c, None)
        if method is None or param is None:
            log.transmitDebugLog(f"警告：出现不存在的字符串({c}) [use_of_stamina]", debug=True, level=2)
            log.transmitRunLog(f"出现不存在的字符串，准备跳过其")
            continue
        # 打副本，直到达成目标或出现意外(体力不够等情况)
        while cnt > 0:
            if is_stop:  # 暂停
                break
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

            # 需要补充体力
            if check.is_no_stamina():
                flag = True
                # 使用燃料
                if json_['use_fuel']:
                    flag = False
                    number = json_['fuel_number']
                    if not func.use_fuel(number):
                        log.transmitRunLog("没有成功使用燃料,退出")
                        func.to_game_main()
                        set_stop(True)
                        break
                # 使用星穹
                if flag and json_['use_explore']:
                    # 使用星穹目前还没想好怎么写
                    if not func.use_explore():
                        log.transmitRunLog("没有成功使用开拓力,退出")
                        func.to_game_main()
                        set_stop(True)
                        break
                func.challenge()

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
            if not json_['auto-fight']:
                log.transmitAllLog("设置选项-自动战斗：否")
                pass
            # 等待挑战完成(阻塞线程)
            log.transmitRunLog("等待挑战完成")
            check.wait_challenge_completed()
            # 退出副本界面
            func.exit_copies()
            log.transmitAllLog("退出副本")
        if is_stop:
            is_stop = False
            log.transmitRunLog("已停止清体力")
            break
    if not func.in_game_main():
        func.to_game_main()  # 若不在主界面则回到主界面
    log.transmitAllLog("体力清理完成")
    dialog.new_win_message("温馨提示", "体力清理完成")


def set_stop(stop: bool):
    global is_stop
    is_stop = stop
    log.transmitAllLog(f"设置stop为{stop}")


if __name__ == '__main__':
    run({"calyx_4": 4})
