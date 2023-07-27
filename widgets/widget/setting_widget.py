from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QFileDialog

from widgets import WidgetBase
from .ui.setting_widget import SettingWidgetUi
from utils.tool import JsonTool
from qfluentwidgets import FluentIcon


class SettingWidget(WidgetBase, SettingWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_card()
        self.__init_widget()
        self.__load_config()

        # 信号连接至槽
        self.gamePathButton.clicked.connect(self.set_file_name)

    def set_file_name(self) -> None:
        """
        选择游戏路径
        """
        filename = QFileDialog.getOpenFileName(self, "AutoStarRail")
        filename = filename[0]
        self.gamePathEdit.setText(filename)

        # 保存至配置文件
        json_ = JsonTool.get_config_json()
        json_["game_path"] = filename
        JsonTool.dump_config_json(json_)

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

        # 设置卡片阴影(set card shadow)
        for card in self.cards:
            shadow = QGraphicsDropShadowEffect(card)
            shadow.setColor(QColor(63, 63, 63, 180))
            shadow.setOffset(0, 0)
            shadow.setBlurRadius(10)
            card.setGraphicsEffect(shadow)

        self.gamePathButton.setIcon(FluentIcon.FOLDER_ADD)

    def __load_config(self):
        """
        加载配置文件
        """
        json_ = JsonTool.get_config_json()
        self.gamePathEdit.setText(json_["game_path"])
        if json_["use_fuel"]:
            self.fuelButton.toggleChecked()  # 燃料
        if json_["use_explore"]:
            self.powerButton.toggleChecked()  # 开拓力
