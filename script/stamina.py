import time

import pyautogui

from utils import func
from utils.path import ImagePath
from widgets import log


class Copies:
    CALYX = "calyx"  # 拟造花萼
    CALYX_GOLD = "calyx_gold"  # 拟造花萼（金）
    CALYX_RED = "calyx_red"  # 拟造花萼（赤）
    STAGNANT_SHADOW = "stagnant_shadow"  # 凝滞虚影
    CAVERN_OF_CORROSION = "cavern_of_corrosion"  # 侵蚀隧道
    ECHO_OF_WAR = "echo_of_war"  # 历战余响


def search_transmission(image_path):
    """
    找image_path对应的传送按钮
    """
    image_rect = func.find_image(image_path)
    if not image_rect:
        return None
    log.transmitRunLog("找传送")
    transmission = ImagePath.TRANSMISSION
    rects = pyautogui.locateAllOnScreen(transmission, confidence=0.9)
    points = []
    for box in rects:
        points.append((box.left, box.top, box))
    point = (image_rect.left, image_rect.top, image_rect)
    transmission_rect = func.closest_point(points, point)[2]  # 计算哪个传送离经验花萼最近
    return transmission_rect


def mouse_scroll(count: int):
    """
    鼠标滚轮
    """
    for _ in range(count):
        for _ in range(6):
            pyautogui.scroll(-10)


def mouse_scroll_search(move_to: str, target: str, cnt=10):
    """
    滚动鼠标滚轮搜索
    """
    log.transmitRunLog("---正在使用滚轮查找---")
    rect = func.find_image(move_to)
    pyautogui.moveTo(rect)
    for _ in range(cnt):
        for _ in range(6):
            pyautogui.scroll(-10)  # 向下滚动查找
        time.sleep(0.5)
        transmission_rect = search_transmission(target)
        if transmission_rect:
            return transmission_rect


def enter_book() -> bool:
    """
    进入星际和平指南界面
    """
    log.transmitRunLog("命令：进入星际和平书")
    book = ImagePath.BOOK
    box = func.find_image(book)
    if box:
        log.transmitRunLog("找到书")
        time.sleep(1)
        pyautogui.keyDown('alt')
        pyautogui.moveTo(box)
        pyautogui.click()  # 进入星际和平书界面
        pyautogui.keyUp('alt')
    else:
        log.transmitAllLog("没找到书")
        # 可能是已经在书界面了
        return False
    time.sleep(1)
    return True


def enter_index() -> bool:
    """
    进入生存索引界面
    """
    log.transmitRunLog("命令：进入生存索引")
    index = ImagePath.INDEX
    index_selected = ImagePath.INDEX_SELECTED
    index_box = func.find_image(index, max_count=1)

    if index_box:
        log.transmitRunLog("找到生存索引")
        # 进入生存索引
        pyautogui.moveTo(index_box)
        pyautogui.click()
    elif pos := func.find_image(index_selected):
        log.transmitRunLog("检测到生存索引已被选择")
        pyautogui.moveTo(pos)
    else:
        log.transmitRunLog("没找到生存索引")
        return False
    time.sleep(1)
    return True


def click_copies_button(copies_name: str) -> bool:
    """
    点击副本按钮
    """
    EN_TO_CN = {
        Copies.CALYX_GOLD: "拟造花萼(金)",
        Copies.CALYX_RED: "拟造花萼(赤)",
        Copies.STAGNANT_SHADOW: "凝滞虚影",
        Copies.CAVERN_OF_CORROSION: "侵蚀隧道",
        Copies.ECHO_OF_WAR: "历战余响"
    }
    NAME_TO_IMAGE = {
        Copies.CALYX_GOLD: ImagePath.CALYX_GOLD,
        Copies.CALYX_RED: ImagePath.CALYX_RED,
        Copies.STAGNANT_SHADOW: ImagePath.STAGNANT_SHADOW,
        Copies.CAVERN_OF_CORROSION: ImagePath.CAVERN_OF_CORROSION,
        Copies.ECHO_OF_WAR: ImagePath.ECHO_OF_WAR
    }
    if copies_name == Copies.ECHO_OF_WAR:
        pyautogui.moveTo(func.find_image(ImagePath.CALYX_GOLD))
        mouse_scroll(3)
    log.transmitRunLog(f"命令：进入{EN_TO_CN[copies_name]}")
    image = NAME_TO_IMAGE[copies_name]
    rect = func.find_image(image)
    if rect:
        log.transmitAllLog(f"找到{EN_TO_CN[copies_name]}")
        pyautogui.moveTo(rect)
        pyautogui.click()
    else:
        log.transmitRunLog("找不到目标")
        return False
    time.sleep(1)
    return True


