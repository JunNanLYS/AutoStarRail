import sys
import time
from typing import Optional

from PySide6.QtCore import Qt, QTimer, QTime, Signal
from PySide6.QtGui import QBrush, QColor, QGuiApplication
from PySide6.QtWidgets import QApplication, QVBoxLayout
from qfluentwidgets import StrongBodyLabel, SubtitleLabel
from qframelesswindow import FramelessDialog

from widgets import WidgetBase


class ScriptDialog(FramelessDialog):
    newDialog = Signal(str, str)
    def __init__(self, title, content):
        super().__init__()
        self.resize(400, 200)
        self.setResizeEnabled(False)
        self.title = title
        self.content = content
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.hide)
        self.__init_widget()

        self.newDialog.connect(self.new_dialog)

    def show(self) -> None:
        """
        使对话框显示在屏幕右下角
        """
        super().show()
        window_mandate_bar = 52  # windows任务栏高度
        desktop = QGuiApplication.screens()[0]
        rect = desktop.geometry()
        w, h = rect.width(), rect.height()
        target_w = w - self.width() - 20
        target_h = h - self.height() - window_mandate_bar - 20
        self.move(target_w, target_h)
        self.raise_()

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.background_widget.resize(self.width(), self.height() - self.titleBar.height())

    def __init_widget(self):
        h = self.titleBar.height()
        self.background_widget = WidgetBase(self, False)
        self.background_widget.move(0, h)
        self.background_widget.resize(self.width(), self.height() - h)
        self.background_widget.setBrush(QBrush(QColor(240, 240, 240)))

        self.vBoxLayout = QVBoxLayout(self.background_widget)
        self.vBoxLayout.setContentsMargins(10, 10, 10, 10)
        self.vBoxLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.vBoxLayout.setSpacing(30)
        self.title_label = SubtitleLabel(self.background_widget)
        self.title_label.setText(self.title)
        self.content_label = StrongBodyLabel(self.background_widget)
        self.content_label.setText(self.content)

        self.vBoxLayout.addWidget(self.title_label)
        self.vBoxLayout.addWidget(self.content_label)

    def setText(self, title, content):
        self.title_label.setText(title)
        self.content_label.setText(content)

    def new_dialog(self, title, content):
        self.setText(title, content)
        self.show()
        self.timer.start(3000)


class ScriptDialogInterface:
    def __init__(self):
        self.instance: Optional[ScriptDialog] = None

    def set_dialog(self, instance: ScriptDialog):
        self.instance = instance

    def new_dialog(self, title, content):
        if self.instance is None:
            raise AttributeError("instance is None")
        if not self.instance.isHidden():
            self.instance.timer.stop()
            self.instance.hide()
        # 使用信号传递是在主线程上，所以可以显示gui，否则会导致程序错误
        self.instance.newDialog.emit(title, content)


script_interface = ScriptDialogInterface()


# 给出一个外部方法方便调用
def new_dialog(title, content):
    script_interface.new_dialog(title, content)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    new_dialog('title', 'content')
    end = QTime.currentTime().addSecs(1)
    while QTime.currentTime() < end:
        app.processEvents()
    new_dialog('title2', 'content2')
    sys.exit(app.exec())
