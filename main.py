import os
import sys
import ctypes

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen

from gui.main_window import MainWindow
from utils.tool import PathTool
from utils.dialog import new_win_message


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if not is_admin():
    new_win_message("", "请使用管理员身份启动脚本")
    exit()

icon = os.path.join(PathTool.get_root_path(), r'doc\help.png')
# 设置应用程序图标
app = QApplication(sys.argv)
app.setWindowIcon(QIcon(icon))
app.setApplicationName("AutoStarRail")
appid = 'AutoStarRail'  # 应用程序名称
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)  # 注册应用使系统能识别

# 应用启动动画
splash = QSplashScreen(QPixmap(icon))
splash.resize(700, 600)
splash.show()
app.processEvents()

# 主窗口
window = MainWindow()
window.setWindowIcon(QIcon(icon))
window.show()
splash.finish(window)

new_win_message("", "AutoStarRail启动成功")

sys.exit(app.exec())
