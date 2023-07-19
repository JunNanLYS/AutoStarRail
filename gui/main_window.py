import PySide6
from PySide6.QtCore import QSize
from qframelesswindow import FramelessMainWindow, FramelessWindow
from PySide6.QtWidgets import QApplication, QWidget
from script.start_game import start_game
from script.use_of_stamina import use_of_stamina

from widgets.navigation_bar import ScriptNavigationBar, LogNavigationBar
from threadpool import script_thread


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

        self.setMinimumSize(QSize(500, 500))
        self.resize(1000, 800)

        # 连接信号
        stamina = self.navigationBar.featureInterface.staminaButton
        stamina.clicked.connect(self.logWindow.show)  # 显示log
        stamina.clicked.connect(
            lambda: script_thread.submit(use_of_stamina, self.navigationBar.featureInterface.get_copies_count())
        )

    def resizeEvent(self, size: PySide6.QtCore.QSize) -> None:
        super().resizeEvent(size)
        self.navigationBar.resize(self.width(), self.height() - self.titleBar.height())

    def __init_widget(self):
        self.navigationBar = ScriptNavigationBar(self)  # 主界面导航栏 (main window navigation bar)
        self.navigationBar.move(0, self.titleBar.height())

        self.logWindow = LogWindow()


if __name__ == "__main__":
    app = QApplication()
    win = MainWindow()
    win.show()

    app.exec()
