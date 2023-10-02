import time
from math import sqrt, pow, inf

import cv2
import pyautogui

import game
import log
from script.utils import (match_template, match_template_gray, template_path, window, mouse, wait_img,
                          get_text_position, where_img, wait_text, Role, win_message)
from script.stamina.data import CN_NAME, name_to_template


class Stamina:
    @classmethod
    def click_book(cls):
        log.info("点击书本")
        pos = match_template_gray(window.get_screenshot(), template_path.BOOK)
        pyautogui.keyDown('alt')
        mouse.click_position(pos)
        pyautogui.keyUp('alt')

    @classmethod
    def click_index(cls):
        log.info("点击生存索引")
        pos = match_template(window.get_screenshot(), template_path.INDEX)
        if pos == (-1, -1):
            pos = match_template(window.get_screenshot(), template_path.INDEX_SELECTED)
        mouse.click_position(pos)

    @classmethod
    def run(cls):
        from config import cfg
        game.set_foreground()  # 将游戏设置到前台
        for name, count in cfg.last_stamina.value.items():
            log.info(f"副本{name}，次数{count}")
            if count == 0:
                continue
            while count > 0:
                game.to_game_main()
                Stamina.click_book()
                wait_img(template_path.BOOK2, mode="gray")
                time.sleep(2)
                Stamina.click_index()
                time.sleep(1)  # 等待过渡动画结束
                split_name = name.split('_')
                # 特殊判断，拟造花萼金和赤
                if split_name[1] in ["gold", "red"]:
                    split_name = split_name[0] + '_' + split_name[1]
                else:
                    split_name = split_name[0]
                target = CN_NAME[split_name]
                pos = get_text_position(window.get_screenshot(), "模拟宇宙")
                mouse.click_positions(pos)
                if target == "侵蚀隧洞" or target == "历战余响":
                    mouse.mouse_scroll(2)
                    time.sleep(1)
                target_pos = get_text_position(window.get_screenshot(), target)
                mouse.click_positions(target_pos)
                time.sleep(1)

                template = name_to_template(split_name + '_' + '1')
                pos = match_template(window.get_screenshot(), template)
                mouse.click_position(pos)

                template = name_to_template(name)
                while True:
                    pos = match_template(window.get_screenshot(), template)
                    if pos != (-1, -1):
                        break
                    mouse.mouse_scroll(3)
                mouse.click_position(pos)
                h, w = cv2.imread(template).shape[:2]
                template_center = (pos[0] + w // 2, pos[1] + h // 2)

                # 处理传送点坐标位置
                log.info("计算对应传送点按钮位置")
                position_list = where_img(window.get_screenshot(), template_path.TRANSMISSION)  # 获取所有传送按钮坐标
                d = inf
                pos = (-1, -1)
                for positions in position_list:
                    d_temp = sqrt(pow(positions[0] - template_center[0], 2) + pow(positions[1] - template_center[1], 2))
                    if d_temp < d:
                        d = d_temp
                        pos = positions
                h, w = cv2.imread(template_path.TRANSMISSION).shape[:2]
                mouse.click_position((pos[0] + w // 2, pos[1] + h // 2))
                time.sleep(2)

                # 根据需求增加挑战次数，若超出6次则只增加6次
                log.info("添加挑战次数")
                wait_text(window.get_screenshot, "挑战")
                pos = match_template(window.get_screenshot(), template_path.ADD_CHALLENGE)
                if count >= 6:
                    for _ in range(5):
                        mouse.click_position(pos)
                        time.sleep(0.1)
                    count -= 6
                else:
                    for _ in range(count - 1):
                        mouse.click_position(pos)
                        time.sleep(0.1)
                    count = 0

                # 点击挑战
                challenge_pos = wait_text(window.get_screenshot, "挑战")
                mouse.click_positions(challenge_pos)

                # 点击开始挑战
                start_challenge_pos = wait_text(window.get_screenshot, "开始挑战")
                mouse.click_positions(start_challenge_pos)

                # 凝滞虚影需要手动攻击
                if "shadow" in name:
                    log.info("需要移动后攻击")
                    time.sleep(1)
                    Role.move_position(20).result()  # 等待移动结束后再攻击
                    pyautogui.click()

                wait_text(game.get_screenshot, "战斗开始")  # 等待进入战斗界面
                auto_fight_pos = match_template_gray(window.get_screenshot(), template_path.AUTO_FIGHT, threshold=0.9)
                if auto_fight_pos != (-1, -1):
                    mouse.click_position(auto_fight_pos)

                wait_img(template_path.EXIT_COPIES)
                exit_pos = match_template(window.get_screenshot(), template_path.EXIT_COPIES)
                h, w = cv2.imread(template_path.EXIT_COPIES).shape[:2]
                mouse.click_position((exit_pos[0] + w // 2, exit_pos[1] + h // 2))
        log.info("运行结束")
        win_message("AutoStarRail", "体力脚本运行结束")


if __name__ == "__main__":
    time.sleep(0.5)
    Stamina.run()