class Calyx:
    """
    拟造花萼
    """
    filename = {1: ImagePath.CALYX_1,
                2: ImagePath.CALYX_2,
                3: ImagePath.CALYX_3,
                4: ImagePath.CALYX_4,
                5: ImagePath.CALYX_5,
                6: ImagePath.CALYX_6,
                7: ImagePath.CALYX_7,
                8: ImagePath.CALYX_8,
                9: ImagePath.CALYX_9,
                10: ImagePath.CALYX_10,
                }

    @classmethod
    def enter_calyx(cls, calyx_name):
        """
        进入花萼界面
        """
        # 有时太快鼠标操作不过来，可以循环3次来避免这种问题
        for _ in range(3):
            if not enter_book():  # 进入星际和平指南
                continue
            if not enter_index():  # 进入生存索引
                continue
            if not click_copies_button(calyx_name):  # 进入花萼
                continue
            return True  # 只有执行到这一行才能返回true
        return False

    @classmethod
    def start(cls, calyx_name: int):
        log.transmitAllLog(f"命令：进入花萼")
        calyx_color = Copies.CALYX_GOLD if calyx_name <= 3 else Copies.CALYX_RED
        if not cls.enter_calyx(calyx_color):
            log.transmitRunLog("没有成功进入金花萼")
            return False

        log.transmitRunLog(f"找图片")
        transmission_rect = search_transmission(cls.filename[calyx_name])
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


class Shadow:
    """
    凝滞虚影
    """
    filename = {
        1: ImagePath.SHAPE_1,
        2: ImagePath.SHAPE_2,
        3: ImagePath.SHAPE_3,
        4: ImagePath.SHAPE_4,
        5: ImagePath.SHAPE_5,
        6: ImagePath.SHAPE_6,
        7: ImagePath.SHAPE_7,
        8: ImagePath.SHAPE_8,
        9: ImagePath.SHAPE_9,
        10: ImagePath.SHAPE_10,
    }

    @classmethod
    def enter_stagnant_shadow(cls):
        """
        进入凝滞虚影
        """
        # 有时太快鼠标操作不过来，可以循环3次来避免这种问题
        for _ in range(3):
            if not enter_book():  # 进入星际和平指南
                continue
            if not enter_index():  # 进入生存索引
                continue
            if not click_copies_button(Copies.STAGNANT_SHADOW):  # 进入凝滞虚影
                continue
            return True  # 只有执行到这一行才能返回true
        return False

    @classmethod
    def start(cls, shape_name: int):
        log.transmitAllLog(f"命令：进入凝滞虚影")
        if not cls.enter_stagnant_shadow():
            log.transmitRunLog("没有成功进入凝滞虚影界面")
            return False
        log.transmitRunLog(f"找凝滞虚影图片")
        transmission_rect = search_transmission(cls.filename[shape_name])

        # 没找到
        if transmission_rect is None:
            transmission_rect = mouse_scroll_search(cls.filename[1], cls.filename[shape_name])

        # 进入凝滞虚影
        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


class Cavern:
    """
    侵蚀隧道(遗器本)
    """
    filename = {
        1: ImagePath.CAVERN_1,
        2: ImagePath.CAVERN_2,
        3: ImagePath.CAVERN_3,
        4: ImagePath.CAVERN_4,
        5: ImagePath.CAVERN_5,
        6: ImagePath.CAVERN_6,
        7: ImagePath.CAVERN_7,
    }

    @classmethod
    def enter_cavern(cls):
        # 有时太快鼠标操作不过来，可以循环3次来避免这种问题
        for _ in range(3):
            if not enter_book():  # 进入星际和平指南
                continue
            if not enter_index():  # 进入生存索引
                continue
            if not click_copies_button(Copies.CAVERN_OF_CORROSION):  # 进入侵蚀隧道
                continue
            return True  # 只有执行到这一行才能返回true
        return False

    @classmethod
    def start(cls, cavern_number: int):
        log.transmitAllLog("进入侵蚀遗器副本")
        if not cls.enter_cavern():
            log.transmitAllLog("没有成功进入侵蚀遗器副本界面")
            return False
        transmission_rect = search_transmission(cls.filename[cavern_number])

        if transmission_rect is None:
            transmission_rect = mouse_scroll_search(cls.filename[1], cls.filename[cavern_number])

        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


