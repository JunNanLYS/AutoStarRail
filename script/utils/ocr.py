import time

from ppocronnx import TextSystem
from numpy import ndarray, array

import log

text_sys = TextSystem(use_angle_cls=False)


def get_text_position(img: ndarray, target: str) -> ndarray:
    """
    获取文字坐标，没有查询到文字则返回空数组
    """
    res = text_sys.detect_and_ocr(img)
    val = 0
    pos = None
    for i in range(len(res)):
        box = res[i]
        if box.ocr_text == target:
            if box.score > val:
                val = box.score
                pos = box.box
    if pos is not None:
        return pos

    for i in range(len(res)):
        box = res[i]
        if target in box.ocr_text:
            if box.score > val:
                val = box.score
                pos = box.box
    if pos is not None:
        return pos
    return array([])


def text_in_img(img: ndarray, target: str) -> bool:
    """
    判断图片中是否包含文字
    """
    res = get_text_position(img, target)
    if res.size == 0:
        return False
    return True


def wait_text(method, target: str, timeout: int = 60):
    """
    :param method: 获取屏幕截图的方法，这个方法返回的必须是ndarray
    :param target: 目标文字
    :param timeout: 最长等待时长
    等待某个文字，若超过timeout时间未等到某个文字则抛出错误
    """
    start = time.time()
    while time.time() - start < timeout:
        pos = get_text_position(method(), target)
        if pos.size != 0:
            return pos
        time.sleep(2)
    log.critical("等待超时")
    raise Exception("等待超时")
