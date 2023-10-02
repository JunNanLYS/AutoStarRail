import pyautogui

import log


def click_position(position, direction=None, val=0):
    """
    鼠标移动至position并点击
    direction: [topLeft, topRight, bottomLeft, bottomRight]
    """
    import win32api
    import win32con
    import time
    x, y = int(position[0]), int(position[1])
    if direction == 'topLeft':
        x -= val
        y -= val
    elif direction == 'topRight':
        x += val
        y -= val
    elif direction == 'bottomLeft':
        x -= val
        y += val
    elif direction == 'bottomRight':
        x += val
        y += val
    win32api.SetCursorPos((x, y))
    log.info(f"点击({x},{y})")
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.15)  # 过快的点击将导致游戏反应不过来最终导致点击失效
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_positions(positions, direction=None, val=0):
    """
    传入单个值则点击该值，多个值则取索引为 元素个数/2 的坐标
    direction: [topLeft, topRight, bottomLeft, bottomRight]
    """
    length = len(positions)
    mid = length // 2 - 1
    if mid < 0:
        mid = 0
    pos = positions[mid]
    x, y = int(pos[0]), int(pos[1])
    click_position((x, y), direction=direction, val=val)


def mouse_scroll(count: int):
    """
    鼠标滚轮
    """
    import pyautogui
    log.info("鼠标滚轮滚动")
    for _ in range(count):
        for _ in range(6):
            pyautogui.scroll(-10)


def down_move(start: tuple, end: tuple, button='left'):
    x1, y1 = start[0], start[1]
    x2, y2 = end[0], end[1]
    pyautogui.mouseDown(x1, y1, button)
    pyautogui.moveTo(x2, y2, duration=1)
    pyautogui.mouseUp(x1, y1)