class Echo:
    """
    历战回响
    """
    filename = {
        1: ImagePath.ECHO_1,
        2: ImagePath.ECHO_2,
        3: ImagePath.ECHO_3,
    }

    @classmethod
    def enter_echo(cls):
        # 有时太快鼠标操作不过来，可以循环3次来避免这种问题
        for _ in range(3):
            if not enter_book():  # 进入星际和平指南
                continue
            if not enter_index():  # 进入生存索引
                continue
            if not click_copies_button(Copies.ECHO_OF_WAR):  # 进入历战余响
                continue
            return True  # 只有执行到这一行才能返回true
        return False

    @classmethod
    def start(cls, echo_number: int):
        log.transmitAllLog("进入历战余响副本")
        if not cls.enter_echo():
            log.transmitAllLog("没有成功进入历战余响副本界面")
            return False
        transmission_rect = search_transmission(cls.filename[echo_number])

        if transmission_rect is None:
            transmission_rect = mouse_scroll_search(cls.filename[1], cls.filename[echo_number])

        pyautogui.moveTo(transmission_rect)
        pyautogui.click()
        time.sleep(2)
        return True


class Stamina:
    copies_cls = {
        Copies.CALYX: Calyx,
        Copies.STAGNANT_SHADOW: Shadow,
        Copies.CAVERN_OF_CORROSION: Cavern,
        Copies.ECHO_OF_WAR: Echo,
    }

    @classmethod
    def use(cls, copies_name: str, number: int):
        """
        copies_name: [calyx, shadow, cavern, echo]  副本名称
        number: 1,2,3,4....                         副本编号
        """
        call = cls.copies_cls[copies_name]
        return call.start(number)


"""
---拟造花萼---
角色经验           1
光锥经验           2
信用点             3
毁灭              4


---凝滞虚影---
空海之形    1
巽风之形    2
鸣雷之形    3
炎华之形    4
锋芒之形    5
霜晶之形    6
幻光之形    7
冰凌之形    8
震厄之形    9
天人之形    10

---侵蚀隧道---
...

---历战余响---
毁灭  1
存护  2
丰饶  3
"""
# 字符串转对应回调函数和参数
STRING_TO_CALLBACK = {
    "calyx_1": (Stamina.use, (Copies.CALYX, 1)),
    "calyx_2": (Stamina.use, (Copies.CALYX, 2)),
    "calyx_3": (Stamina.use, (Copies.CALYX, 3)),
    "calyx_4": (Stamina.use, (Copies.CALYX, 4)),
    "calyx_5": (Stamina.use, (Copies.CALYX, 5)),
    "calyx_6": (Stamina.use, (Copies.CALYX, 6)),
    "calyx_7": (Stamina.use, (Copies.CALYX, 7)),
    "calyx_8": (Stamina.use, (Copies.CALYX, 8)),
    "calyx_9": (Stamina.use, (Copies.CALYX, 9)),
    "calyx_10": (Stamina.use, (Copies.CALYX, 10)),
    "shadow_1": (Stamina.use, (Copies.STAGNANT_SHADOW, 1)),
    "shadow_2": (Stamina.use, (Copies.STAGNANT_SHADOW, 2)),
    "shadow_3": (Stamina.use, (Copies.STAGNANT_SHADOW, 3)),
    "shadow_4": (Stamina.use, (Copies.STAGNANT_SHADOW, 4)),
    "shadow_5": (Stamina.use, (Copies.STAGNANT_SHADOW, 5)),
    "shadow_6": (Stamina.use, (Copies.STAGNANT_SHADOW, 6)),
    "shadow_7": (Stamina.use, (Copies.STAGNANT_SHADOW, 7)),
    "shadow_8": (Stamina.use, (Copies.STAGNANT_SHADOW, 8)),
    "shadow_9": (Stamina.use, (Copies.STAGNANT_SHADOW, 9)),
    "shadow_10": (Stamina.use, (Copies.STAGNANT_SHADOW, 10)),
    "cavern_1": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 1)),
    "cavern_2": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 2)),
    "cavern_3": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 3)),
    "cavern_4": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 4)),
    "cavern_5": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 5)),
    "cavern_6": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 6)),
    "cavern_7": (Stamina.use, (Copies.CAVERN_OF_CORROSION, 7)),
    "echo_1": (Stamina.use, (Copies.ECHO_OF_WAR, 1)),
    "echo_2": (Stamina.use, (Copies.ECHO_OF_WAR, 2)),
    "echo_3": (Stamina.use, (Copies.ECHO_OF_WAR, 3)),
}

if __name__ == '__main__':
    call, param = STRING_TO_CALLBACK['shadow_3']
    call(*param)
