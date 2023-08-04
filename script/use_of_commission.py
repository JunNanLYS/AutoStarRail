import time

import pyautogui

from script import commission, start_game
from widgets import log
from utils import func, cv_tool


def run():
    start_game.start_game()
    log.transmitAllLog("开始清理委托")
    if not func.in_game_main():
        log.transmitRunLog("检测到未在游戏主界面")
        if not func.to_game_main():
            log.transmitRunLog("未成功进入游戏主界面，退出")
            log.transmitDebugLog("未成功进入游戏主界面，退出", debug=True, level=2)
            return
    commission.enter_commission()  # 进入委托界面
    log.transmitRunLog("等待进入委托界面,10秒等待时长")
    for _ in range(10):
        if commission.in_commission():
            break
        time.sleep(1)
    else:
        log.transmitRunLog("等待超时，退出", debug=True)
        return

    pending_points = commission.get_pending_point()  # 获取所有感叹号的位置
    pending_points = cv_tool.remove_same_position(pending_points, 3)  # 去重
    if not pending_points:
        log.transmitAllLog("没有待领取的委托", debug=True)
        return

    pending_points.sort(key=lambda p: p[1])  # 按照y进行排序
    title_y = pending_points[0][1]  # 标题所在的纵轴
    error_value = 3  # 在这上下浮动
    title_y_lower, title_y_upper = title_y - error_value, title_y + error_value
    commission_title = [point for point in pending_points if title_y_lower <= point[1] <= title_y_upper]
    if len(commission_title) > commission.COMMISSION_TITLE_COUNT:
        log.transmitDebugLog(f"感叹号应为{commission.COMMISSION_TITLE_COUNT},"
                             f"实际为{len(commission_title)},"
                             f"内容为{commission_title}")

    log.transmitRunLog("开始模拟鼠标")
    for title_point in commission_title:
        title_p = (title_point[0] - 25, title_point[1] + 25)  # 感叹号在右上角且按钮在左下角，所以向左下角移动
        pyautogui.moveTo(*title_p)
        pyautogui.click()
        log.transmitRunLog("移动至委托标题")
        time.sleep(1)
        flag = True
        while flag:
            # 每次领取完或者打开新委托标题重新获取感叹号(感叹号会刷新)
            pending_points = cv_tool.remove_same_position(
                sorted(commission.get_pending_point(), key=lambda p: p[1]), 3)
            for child in pending_points:
                if child in commission_title:
                    continue
                child_p = (child[0] - 25, child[1] + 25)  # 感叹号在右上角且按钮在左下角，所以向左下角移动
                pyautogui.moveTo(*child_p)
                pyautogui.click()
                log.transmitRunLog("移动至委托内容")
                commission.receive_commissioning_reward()  # 领取奖励
                log.transmitRunLog("领取奖励")
                time.sleep(1)
                commission.re_commission()  # 重新委托
                log.transmitRunLog("重新委托")
                time.sleep(2)
                break
            else:
                flag = False
    log.transmitAllLog("委托清理完毕")


if __name__ == '__main__':
    run()
