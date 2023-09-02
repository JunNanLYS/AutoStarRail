import os

from qfluentwidgets import (NavigationItemPosition, NavigationWidget,
                            NavigationInterface, FluentIcon, MSFluentWindow)
from PySide6.QtGui import QIcon

import config
from gui.widgets import SettingInterface


class AutoStarRail(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.setting_interface = SettingInterface(self)

        self.__init_widget()

    def __init_navigation(self):
        self.addSubInterface(
            self.setting_interface,
            FluentIcon.SETTING,
            "设置",
            position=NavigationItemPosition.BOTTOM
        )

    def __init_widget(self):
        import ctypes
        icon = os.path.join(config.abspath, "doc", "help.ico")
        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle("AutoStarRail")
        self.resize(800, 600)
        self.__init_navigation()

        # 设置应用程序
        appid = 'AutoStarRail'  # 应用程序名称
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)  # 注册应用使系统能识别


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = AutoStarRail()
    window.show()
    app.exec()
