import PySide6
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel, QVBoxLayout
from qframelesswindow import FramelessWindow
from qfluentwidgets import PushButton


class Record(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.vBoxLayout = QVBoxLayout(self)
        self.vBoxLayout.setContentsMargins(0, 32, 0, 0)
        self.button = PushButton("开始录制", self)
        self.vBoxLayout.addWidget(self.button, 0, Qt.AlignmentFlag.AlignTop)
        self.resize(300, 300)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication()
    win = Record()
    win.show()
    app.exec()
