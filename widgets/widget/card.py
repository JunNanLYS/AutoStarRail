from PySide6.QtGui import QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect
from widgets import WidgetBase


class FeatureCard(WidgetBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        # init shadow
        shadow = QGraphicsDropShadowEffect(self)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(63, 63, 63, 180))
        shadow.setBlurRadius(10)
        self.setGraphicsEffect(shadow)
