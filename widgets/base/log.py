from PySide6.QtCore import Signal, Qt
from PySide6.QtGui import QTextCharFormat
from qfluentwidgets import PlainTextEdit
from typing import Optional


class Log:
    """
    单例类，主要将log输出绑定到widget上，便于观察
    """
    __isinstance = None

    def __init__(self):
        self._runLogWidget: Optional["LogWidget"] = None  # 程序运行日志
        self._gameLogWidget: Optional["LogWidget"] = None  # 游戏运行时的日志

    def setRunLogWidget(self, widget: "LogWidget"):
        self._runLogWidget = widget

    def setGameLogWidget(self, widget: "LogWidget"):
        self._gameLogWidget = widget

    def transmitRunLog(self, content: str, debug=False):
        print(content) if debug else ...
        if self._runLogWidget is not None:
            self._runLogWidget.add.emit(content)

    def transmitGameLog(self, content: str, debug=False):
        print(content) if debug else ...
        if self._gameLogWidget is not None:
            self._gameLogWidget.add.emit(content)

    def transmitAllLog(self, content: str, debug=False):
        print(content) if debug else ...
        self.transmitRunLog(content)
        self.transmitGameLog(content)

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)
            return cls.__isinstance
        return cls.__isinstance


log_isinstance = Log()


class LogWidget(PlainTextEdit):
    add = Signal(str)
    added = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)  # 只读(only read)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setMinimumSize(50, 50)
        self.setMaximumSize(2560, 1660)

        # 初始化字体(init font)
        fmt = QTextCharFormat()
        fmt.setFontPointSize(12)
        self.mergeCurrentCharFormat(fmt)

        # 将信号连接至槽函数(signal connect slot)
        self.add.connect(self.append)

    def append(self, text):
        """
        将要加入的string传入，将在控件最底下生成
        :param text: 要新增的文字
        :return:
        """
        self.appendPlainText(text)
        self.added.emit()
