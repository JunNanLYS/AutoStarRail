import time

import pyautogui

import game
from script.utils import (match_template, match_template_gray, template_path, window, mouse, wait_img,
                          get_text_position)

import log
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
        for name, count in cfg.last_stamina.value.items():
            game.to_game_main()
            Stamina.click_book()
            wait_img(template_path.BOOK2)
            time.sleep(1)
            Stamina.click_index()
            time.sleep(1)  # 过度动画
            split_name = name.split('_')[0]
            target = CN_NAME[split_name]
            pos = get_text_position(window.get_screenshot(), "模拟宇宙")
            mouse.click_positions(pos)
            if target == "侵蚀隧洞" or target == "历战余响":
                mouse.mouse_scroll(2)
                time.sleep(1)
            print(target, split_name)
            target_pos = get_text_position(window.get_screenshot(), target)
            mouse.click_positions(target_pos)
            time.sleep(1)

            template = name_to_template(split_name + '_' + '1')
            print(template)
            pos = match_template(window.get_screenshot(), template)
            mouse.click_position(pos)

            template = name_to_template(name)
            while True:
                pos = match_template(window.get_screenshot(), template)
                if pos != (-1, -1):
                    break
                mouse.mouse_scroll(3)
            mouse.click_position(pos)




if __name__ == "__main__":
    time.sleep(0.5)
    Stamina.run()
