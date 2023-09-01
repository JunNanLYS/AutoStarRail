from cnocr import CnOcr

from widgets import log

cnocr = CnOcr()


def get_text_position(path, target: str):
    """
    获取文字坐标
    """
    log.transmitRunLog("OCR判断中，需要3秒左右请耐心等待")
    res = cnocr.ocr(path)
    for i in range(len(res)):
        d = res[i]
        if target in d['text']:
            return d['position']
    log.transmitDebugLog(f"{target}查找失败")
    return None
