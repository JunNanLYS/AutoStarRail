import sys
import time
from typing import Optional

from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QBrush, QColor, QGuiApplication
from PySide6.QtWidgets import QApplication, QVBoxLayout
from qfluentwidgets import StrongBodyLabel, SubtitleLabel
from qframelesswindow import FramelessDialog

from widgets import WidgetBase


class ScriptDialog(FramelessDialog):
    def __init__(self, title, content):
        super().__init__()
        self.resize(400, 200)
        self.setResizeEnabled(False)
        self.title = title
        self.content = content
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.close)
        self.__init_widget()

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
        self.timer.start(3000)

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


dialog_instance: Optional[ScriptDialog] = None


def new_dialog(title, content):
    global dialog_instance
    # 判断当前是否还有存在的对话框
    if dialog_instance:
        dialog_instance.close()
        dialog_instance = None
    dialog_instance = ScriptDialog(title, content)
    dialog_instance.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    new_dialog('title', 'content')
    time.sleep(1)
    new_dialog('title2', 'content2')
    sys.exit(app.exec())
