import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow


class AutoStarRail(MainWindow):
    def __init__(self):
        super().__init__()


# 设置应用程序图标
app = QApplication(sys.argv)
auto_star_rail = AutoStarRail()
auto_star_rail.show()
sys.exit(app.exec())
