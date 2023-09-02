import os

from qfluentwidgets import (NavigationItemPosition, NavigationWidget,
                            NavigationInterface, FluentIcon, MSFluentWindow)
from PySide6.QtGui import QIcon

import config
import log
from gui.widgets import SettingInterface, ScriptInterface, LogInterface, AvatarInterface


def get_icon_path(icon_name: str):
    return os.path.join(config.abspath, "gui", "icon", icon_name)


class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.setting_interface = SettingInterface(self)
        self.script_interface = ScriptInterface(self)
        self.log_interface = LogInterface(self)
        self.avatar_interface = AvatarInterface(self)

        self.__init_widget()

    def __init_navigation(self):
        self.addSubInterface(
            self.script_interface,
            QIcon(get_icon_path("run_d.png")),
            "脚本",
            position=NavigationItemPosition.TOP,
            selectedIcon=QIcon(get_icon_path("run_s.png"))
        )

        self.addSubInterface(
            self.log_interface,
            QIcon(get_icon_path("log_d.png")),
            "日志",
            position=NavigationItemPosition.TOP,
            selectedIcon=QIcon(get_icon_path("log_s.png"))
        )

        self.addSubInterface(
            self.avatar_interface,
            QIcon(get_icon_path("NanJun.png")),
            "NanJun",
            position=NavigationItemPosition.BOTTOM,
        )

        self.addSubInterface(
            self.setting_interface,
            FluentIcon.SETTING,
            "设置",
            position=NavigationItemPosition.BOTTOM
        )

        self.navigationInterface.setCurrentItem("脚本")

    def __init_widget(self):
        import ctypes
        icon = os.path.join(config.abspath, "doc", "help.ico")
        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle("AutoStarRail")
        self.resize(900, 600)
        self.__init_navigation()
        log.set_log_widget(self.log_interface)

        # 设置应用程序
        appid = 'AutoStarRail'  # 应用程序名称
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)  # 注册应用使系统能识别


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
