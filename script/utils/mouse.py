def click_position(position):
    """鼠标移动至position并点击"""
    import win32api
    import win32con
    import time
    x, y = int(position[0]), int(position[1])
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.1)  # 过快的点击将导致游戏反应不过来最终导致点击失效
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def click_positions(positions):
    """
    传入单个值则点击该值，多个值则取索引为 元素个数/2 的坐标
    """
    length = len(positions)
    mid = length // 2 - 1
    if mid < 0:
        mid = 0
    pos = positions[mid]
    x, y = int(pos[0]), int(pos[1])
    click_position((x, y))


def mouse_scroll(count: int):
    """
    鼠标滚轮
    """
    import pyautogui
    for _ in range(count):
        for _ in range(6):
            pyautogui.scroll(-10)
