import sys
import os

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

import config
from gui.main_window import MainWindow


class AutoStarRail(MainWindow):
    def __init__(self):
        super().__init__()

        self.__init_widget()

    def connect_signal_to_slot(self):
        pass

    def __init_widget(self):
        import ctypes
        icon = os.path.join(config.abspath, "doc", "help.ico")
        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle("AutoStarRail")

        # 设置应用程序
        appid = 'AutoStarRail'  # 应用程序名称
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)  # 注册应用使系统能识别


# 设置应用程序图标
app = QApplication(sys.argv)
auto_star_rail = AutoStarRail()
auto_star_rail.show()
sys.exit(app.exec())
