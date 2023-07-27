import PySide6
from PySide6.QtCore import Signal, QSize, Qt
from PySide6.QtGui import QBrush, QColor, QPainter
from PySide6.QtWidgets import QWidget
from qfluentwidgets import MessageDialog


class WidgetBase(QWidget):
    sizeChange = Signal(QSize)
    dialogSignal = Signal(str, str)
    maskShow = Signal()
    maskHide = Signal()

    def __init__(self, parent=None, _isRound=True):
        super().__init__(parent)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self._brush = QBrush(QColor(255, 255, 255))
        self._isRound = _isRound
        self._radius = 10
        self._drawPen = False
        self._drawPenColor = QColor(0, 0, 0)

        # 将信号连接至槽函数(signal connect to slot)
        self.dialogSignal.connect(self.showMessageDialog)

    def resizeEvent(self, event: PySide6.QtGui.QResizeEvent) -> None:
        super().resizeEvent(event)
        self.sizeChange.emit(self.size())

    def paintEvent(self, event: PySide6.QtGui.QPaintEvent) -> None:
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        if self._drawPen:
            painter.setPen(self._drawPenColor)
        else:
            painter.setPen(Qt.NoPen)
        painter.setBrush(self._brush)
        if self._isRound:
            painter.drawRoundedRect(self.rect(), self._radius, self._radius)
        else:
            painter.drawRect(self.rect())

    def showMessageDialog(self, title: str, message: str):
        dialog = MessageDialog(title, message, self)
        dialog.show()

    def setDrawPen(self, draw: bool):
        self._drawPen = draw

    def setDrawPenColor(self, color: QColor):
        self._drawPenColor = color

    def setBrush(self, brush: QBrush):
        self._brush = brush

    def Brush(self):
        return self._brush

    def setRound(self, r: bool):
        self._isRound = r

    def isRound(self):
        return self._isRound

    def setRadius(self, r: int):
        self._radius = r