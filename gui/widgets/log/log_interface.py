from PySide6.QtCore import Signal
from qfluentwidgets import PlainTextEdit


class LogInterface(PlainTextEdit):
    add = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("日志")
        self.add.connect(self.append)
        self.setReadOnly(True)

    def append(self, text: str) -> None:
        self.appendPlainText(text)

