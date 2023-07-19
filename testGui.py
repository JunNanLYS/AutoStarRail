from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QApplication, QWidget
from widgets import LogWidget, WidgetBase
from qfluentwidgets import PushButton
from qframelesswindow import FramelessWindow, FramelessMainWindow


def slot1():
    print("slot1")


def slot2():
    print("slot2")


class MainWindow(FramelessMainWindow):
    def __init__(self):
        super().__init__()
        self.button = PushButton(self)

        self.button.clicked.connect(slot1)
        self.button.clicked.disconnect(slot1)
        # self.button.disconnect(self.button.clicked.connect(self.slot2))


app = QApplication()
win = MainWindow()
win.show()
app.exec()
