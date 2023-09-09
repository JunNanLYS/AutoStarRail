import sys
import os
from concurrent.futures import Future

from PySide6.QtCore import Signal
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

import config
import log
import threadpool
from config import cfg
from gui.main_window import MainWindow


def get_time():
    from datetime import datetime
    return datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")


class AutoStarRail(MainWindow):
    exception_message_signal = Signal(Future)

    def __init__(self):
        super().__init__()

        self.__init_widget()

    def exception_message(self, f: Future):
        """捕获异常并弹出对话框"""
        from qfluentwidgets import MessageBox
        try:
            f.result()
        except Exception as e:
            log.error(f"捕获到异常: {type(e).__name__}, {e}")
            dialog = MessageBox(type(e).__name__, str(e), self.window())
            dialog.exec()

    def __on_run_interface_button_clicked_slot(self):
        from qfluentwidgets import MessageBox
        from script.stamina.main import Stamina
        from script.universe.main import Universe
        from script.commission.main import Commission
        combobox = self.run_interface.combobox
        current_text = combobox.currentText()
        text_to_method = {
            "体力": Stamina.run,
            "模拟宇宙": Universe.run_universe,
            "委托": Commission.run
        }
        # 使用不开放的脚本
        if current_text not in text_to_method:
            dialog = MessageBox("温馨提示", "该功能暂不开放", self.window())
            dialog.exec()
        # 运行脚本
        else:
            future = threadpool.script_thread.submit(text_to_method[current_text])
            future.add_done_callback(self.exception_message_signal.emit)
            future.add_done_callback(self.update_info_card)

        if current_text == "体力":
            now = get_time()
            cfg.set(cfg.last_stamina_time, now)

    def __on_angle_button_slot(self):
        from script.universe.main import Universe
        future = threadpool.script_thread.submit(Universe.run_align_angle)
        future.add_done_callback(self.exception_message_signal.emit)
        future.add_done_callback(self.update_info_card)

    def __connect_signal_to_slot(self):
        # AutoStarRail
        self.exception_message_signal.connect(self.exception_message)
        # run interface
        self.run_interface.button_run.clicked.connect(self.__on_run_interface_button_clicked_slot)
        self.run_interface.button_angle.clicked.connect(self.__on_angle_button_slot)

    def __init_widget(self):
        import ctypes
        self.__connect_signal_to_slot()

        icon = os.path.join(config.abspath, "doc", "help.ico")
        self.setWindowIcon(QIcon(icon))
        self.setWindowTitle("AutoStarRail")

        # 设置应用程序
        appid = 'AutoStarRail'  # 应用程序名称
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)  # 注册应用使系统能识别


# 将Auto_Simulated_Universe添加到搜索路径
sys.path.append(os.path.join(config.abspath, "Auto_Simulated_Universe"))

# 设置应用程序图标
app = QApplication(sys.argv)
auto_star_rail = AutoStarRail()
auto_star_rail.show()
sys.exit(app.exec())
