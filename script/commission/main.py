import time

import cv2
import numpy as np
import pyautogui

import log
import game
from script.commission.data import TITLE_COUNT
from script.utils import (get_text_position, wait_text, window, mouse, template_path, cv_utils, win_message,
                          wait_img, match_template)


class Commission:
    message = False

    @classmethod
    def to_commission(cls):
        log.debug("尝试打开委托界面")
        pyautogui.press("esc")
        pos = wait_text(window.get_screenshot, "委托")
        mouse.click_positions(pos)
        wait_img(template_path.IS_COMMISSION)

    @classmethod
    def get_pending_point(cls) -> list:
        """
        查找所有感叹号的位置
        """
        screenshot = window.get_screenshot()
        template = cv2.imread(template_path.PENDING)
        h, w, _ = template.shape  # 获取模板图宽和高

        # 转HSV
        screenshot_hsv = cv2.cvtColor(screenshot, cv2.COLOR_BGR2HSV)
        template_hsv = cv2.cvtColor(template, cv2.COLOR_BGR2HSV)

        lower = np.array([0, 0, 63])
        upper = np.array([2, 255, 255])

        mask1 = cv2.inRange(screenshot_hsv, lower, upper)
        mask2 = cv2.inRange(template_hsv, lower, upper)

        screenshot = cv2.bitwise_and(screenshot, screenshot, mask=mask1)
        template = cv2.bitwise_and(template, template, mask=mask2)

        result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)

        # 设定阈值
        threshold = 0.85

        # 找到所有匹配位置
        loc = np.where(result >= threshold)
        point = []  # 存储感叹号全局坐标

        for pt in zip(*loc[::-1]):
            top_left = pt
            point.append(top_left)

        return cv_utils.remove_same_position(point, 3)

    @classmethod
    def run(cls):
        game.set_foreground()
        game.to_game_main()
        cls.to_commission()
        time.sleep(1)
        if not cls.get_pending_point():
            log.info("没有需要清理的委托")
            win_message("委托", "没有需要清理的委托")
            return
        while cls.get_pending_point():
            pending_pos = cls.get_pending_point()
            pending_pos.sort(key=lambda x: x[1])  # 按y排序
            title_y = pending_pos[0][1]
            error_v = 3
            title_y_lower, title_y_upper = title_y - error_v, title_y + error_v
            title_pos = [point for point in pending_pos if title_y_lower <= point[1] <= title_y_upper]
            if len(title_pos) > TITLE_COUNT:
                log.error(f"委托标题应为{TITLE_COUNT}，实际为{len(title_pos)}")

            for point in title_pos:
                log.info("移动至委托标题")
                mouse.click_position(point)
                time.sleep(1.5)

                while commission_pos := cls.get_pending_point():
                    for commission_point in commission_pos:
                        if title_y_lower <= commission_point[1] <= title_y_upper:
                            # 跳过标题
                            continue
                        else:
                            # 委托任务
                            mouse.click_position(commission_point)
                            time.sleep(1)

                            wait_img(template_path.GET_COMMISSION)
                            get_pos = match_template(window.get_screenshot(),
                                                     template_path.GET_COMMISSION)
                            mouse.click_position(get_pos, direction="bottomRight", val=30)

                            wait_img(template_path.RE_COMMISSION)
                            again = match_template(window.get_screenshot(),
                                                   template_path.RE_COMMISSION,
                                                   threshold=0.9)
                            mouse.click_position(again)
                            time.sleep(1)
                            mouse.click_position(again, direction="bottomRight", val=30)
                            break
                    else:
                        # 只剩标题
                        break
        win_message("委托", "委托自动化完成")


if __name__ == '__main__':
    Commission.run()
