from cnocr import CnOcr

import time

import log

cnocr = CnOcr()


def get_text_position(path, target: str):
    """
    获取文字坐标
    """
    res = cnocr.ocr(path)
    for i in range(len(res)):
        d = res[i]
        if target in d['text']:
            return d['position']
    return None


def text_in_img(path, target: str) -> bool:
    """
    判断图片中是否包含文字
    """
    res = cnocr.ocr(path)
    for i in range(len(res)):
        d = res[i]
        if target in d['text']:
            return True
    return False


def wait_text(method, target: str, timeout: int = 60):
    """
    等待某个文字，若超过timeout时间未等到某个文字则抛出错误
    """
    start = time.time()
    while time.time() - start < timeout:
        pos = get_text_position(method(), target)
        if pos is not None:
            return pos
        time.sleep(0.1)
    log.critical("等待超时")
    raise Exception("等待超时")
