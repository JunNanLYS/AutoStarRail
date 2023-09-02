import os
import sys
import ctypes

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

import config
from gui.main_window import AutoStarRail
from script.utils import win_message


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        win_message("AutoStarRail", "请使用管理员身份运行脚本谢谢")
        return False


if not is_admin():
    win_message("", "请使用管理员身份启动脚本")
    exit()

# 设置应用程序图标
app = QApplication(sys.argv)


# 应用启动动画
splash = QSplashScreen(QPixmap(config.abspath + r"\doc\help.png"))
splash.resize(700, 600)
splash.show()
app.processEvents()

# 主窗口
window = AutoStarRail()
window.show()
splash.finish(window)

win_message("", "AutoStarRail启动成功")

sys.exit(app.exec())
