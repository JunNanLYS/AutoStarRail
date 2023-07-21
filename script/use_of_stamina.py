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


def search_transmission(image_path):
    """
    找image_path对应的传送按钮
    """
    image_rect = func.find_image(image_path)
    if not image_rect:
        return None
    log.transmitRunLog("找传送", output=True)
    transmission = ImagePath.TRANSMISSION
    rects = pyautogui.locateAllOnScreen(transmission, confidence=0.9)
    points = []
    for box in rects:
        points.append((box.left, box.top, box))
    point = (image_rect.left, image_rect.top, image_rect)
    transmission_rect = func.closest_point(points, point)[2]  # 计算哪个传送离经验花萼最近
    return transmission_rect


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
    log.transmitRunLog("命令：进入生存索引", output=True)
    index = ImagePath.INDEX
    index_selected = ImagePath.INDEX_SELECTED
    index_box = func.find_image(index)

    if index_box:
        log.transmitRunLog("找到生存索引", output=True)
        # 进入生存索引
        pyautogui.moveTo(index_box)
        pyautogui.click()
    elif pos := func.find_image(index_selected):
        log.transmitRunLog("检测到生存索引已被选择", output=True)
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
    log.transmitRunLog("命令：进入花萼(金)", output=True)
    calyx = ImagePath.CALYX_GOLD
    box = func.find_image(calyx)
    if box:
        log.transmitAllLog("找到花萼", output=True)
        pyautogui.moveTo(box)
        pyautogui.click()
    # 花萼已经被选中
    elif func.find_image(ImagePath.CALYX_GOLD_SELECTED):
        log.transmitRunLog("检测到花萼已被选中", output=True)
    else:
        log.transmitRunLog("找不到花萼", output=True)
        return False
    time.sleep(1)
    return True


def enter_calyx_red() -> bool:
    """
    进入花萼(赤)
    """
    log.transmitRunLog("命令：进入赤花萼")
    calyx = ImagePath.CALYX_RED
    rect = func.find_image(calyx, confidence=0.9)
    if rect:
        log.transmitAllLog("找到花萼", output=True)
        pyautogui.moveTo(rect)
        pyautogui.click()
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
        if not enter_book():
            return False
        if not enter_index():
            return False
        if not enter_calyx_red():
            return False
        return True

    @classmethod
    def into_bud_of_gold_calyx(cls, bud_name: str):
        name = {"角色经验": ImagePath.CALYX_CHARACTER_EXP,
                "光锥经验": ImagePath.CALYX_CONE_EXP,
                "信用点": ImagePath.CALYX_CREDIT}
        log.transmitAllLog(f"命令：进入{bud_name}花萼")
        if not cls.enter_calyx_gold():
            log.transmitRunLog("没有成功进入金花萼")
            return False

        log.transmitRunLog(f"找{bud_name}图片", output=True)
        transmission_rect = search_transmission(name[bud_name])
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True

    @classmethod
    def into_bud_of_red_calyx(cls, bud_name: str):
        """
        进入行迹
        """
        name = {"毁灭": ImagePath.CALYX_DESTRUCTION,
                "存护": ImagePath.CALYX_PRESERVATION,
                "巡猎": ImagePath.CALYX_HUNT,
                "丰饶": ImagePath.CALYX_ABUNDANCE,
                "智识": ImagePath.CALYX_ERUDITION,
                "和谐": ImagePath.CALYX_HARMONY,
                "虚无": ImagePath.CALYX_NIHILITY}
        log.transmitAllLog(f"命令：进入{bud_name}行迹")
        if not cls.enter_calyx_red():
            log.transmitRunLog("没有成功进入赤花萼")
            return False

        log.transmitRunLog(f"找{bud_name}行迹图片")
        transmission_rect = search_transmission(name[bud_name])
        # 没找到
        if transmission_rect is None:
            rect = func.find_image(name["毁灭"])
            pyautogui.moveTo(rect)
            for _ in range(5):
                for _ in range(6):
                    pyautogui.scroll(-10)  # 向下滚动查找
                time.sleep(0.5)
                transmission_rect = search_transmission(name[bud_name])
                if transmission_rect:
                    break
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


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
        "characterEXP": (Calyx.into_bud_of_gold_calyx, "角色经验"),
        "coneEXP": (Calyx.into_bud_of_gold_calyx, "光锥经验"),
        "credit": (Calyx.into_bud_of_gold_calyx, "信用点"),
        "calyxDestruction": (Calyx.into_bud_of_red_calyx, "毁灭"),
        "calyxPreservation": (Calyx.into_bud_of_red_calyx, "存护"),
        "calyxHunt": (Calyx.into_bud_of_red_calyx, "巡猎"),
        "calyxAbundance": (Calyx.into_bud_of_red_calyx, "丰饶"),
        "calyxErudition": (Calyx.into_bud_of_red_calyx, "智识"),
        "calyxHarmony": (Calyx.into_bud_of_red_calyx,  "和谐"),
        "calyxNihility": (Calyx.into_bud_of_red_calyx, "虚无"),
    }

    start_game()  # 开启游戏
    func.wait_image(ImagePath.MANDATE)  # 等待进入游戏

    for c, cnt in copies.items():
        method, parameter = str_to_func.get(c, None)
        if method is None:
            log.transmitRunLog(f"警告：出现不存在的字符串({c}) [use_of_stamina]", output=True)
            continue
        # 打副本，直到达成目标或出现意外(体力不够等情况)
        while cnt > 0:
            res = method(parameter)
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


