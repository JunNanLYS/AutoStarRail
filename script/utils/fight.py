import time
from multiprocessing import Lock, Value, Process
from typing import Optional

import cv2
import pyautogui
from numpy import ndarray

__image: Optional[ndarray] = None
__process: Optional[Process] = None
__fighting = Value('b', False)
__stop = Value('b', True)
__close = Value('b', False)
__fighting_lock = Lock()
__stop_lock = Lock()


def fire() -> None:
    """游戏角色开火（主界面）"""
    s = time.time()
    while time.time() - s <= 1:
        pyautogui.click()
        time.sleep(0.2)
    time.sleep(0.5)


def have_jar() -> bool:
    """
    查找是否有锁定罐子
    """
    from script.utils import in_range_color, template_in_img, template_path
    img = in_range_color(__image, [255, 255, 240], [255, 255, 255])
    template = cv2.imread(template_path.SELECT_JAR)
    return template_in_img(img, template, threshold=0.7)


def have_monster() -> bool:
    """
    1. 查找问号
    2. 查找感叹号
    3. 查找锁定敌人标志(暂时还没办法解决)
    """
    from script.utils import template_in_img, template_path
    template1 = cv2.imread(template_path.QUESTION_MASK)
    template2 = cv2.imread(template_path.WARNING)
    res1 = template_in_img(__image, template1)
    res2 = template_in_img(__image, template2)
    if res1 or res2:
        return True
    return False


def in_fighting() -> bool:
    """
    匹配未开启的自动战斗模板图
    匹配3种不同的自动战斗模板图
    匹配不到前自动战斗模板则匹配手机模板
    """
    from script.utils import template_in_img, match_template_gray, template_path
    templates = [template_path.AUTO_FIGHT, template_path.AUTO_FIGHT_2,
                 template_path.AUTO_FIGHT_3, template_path.AUTO_FIGHT_4]
    for template in templates:
        if template_in_img(__image, template):
            return True
    res = match_template_gray(__image, template_path.PHONE)
    if res == (-1, -1):
        return True
    return False


def is_fighting() -> bool:
    """返回是否在战斗"""
    with __fighting_lock:
        res = __fighting.value
    return bool(res)


def update_img() -> None:
    """
    更新游戏图像
    """
    import game
    global __image
    __image = game.get_screenshot()


def main(_stop: Value, _stop_lock: Lock, _fighting: Value, _fighting_lock: Lock, _close: Value) -> None:
    while not _close.value:
        with _stop_lock:
            c_stop = _stop.value
        # 暂停
        if c_stop:
            time.sleep(1)
            continue
        # 更新游戏截图
        update_img()
        if in_fighting():
            with _fighting_lock:
                _fighting.value = True
                time.sleep(1)
                continue
        elif have_jar():
            fire()
        elif have_monster():
            fire()


def start() -> None:
    """开启战斗模块"""
    import log
    # 已创建子进程则无需再创建
    global __process
    if __process:
        with __stop_lock:
            __stop.value = False
        log.info("开启战斗模块")
    else:
        log.info("创建子进程")
        __stop.value = False
        __process = Process(target=main, args=(__stop, __stop_lock, __fighting, __fighting_lock, __close))
        __process.start()


def stop() -> None:
    """暂停战斗模块"""
    import log
    if __process:
        with __stop_lock:
            __stop.value = True
        log.info("暂停战斗模块")
    else:
        raise Exception("未创建子进程")


def close() -> None:
    """关闭战斗模块"""
    import log
    global __process
    if __process:
        # 防止内存泄漏或者僵尸进程
        log.info("尝试关闭子进程")
        __close.value = True
        __process.join()
        __process = None
        __close.value = False
        log.info("子进程已关闭")
        log.info("关闭战斗模块")
    else:
        raise Exception("未创建子进程")


if __name__ == '__main__':
    # 开启子进程
    start()
    stop()
    print(__stop.value)
    time.sleep(2)
    start()
    time.sleep(5)
    close()
    time.sleep(1)
