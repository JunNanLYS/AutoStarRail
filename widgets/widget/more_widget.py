from widgets import WidgetBase
from .ui.more_widget import MoreWidgetUi
from utils.dialog import functions_not_open


class MoreWidget(WidgetBase, MoreWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")  # 关闭边框
