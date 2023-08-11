from PySide6.QtGui import QBrush, QColor

from widgets import WidgetBase
from .ui.universe_widget import UniverseWidgetUi


class UniverseWidget(WidgetBase, UniverseWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBrush(QBrush(QColor(240, 240, 240)))
        self.setupUi(self)
