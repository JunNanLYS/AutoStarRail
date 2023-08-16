import os

import cv2
import numpy as np

import config

root = config.abspath
pen_size = 2
world_number = 2  # 世界编号
map_name = "big-1-1.png"  # 大地图-地区-坐标点
filename = os.path.join(root, "world", "map", str(world_number), map_name)

# 读取原图
img = cv2.imread(filename)
cv2.namedWindow("image")

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(img_gray, 200, 255, cv2.THRESH_BINARY)
two_val_name = map_name.split('.')[0] + '-two.png'
two_val_filename = os.path.join(root, "world", "map", str(world_number), two_val_name)
cv2.imwrite(two_val_filename, thresh)

# 定义鼠标回调函数
ix, iy = -1, -1
drawing = False


def draw_line(event, x, y, flags, param):
    global ix, iy, drawing

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x, y
        cv2.circle(img, (x, y), pen_size, (255, 0, 0))

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.line(img, (ix, iy), (x, y), (255, 0, 0), pen_size)


# 设置鼠标回调函数
cv2.setMouseCallback('image', draw_line)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        break

cv2.destroyAllWindows()
