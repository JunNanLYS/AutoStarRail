import os

from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication
from qframelesswindow import FramelessMainWindow, FramelessWindow

import utils.tool
from script import use_of_world, use_of_commission, use_of_stamina, auto_honkai_star_rail
from script.use_of_stamina import set_stop
from threadpool import script_thread, function_thread
from utils import dialog
from widgets.widget.dialog import new_dialog, ScriptDialog, script_interface
from widgets.navigation_bar import ScriptNavigationBar, LogNavigationBar


class LogWindow(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_widget()

        self.setMinimumSize(QSize(500, 500))
        self.resize(700, 500)
        self.move(0, 0)

        self.titleBar.closeBtn.clicked.disconnect(self.window().close)  # 把原来的close断开
        self.titleBar.closeBtn.clicked.connect(self.hide)

    def save_log(self):
        widget = self.logNavigationBar
        filename = os.path.join(utils.tool.PathTool.get_root_path(), "logs")
        run_log = os.path.join(filename, "run_log.log")
        game_log = os.path.join(filename, "game_log.log")
        debug_log = os.path.join(filename, "debug_log.log")
        # key是路径，value是控件引用
        dic = {
            run_log: widget.runLogInterface,
            game_log: widget.gameLogInterface,
            debug_log: widget.debugLogInterface,
        }
        # 将日志保存到路径文件夹中
        for log_filename, log_interface in dic.items():
            with open(log_filename, "w", encoding="UTF-8") as f:
                f.write(log_interface.toPlainText())

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.logNavigationBar.resize(self.width(), self.height() - self.titleBar.height())

    def __init_widget(self):
        self.logNavigationBar = LogNavigationBar(self)  # 日志窗口的导航栏
        self.logNavigationBar.move(0, self.titleBar.height())


class MainWindow(FramelessMainWindow):
    def __init__(self):
        super().__init__()
        self.__init_widget()
        # 连接信号
        self.__init_stamina_signal()
        self.__init_world_signal()
        self.__init_universe_signal()
        self.__init_more_signal()
        self.__init_info_signal()

        self.setMinimumSize(QSize(300, 300))
        self.resize(700, 600)
        self.raise_()

    def resizeEvent(self, size: QSize) -> None:
        super().resizeEvent(size)
        self.navigationBar.resize(self.width(), self.height() - self.titleBar.height())

    def __init_widget(self):
        self.navigationBar = ScriptNavigationBar(self)  # 主界面导航栏 (main window navigation bar)
        self.navigationBar.move(0, self.titleBar.height())

        self.logWindow = LogWindow()
        self.logWindow.hide()

        self.script_dialog = ScriptDialog("", "")
        script_interface.set_dialog(self.script_dialog)

    def __init_stamina_signal(self):
        """
        初始化体力界面的信号
        """
        stamina_stop = self.navigationBar.staminaInterface.stopButton
        stamina = self.navigationBar.staminaInterface.staminaButton
        stamina.clicked.connect(self.logWindow.show)  # 显示log
        stamina.clicked.connect(
            lambda: script_thread.submit(use_of_stamina.run, self.navigationBar.staminaInterface.get_copies_count())
        )
        stamina_stop.clicked.connect(lambda: set_stop(True))

    def __init_world_signal(self):
        """
        初始化世界界面的信号
        """
        # 控件初始化
        update_map = self.navigationBar.worldInterface.update_map_action
        update_script = self.navigationBar.worldInterface.update_script_action
        update_picture = self.navigationBar.worldInterface.update_picture_action
        update_all = self.navigationBar.worldInterface.updateButton
        map_combo = self.navigationBar.worldInterface.mapComboBox
        start_world = self.navigationBar.worldInterface.startButton

        # 连接信号
        start_world.clicked.connect(self.logWindow.show)  # 显示log
        start_world.clicked.connect(
            lambda: script_thread.submit(use_of_world.run, map_combo.currentText())
        )
        update_map.triggered.connect(
            lambda: function_thread.submit(use_of_world.update, '地图'))
        # update_script.triggered.connect(
        #     lambda: function_thread.submit(use_of_world.update, '脚本'))
        update_script.triggered.connect(
            lambda: dialog.functions_not_open(self))
        update_picture.triggered.connect(
            lambda: function_thread.submit(use_of_world.update, '图片'))
        # update_all.clicked.connect(
        #     lambda: function_thread.submit(use_of_world.update, '全部'))
        update_all.clicked.connect(
            lambda: dialog.functions_not_open(self))

    def __init_universe_signal(self):
        pass

    def __init_more_signal(self):
        widget = self.navigationBar.moreInterface
        commission_button = widget.commissionButton
        mandate_button = widget.mandateButton
        auto_button = widget.autoButton

        commission_button.clicked.connect(self.logWindow.show)
        commission_button.clicked.connect(
            lambda: script_thread.submit(use_of_commission.run)
        )
        mandate_button.clicked.connect(
            lambda: dialog.functions_not_open(self)
        )

        stamina_interface = self.navigationBar.staminaInterface
        world_interface = self.navigationBar.worldInterface
        auto_button.clicked.connect(self.logWindow.show)
        auto_button.clicked.connect(
            lambda: script_thread.submit(auto_honkai_star_rail.run,
                                         stamina_interface.get_copies_count(),
                                         world_interface.mapComboBox.currentText()))

    def __init_info_signal(self):
        widget = self.navigationBar.infoInterface
        view_log = widget.viewLogButton
        save_log = widget.saveLogButton

        view_log.clicked.connect(self.logWindow.show)
        save_log.clicked.connect(
            lambda: function_thread.submit(self.logWindow.save_log))


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()
