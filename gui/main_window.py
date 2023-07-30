from PySide6.QtCore import QSize
from PySide6.QtWidgets import QApplication
from qframelesswindow import FramelessMainWindow, FramelessWindow

from script.use_of_stamina import use_of_stamina, set_stop
from script import world
from threadpool import script_thread
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

        self.setMinimumSize(QSize(300, 300))
        self.resize(700, 600)

        # 清体力
        stamina_stop = self.navigationBar.staminaInterface.stopButton
        stamina = self.navigationBar.staminaInterface.staminaButton
        stamina.clicked.connect(self.logWindow.show)  # 显示log
        stamina.clicked.connect(
            lambda: script_thread.submit(use_of_stamina, self.navigationBar.staminaInterface.get_copies_count())
        )
        stamina_stop.clicked.connect(lambda: set_stop(True))

        # 锄大地
        map_combo = self.navigationBar.worldInterface.mapComboBox
        start_world = self.navigationBar.worldInterface.startButton
        start_world.clicked.connect(self.logWindow.show)  # 显示log
        start_world.clicked.connect(
            lambda: script_thread.submit(world.run, map_combo.currentText())
        )

        # 模拟宇宙

    def resizeEvent(self, size: QSize) -> None:
        super().resizeEvent(size)
        self.navigationBar.resize(self.width(), self.height() - self.titleBar.height())

    def __init_widget(self):
        self.navigationBar = ScriptNavigationBar(self)  # 主界面导航栏 (main window navigation bar)
        self.navigationBar.move(0, self.titleBar.height())

        self.logWindow = LogWindow()
        self.logWindow.hide()


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()
    app.exec()
