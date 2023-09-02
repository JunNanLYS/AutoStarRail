import os
import sys
import ctypes

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

import config
from gui.main_window import MainWindow
from script.utils import win_message


class AutoStarRail(MainWindow):
    def __init__(self):
        super().__init__()


# 设置应用程序图标
app = QApplication(sys.argv)

win_message("", "AutoStarRail启动成功")
sys.exit(app.exec())
