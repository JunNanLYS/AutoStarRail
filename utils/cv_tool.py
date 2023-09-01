from copy import deepcopy
from typing import Union, List

import cv2
import numpy as np
from numpy import ndarray


def is_same_position(position1: tuple, position2: tuple, error_value: int):
    """
    传入两个坐标位置，判断这两个位置是否是同一个位置
    :param position1: 点1
    :param position2: 点2
    :param error_value: 误差值
    """
    for add_x in range(-error_value, error_value + 1):
        for add_y in range(-error_value, error_value + 1):
            if position1 == (position2[0] + add_x, position2[1] + add_y):
                return True
    return False


def remove_same_position(positions: list, error_value: int):
    flag = set()  # 记录需要被删除的下标
    cur = 0
    while cur < len(positions) - 1:
        nex = cur + 1
        while nex < len(positions):
            # 跳过被标记的下标
            if nex in flag:
                nex += 1
                continue
            # 判断是否是同一个点
            if is_same_position(positions[cur], positions[nex], error_value):
                flag.add(nex)
            nex += 1
        cur += 1
        # 跳过被标记的下标
        while cur in flag:
            cur += 1
    return [position for i, position in enumerate(positions) if i not in flag]


def rotate_image(image, angle):
    """
    旋转图片
    :param image: 需要旋转的图像
    :param angle: 旋转角度
    """
    h, w = image.shape[:2]
    matrix = cv2.getRotationMatrix2D((w // 2, h // 2), angle, 1.0)  # 获取旋转矩阵
    rotated_image = cv2.warpAffine(image, matrix, (w, h))  # 获取旋转后的图像
    return rotated_image


def in_range_color(image, lower_color: list, upper_color: list):
    """
    保留图像中颜色范围内的颜色，方法内自带深拷贝，不会污染原图像
    :param image: 图像
    :param lower_color: 下限
    :param upper_color: 上限
    :return: image
    """
    img = deepcopy(image)
    lower_color = np.array(lower_color)
    upper_color = np.array(upper_color)
    img[np.sum(img - lower_color, axis=-1) < 0] = [0, 0, 0]
    img[np.sum(img - upper_color, axis=-1) > 0] = [0, 0, 0]
    return img


def to_ndarray(img: Union[str, ndarray]) -> ndarray:
    """
    将图片装换为numpy.ndarray
    """
    if isinstance(img, str):
        img = cv2.imread(img)
    return img


def template_in_img(img: Union[str, ndarray], template: Union[str, ndarray], threshold=0.8) -> bool:
    """
    判断模板图是否在img中
    """
    img = to_ndarray(img)
    template = to_ndarray(template)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)
    return max_val >= threshold


def match_template(img: Union[str, ndarray], template: Union[str, ndarray], threshold=0.8) -> tuple:
    """
    模板匹配，匹配成功返回模板图左上角坐标，失败返回(-1, -1)
    """
    img = to_ndarray(img)
    template = to_ndarray(template)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    if max_val >= threshold:
        return max_loc
    return -1, -1


def match_template_gray(img: Union[str, ndarray], template: Union[str, ndarray], threshold=0.8):
    """
    模板匹配(灰),匹配成功返回模板左上角坐标，失败返回(-1, -1)
    """
    img = to_ndarray(img)
    template = to_ndarray(template)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    if max_val >= threshold:
        return max_loc
    return -1, -1


if __name__ == '__main__':
    pass
