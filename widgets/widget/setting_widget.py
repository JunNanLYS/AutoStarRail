from typing import Union

from PySide6.QtWidgets import QFileDialog
from qfluentwidgets import FluentIcon

from utils.tool import JsonTool
from widgets import WidgetBase
from .ui.setting_widget import SettingWidgetUi


def dump_value_to_json(key: str, value: Union[bool, int]) -> None:
    """
    key是json的键
    value是要设置的值
    """
    json_ = JsonTool.get_config_json()
    json_[key] = value
    JsonTool.dump_config_json(json_)


class SettingWidget(WidgetBase, SettingWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()
        self.__load_config()

        # 信号连接至槽
        self.gamePathButton.clicked.connect(self.set_file_name)
        self.fuelButton.checkedChanged. \
            connect(lambda: dump_value_to_json('use_fuel', self.fuelButton.isChecked()))
        self.exploreButton.checkedChanged. \
            connect(lambda: dump_value_to_json('use_explore', self.exploreButton.isChecked()))
        self.autofightButton.checkedChanged. \
            connect(lambda: dump_value_to_json('auto-fight', self.autofightButton.isChecked()))
        self.fuelSpinBox.valueChanged. \
            connect(lambda: dump_value_to_json('fuel_number', self.fuelSpinBox.value()))
        self.exploreSpinBox.valueChanged. \
            connect(lambda: dump_value_to_json('explore_number', self.exploreSpinBox.value()))

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

    def set_auto_fight(self) -> None:
        """
        设置自动战斗
        """
        json_ = JsonTool.get_config_json()
        json_["auto-fight"] = self.autofightButton.isChecked()
        JsonTool.dump_config_json(json_)

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        self.gamePathButton.setIcon(FluentIcon.FOLDER_ADD)
        self.fuelSpinBox.setMinimum(1)
        self.exploreSpinBox.setMinimum(1)

    def __load_config(self):
        """
        加载配置文件
        """
        from config import config as cfg
        json_ = JsonTool.get_config_json()
        self.gamePathEdit.setText(cfg.game_path)
        if cfg.auto_fight:
            self.autofightButton.toggleChecked()  # 自动战斗
        if cfg.use_fuel:
            self.fuelButton.toggleChecked()  # 燃料
        if cfg.use_explore:
            self.exploreButton.toggleChecked()  # 开拓力

        self.fuelSpinBox.setValue(json_["fuel_number"])
        self.exploreSpinBox.setValue(json_["explore_number"])
