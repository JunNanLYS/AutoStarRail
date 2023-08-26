"""
战斗模块
"""
import time
from threading import Thread
from typing import Callable, Optional


class Fight:
    def __init__(self, set_move: Callable):
        self.set_move = set_move  # set_move接受一个bool，True可移动，False不能移动
        self.thread: Optional[Thread] = None
        self.close_thread = False  # 用于关闭线程

    def have_monster(self) -> bool:
        pass

    def go_fight(self):
        pass

    def in_fight(self) -> bool:
        pass

    def main(self):
        while not self.close_thread:
            # 发现怪物
            if self.have_monster():
                self.set_move(False)
                current = time.time()
                # 持续3秒攻击
                while current + 3 < time.time():
                    self.go_fight()
                # 判断是否进入了战斗
                if self.in_fight():
                    pass
                else:
                    self.set_move(True)
            else:
                time.sleep(1)

    def start(self):
        """
        开始监测，将开启新线程
        """
        self.close_thread = False
        thread = Thread(target=self.main)
        thread.start()

    def stop(self):
        """
        暂停检测
        """
        self.close_thread = True
