import time
import pyautogui

from utils.path import ImagePath
from utils import func, check
from script.start_game import start_game
from widgets import log
from threadpool import script_thread

"""
拟造花萼：10
凝滞虚影：30
侵蚀隧洞：40
历战余响：30
"""


def enter_book() -> bool:
    """
    进入星际和平指南界面
    """
    log.transmitRunLog("命令：进入星际和平书", output=True)
    book = ImagePath.BOOK
    box = func.find_image(book)
    if box:
        log.transmitRunLog("找到书", output=True)
        pyautogui.keyDown('alt')
        pyautogui.moveTo(box)
        pyautogui.click()  # 进入星际和平书界面
        pyautogui.keyUp('alt')
    else:
        log.transmitAllLog("没找到书", output=True)
        # 可能是已经在书界面了
        return False
    time.sleep(1)
    return True


def enter_index() -> bool:
    """
    进入生存索引界面
    """
    index = ImagePath.INDEX
    index_selected = ImagePath.INDEX_SELECTED
    index_box = func.find_image(index)

    if index_box:
        log.transmitRunLog("找到生存索引")
        # 进入生存索引
        pyautogui.moveTo(index_box)
        pyautogui.click()
    elif pos := func.find_image(index_selected):
        log.transmitRunLog("检测到生存索引已被选择")
        pyautogui.moveTo(pos)
    else:
        log.transmitRunLog("没找到生存索引", output=True)
        return False
    time.sleep(1)
    return True


def enter_calyx_gold() -> bool:
    """
    进入花萼(金)
    """
    log.transmitRunLog("命令：进入花萼(金)")
    calyx = ImagePath.CALYX_GOLD
    box = func.find_image(calyx)
    if box:
        log.transmitAllLog("找到花萼")
        pyautogui.moveTo(box)
        pyautogui.click()
    # 花萼已经被选中
    elif func.find_image(ImagePath.CALYX_GOLD_SELECTED):
        log.transmitRunLog("检测到花萼已被选中")
    else:
        log.transmitRunLog("找不到花萼", output=True)
        return False
    time.sleep(1)
    return True


class Calyx:
    @classmethod
    def enter_calyx_gold(cls) -> bool:
        """
        进入金花萼
        """
        if not enter_book():  # 进入”星际和平书“界面
            return False
        if not enter_index():  # 进入“生存索引”界面
            return False
        if not enter_calyx_gold():  # 进入金花萼
            return False
        return True

    @classmethod
    def enter_calyx_red(cls) -> bool:
        """
        进入赤花萼
        """
        pass

    @classmethod
    def enter_characterEXP(cls) -> bool:
        """
        进入“角色经验”花萼
        """
        log.transmitAllLog("命令：进入“角色经验”花萼", output=True)

        if not cls.enter_calyx_gold():
            log.transmitRunLog("没有成功进入花萼")
            return False

        log.transmitRunLog("找角色经验花萼", output=True)
        calyx_characterEXP = ImagePath.CALYX_CHARACTER_EXP
        # 查找经验花萼
        characterEXP_rect = func.find_image(calyx_characterEXP)

        log.transmitRunLog("找传送", output=True)
        transmission = ImagePath.TRANSMISSION
        rects = pyautogui.locateAllOnScreen(transmission, confidence=0.8)
        points = []
        for box in rects:
            points.append((box.left, box.top, box))
        characterEXP_point = (characterEXP_rect.left, characterEXP_rect.top, characterEXP_rect)
        transmission_rect = func.closest_point(points, characterEXP_point)[2]  # 计算哪个传送离经验花萼最近
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True

    @classmethod
    def enter_coneEXP(cls):
        """
        进入”光锥经验“花萼
        """
        pass

    @classmethod
    def enter_credit(cls):
        """
        进入”信用点“花萼
        """
        pass


def use_of_stamina(copies: dict):
    """
    用于清理体力的方法
    :param copies: 保存着各个副本要进行的次数
    copies.keys() = [
    "characterEXP", "coneEXP", "credit", <- calyx(gold)
    ]
    """
    # 字符串转对应方法
    str_to_func = {
        "characterEXP": Calyx.enter_characterEXP,
        "coneEXP": Calyx.enter_coneEXP,
        "credit": Calyx.enter_credit,
    }

    start_game()  # 开启游戏
    func.wait_image(ImagePath.MANDATE)  # 等待进入游戏

    for c, cnt in copies.items():
        method = str_to_func.get(c, None)
        if method is None:
            log.transmitRunLog(f"警告：出现不存在的字符串({c}) [use_of_stamina]", output=True)
            continue
        # 打副本，直到达成目标或出现意外(体力不够等情况)
        while cnt > 0:
            res = method()
            if not res:  # 没有进入副本界面
                log.transmitRunLog(f"警告：没有进入副本界面({c}) []use_of_stamina")
                break

            # 进入副本界面后增加挑战次数，因为默认是1次，所以鼠标点击cnt-1次就行了。
            if cnt > 6:
                func.add_challenge(5)
                cnt -= 6
            else:
                func.add_challenge(cnt - 1)
                cnt = 0

            # 进入挑战
            func.challenge()
            log.transmitAllLog("进入挑战")
            # 开始挑战
            func.start_challenge()
            log.transmitRunLog("开始挑战")
            # 等待挑战完成(阻塞主线程)
            log.transmitRunLog("等待挑战完成")
            check.wait_challenge_completed()
            # 退出副本界面
            func.exit_copies()
            log.transmitAllLog("退出副本")
