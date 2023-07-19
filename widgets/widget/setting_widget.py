from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from widgets import WidgetBase
from .ui.setting_widget import SettingWidgetUi
from qfluentwidgets import FluentIcon


class SettingWidget(WidgetBase, SettingWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_card()
        self.__init_widget()

    def __init_card(self):
        """
        将卡片存储起来
        """
        self.cards = []
        for child in self.scrollAreaWidget.children():
            if "Card" in child.objectName():
                self.cards.append(child)

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        # self.gameCard.setBrush(QBrush(QColor(250, 250, 250)))
        # self.staminaCard.setBrush(QBrush(QColor(250, 250, 250)))

        # 设置卡片阴影(set card shadow)
        for card in self.cards:
            shadow = QGraphicsDropShadowEffect(card)
            shadow.setColor(QColor(63, 63, 63, 180))
            shadow.setOffset(0, 0)
            shadow.setBlurRadius(10)
            card.setGraphicsEffect(shadow)

        self.setPathButton.setIcon(FluentIcon.FOLDER_ADD)