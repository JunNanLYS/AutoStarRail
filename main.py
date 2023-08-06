import os
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow, MySplashScreen
from utils.tool import PathTool

app = QApplication(sys.argv)
app.setWindowIcon(QIcon(os.path.join(PathTool.get_root_path(), r'doc\help.png')))
app.setApplicationName("AutoStarRail")
# 应用启动动画
splash = MySplashScreen(QIcon(os.path.join(PathTool.get_root_path(), r'doc\help.png')))
splash.resize(700, 600)
splash.show()
app.processEvents()

window = MainWindow()
window.show()
splash.finish()
sys.exit(app.exec())
