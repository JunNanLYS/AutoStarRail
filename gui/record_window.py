import PySide6
from qframelesswindow import FramelessWindow


class Record(FramelessWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.resize(500, 500)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication

    app = QApplication()
    win = Record()
    win.show()
    app.exec()
