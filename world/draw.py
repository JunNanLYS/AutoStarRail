import os
from copy import deepcopy
from math import atan

import cv2

import config


def get_big_map(world, name):
    filename = os.path.join(
        root,
        r"world\map",
        str(world),
        name
    )
    image = cv2.imread(os.path.join(filename, 'default.png'))
    return image


# 初始化
root = config.abspath
pen_size = 1  # 画笔大小
world_number = 2  # 世界编号
map_name = "1-1"  # 地区-传送点编号

# 读取原图
img = get_big_map(world_number, map_name)

cv2.namedWindow("image")

# 定义鼠标回调函数
ix, iy = 0, 0
drawing = False
is_first = True
color = (0, 0, 255)
blue = (255, 0, 0)


def is45angle(pos1, pos2):
    x, y = pos2[0] - pos1[0], -(pos2[1] - pos1[1])
    angle = int(abs(atan(y / x)) * (180 / 3.1415926535))
    return angle == 45


def draw_line(event, x, y, flags, param):
    global ix, iy, drawing, is_first

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (x, y), 0, color)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), (x, y), color, pen_size)
        if is_first:
            cv2.circle(img, (ix, iy), 0, (0, 255, 0))
            is_first = False

    elif event == cv2.EVENT_MOUSEMOVE:
        copy_img = deepcopy(img)
        if x == ix or y == iy:
            use_color = color
        elif is45angle((ix, iy), (x, y)):
            use_color = color
        else:
            use_color = blue
        cv2.line(copy_img, (ix, iy), (x, y), use_color, pen_size)
        cv2.imshow("preview", copy_img)
        cv2.moveWindow("preview", 0, 0)


# 设置鼠标回调函数
cv2.setMouseCallback('image', draw_line)

while True:
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
cv2.imwrite(os.path.join(
    root,
    r"world\map",
    str(world_number),
    map_name,
    "road.png"), img)
