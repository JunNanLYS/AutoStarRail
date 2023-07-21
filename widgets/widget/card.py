from typing import Optional

from PySide6.QtCore import Property, QSize, QPropertyAnimation
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QLabel, QSpinBox, QSpacerItem, QWidget
from widgets import WidgetBase


class Card(WidgetBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        # init shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(63, 63, 63, 180))
        shadow.setBlurRadius(10)
        self.setGraphicsEffect(shadow)


class StretchableCard(Card):
    def __init__(self, parent=None):
        super().__init__(parent)
        # init animation
        self.animation = QPropertyAnimation(self, b'stretchHeight')
        self.animation.setDuration(500)

    @Property(int)
    def stretchHeight(self):
        return self.height()

    @stretchHeight.setter
    def stretchHeight(self, height):
        self.setFixedHeight(height)

    def startAnimation(self, height):
        self.animation.setStartValue(self.height())  # 从当前卡片高度开始
        self.animation.setEndValue(height)  # 到设定的位置结束
        self.animation.start()


class StaminaCard(StretchableCard):
    def __init__(self, parent=None):
        super().__init__(parent)
        self._isStretch = True
        self._title: Optional[QWidget] = None

    def setTitleLabel(self, widget):
        self._title = widget
        self._title.setFixedHeight(self._title.height())

    def recover(self):
        self.setMinimumHeight(0)
        self.setMaximumHeight(10000)

    def mousePressEvent(self, event) -> None:
        """
        点击卡片标题伸缩
        """
        super().mousePressEvent(event)
        # 没设置标题
        if self._title is None:
            return

        pressPosition = event.position()
        x1, x2 = self._title.x(), self._title.x() + self._title.width()
        y1, y2 = self._title.y(), self._title.y() + self._title.height()
        if x1 <= pressPosition.x() <= x2 and y1 <= pressPosition.y() <= y2:
            for child in self.children():
                if child is self._title:
                    continue
                if isinstance(child, (QLabel, QSpinBox, QSpacerItem)):
                    child.hide() if self._isStretch else child.show()
            if self._isStretch:
                self.startAnimation(self._title.height() + 10)
                self._isStretch = False
            else:
                self._isStretch = True
                self.recover()
