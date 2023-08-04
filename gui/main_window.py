from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication
from qframelesswindow import FramelessMainWindow, FramelessWindow

from utils import dialog
from script import use_of_world, use_of_commission
from script.use_of_stamina import use_of_stamina, set_stop
from threadpool import script_thread, function_thread
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

        self.setMinimumSize(QSize(300, 300))
        self.resize(700, 600)

        # 模拟宇宙

    def resizeEvent(self, size: QSize) -> None:
        super().resizeEvent(size)
        self.navigationBar.resize(self.width(), self.height() - self.titleBar.height())

    def __init_widget(self):
        self.navigationBar = ScriptNavigationBar(self)  # 主界面导航栏 (main window navigation bar)
        self.navigationBar.move(0, self.titleBar.height())

        self.logWindow = LogWindow()
        self.logWindow.hide()

    def __init_stamina_signal(self):
        """
        初始化体力界面的信号
        """
        stamina_stop = self.navigationBar.staminaInterface.stopButton
        stamina = self.navigationBar.staminaInterface.staminaButton
        stamina.clicked.connect(self.logWindow.show)  # 显示log
        stamina.clicked.connect(
            lambda: script_thread.submit(use_of_stamina, self.navigationBar.staminaInterface.get_copies_count())
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
        commission_button.clicked.connect(self.logWindow.show)
        commission_button.clicked.connect(
            lambda: script_thread.submit(use_of_commission.run)
        )
        mandate_button.clicked.connect(
            lambda: dialog.functions_not_open(self)
        )


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()
