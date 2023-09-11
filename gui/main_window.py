import os

from qfluentwidgets import (NavigationItemPosition, NavigationWidget,
                            NavigationInterface, FluentIcon, MSFluentWindow)
from PySide6.QtGui import QIcon

import config
import log
from gui.widgets import (SettingInterface, ScriptInterface, LogInterface, AvatarInterface, RunInterface)


def get_icon_path(icon_name: str):
    return os.path.join(config.abspath, "gui", "icon", icon_name)


class MainWindow(MSFluentWindow):
    def __init__(self):
        super().__init__()
        self.is_first = True

        self.setting_interface = SettingInterface(self)
        self.script_interface = ScriptInterface(self)
        self.log_interface = LogInterface(self)
        self.avatar_interface = AvatarInterface(self)
        self.run_interface = RunInterface(self)

        self.__init_widget()

    def update_info_card(self, *args):
        self.script_interface.update_info_card()

    def __init_navigation(self):
        self.addSubInterface(
            self.script_interface,
            QIcon(get_icon_path("script_d.png")),
            "脚本",
            position=NavigationItemPosition.TOP,
            selectedIcon=QIcon(get_icon_path("script_s.png"))
        )

        self.addSubInterface(
            self.log_interface,
            QIcon(get_icon_path("log_d.png")),
            "日志",
            position=NavigationItemPosition.TOP,
            selectedIcon=QIcon(get_icon_path("log_s.png"))
        )

        self.addSubInterface(
            self.run_interface,
            QIcon(get_icon_path("run_d.png")),
            "运行",
            position=NavigationItemPosition.SCROLL,
            selectedIcon=QIcon(get_icon_path("run_s.png"))
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

    def __init_widget(self):
        self.resize(900, 600)
        self.__init_navigation()
        log.set_log_widget(self.log_interface)


if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
