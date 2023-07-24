import time
import pyautogui

from utils.path import ImagePath
from utils import func, check
from script.start_game import start_game
from widgets import log
from threadpool import script_thread

"""
                                            副本名称
拟造花萼(金)
characterEXP        角色经验
coneEXP             光锥经验
credit              信用点

拟造花萼(赤)
calyxDestruction    毁灭
calyxPreservation   存护
calyxHunt           巡猎
calyxAbundance      丰饶
calyxErudition      智识
calyxHarmony        和谐
calyxNihility       虚无

凝滞虚影
shapeOfQuanta       空海之形
shapeOfGust         巽风之形
shapeOfFulmination  鸣雷之形
shapeOfBlaze        炎华之形
shapeOfSpike        锋芒之形
shapeOfRime         霜晶之形
shapeOfMirage       幻光之形
shapeOfLcicle       冰凌之形
shapeOfDoom         震厄之形
shapeOfCelestial    天人之形

侵蚀隧洞

历战回响
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


def enter_stagnant_shadow() -> bool:
    """
    进入凝滞虚影
    """
    log.transmitRunLog("命令：进入凝滞虚影")
    shadow = ImagePath.STAGNANT_SHADOW
    rect = func.find_image(shadow, confidence=0.9)
    if rect:
        log.transmitAllLog("找到凝滞虚影按钮")
        pyautogui.moveTo(rect)
        pyautogui.click()
    else:
        log.transmitRunLog("找不到凝滞虚影")
        return False
    time.sleep(1)
    return True


class Calyx:
    """
    拟造花萼
    """
    filename = {"角色经验": ImagePath.CALYX_CHARACTER_EXP,
                "光锥经验": ImagePath.CALYX_CONE_EXP,
                "信用点": ImagePath.CALYX_CREDIT,
                "毁灭": ImagePath.CALYX_DESTRUCTION,
                "存护": ImagePath.CALYX_PRESERVATION,
                "巡猎": ImagePath.CALYX_HUNT,
                "丰饶": ImagePath.CALYX_ABUNDANCE,
                "智识": ImagePath.CALYX_ERUDITION,
                "和谐": ImagePath.CALYX_HARMONY,
                "虚无": ImagePath.CALYX_NIHILITY,
                }

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
        log.transmitAllLog(f"命令：进入{bud_name}花萼")
        if not cls.enter_calyx_gold():
            log.transmitRunLog("没有成功进入金花萼")
            return False

        log.transmitRunLog(f"找{bud_name}图片", output=True)
        transmission_rect = search_transmission(cls.filename[bud_name])
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True

    @classmethod
    def into_bud_of_red_calyx(cls, bud_name: str):
        """
        进入行迹
        """
        log.transmitAllLog(f"命令：进入{bud_name}行迹")
        if not cls.enter_calyx_red():
            log.transmitRunLog("没有成功进入赤花萼")
            return False

        log.transmitRunLog(f"找{bud_name}行迹图片")
        transmission_rect = search_transmission(cls.filename[bud_name])
        # 没找到
        if transmission_rect is None:
            rect = func.find_image(cls.filename["毁灭"])
            pyautogui.moveTo(rect)
            for _ in range(5):
                for _ in range(6):
                    pyautogui.scroll(-10)  # 向下滚动查找
                time.sleep(0.5)
                transmission_rect = search_transmission(cls.filename[bud_name])
                if transmission_rect:
                    break
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


class Shadow:
    """
    凝滞虚影
    """
    filename = {
        "空海之形": ImagePath.SHAPE_OF_QUANTA,
        "巽风之形": ImagePath.SHAPE_OF_GUST,
        "鸣雷之形": ImagePath.SHAPE_OF_FULMINATION,
        "炎华之形": ImagePath.SHAPE_OF_BLAZE,
        "锋芒之形": ImagePath.SHAPE_OF_SPIKE,
        "霜晶之形": ImagePath.SHAPE_OF_RIME,
        "幻光之形": ImagePath.SHAPE_OF_MIRAGE,
        "冰凌之形": ImagePath.SHAPE_OF_LCICLE,
        "震厄之形": ImagePath.SHAPE_OF_DOOM,
        "天人之形": ImagePath.SHAPE_OF_CELESTIAL,
    }

    @classmethod
    def enter_stagnant_shadow(cls):
        """
        进入凝滞虚影
        """
        if not enter_book():  # 进入”星际和平书“界面
            return False
        if not enter_index():  # 进入“生存索引”界面
            return False
        if not enter_stagnant_shadow():  # 凝滞虚影
            return False
        return True

    @classmethod
    def into_shadow(cls, shape_name: str):
        log.transmitAllLog(f"命令：进入{shape_name}-凝滞虚影")
        if not cls.enter_stagnant_shadow():
            log.transmitRunLog("没有成功进入凝滞虚影界面")
            return False
        log.transmitRunLog(f"找{shape_name}-凝滞虚影图片")
        transmission_rect = search_transmission(cls.filename[shape_name])

        # 没找到
        if transmission_rect is None:
            rect = func.find_image(cls.filename["空海之形"])
            pyautogui.moveTo(rect)  # 鼠标移动到凝滞虚影内
            for _ in range(10):
                for _ in range(6):
                    pyautogui.scroll(-10)  # 向下滚动查找
                time.sleep(0.5)
                transmission_rect = search_transmission(cls.filename[shape_name])
                if transmission_rect:
                    break

        # 进入凝滞虚影
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


# 字符串转对应回调函数和参数
STRING_TO_CALLBACK = {
    "characterEXP": (Calyx.into_bud_of_gold_calyx, ("角色经验",)),
    "coneEXP": (Calyx.into_bud_of_gold_calyx, ("光锥经验",)),
    "credit": (Calyx.into_bud_of_gold_calyx, ("信用点",)),
    "calyxDestruction": (Calyx.into_bud_of_red_calyx, ("毁灭",)),
    "calyxPreservation": (Calyx.into_bud_of_red_calyx, ("存护",)),
    "calyxHunt": (Calyx.into_bud_of_red_calyx, ("巡猎",)),
    "calyxAbundance": (Calyx.into_bud_of_red_calyx, ("丰饶",)),
    "calyxErudition": (Calyx.into_bud_of_red_calyx, ("智识",)),
    "calyxHarmony": (Calyx.into_bud_of_red_calyx, ("和谐",)),
    "calyxNihility": (Calyx.into_bud_of_red_calyx, ("虚无",)),
    "shapeOfQuanta": (Shadow.into_shadow, ("空海之形",)),
    "shapeOfGust": (Shadow.into_shadow, ("巽风之形",)),
    "shapeOfFulmination": (Shadow.into_shadow, ("鸣雷之形",)),
    "shapeOfBlaze": (Shadow.into_shadow, ("炎华之形",)),
    "shapeOfSpike": (Shadow.into_shadow, ("锋芒之形",)),
    "shapeOfRime": (Shadow.into_shadow, ("霜晶之形",)),
    "shapeOfMirage": (Shadow.into_shadow, ("幻光之形",)),
    "shapeOfLcicle": (Shadow.into_shadow, ("冰凌之形",)),
    "shapeOfDoom": (Shadow.into_shadow, ("震厄之形",)),
    "shapeOfCelestial": (Shadow.into_shadow, ("天人之形",)),
}


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
        method, parameter = STRING_TO_CALLBACK.get(c, None)
        if method is None:
            log.transmitRunLog(f"警告：出现不存在的字符串({c}) [use_of_stamina]", output=True)
            continue
        # 打副本，直到达成目标或出现意外(体力不够等情况)
        while cnt > 0:
            res = method(*parameter)
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
                pyautogui.keyDown('w')
                time.sleep(1)
                pyautogui.keyUp('w')
                pyautogui.click()
            # 等待挑战完成(阻塞主线程)
            log.transmitRunLog("等待挑战完成")
            check.wait_challenge_completed()
            # 退出副本界面
            func.exit_copies()
            log.transmitAllLog("退出副本")

