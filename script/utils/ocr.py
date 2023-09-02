from cnocr import CnOcr

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
