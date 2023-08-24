POINT = (100, 100)      # 原点
ONE_45 = (110, 90)      # 第一象限45度
TWO_45 = (90, 90)       # 第二象限45度
THREE_45 = (90, 110)    # 第三象限45度
FOUR_45 = (110, 110)    # 第四象限45度
UP_Y = (100, 90)        # 正Y
DOWN_Y = (100, 110)     # 负Y
LEFT_X = (90, 100)      # 正X
RIGHT_X = (110, 100)    # 负X

# (原点, 目标位置, 应该返回的角度)
TEST_DATA = [
    (POINT, ONE_45, 315),
    (POINT, TWO_45, 45),
    (POINT, THREE_45, 135),
    (POINT, FOUR_45, 225),
    (POINT, UP_Y, 0),
    (POINT, DOWN_Y, 180),
    (POINT, LEFT_X, 90),
    (POINT, RIGHT_X, 270)
]