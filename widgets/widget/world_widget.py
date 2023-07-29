import json
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication
from qfluentwidgets import RoundMenu
from pydantic import BaseModel

from .ui.world_widget import WorldWidgetUi
from widgets import WidgetBase
from utils.dialog import functions_not_open
from utils import tool


class MapData(BaseModel):
    author: str
    filename: str
    name: str
    number: str


name_to_map = {}  # name: Map
number_to_map = {}  # number: Map

root_path = tool.PathTool.get_root_path()
map_filename = root_path + r'\StarRailAssistant\map'  # 地图文件地址

json_files = [file for file in os.listdir(map_filename) if file.endswith('.json')]

for json_file in json_files:
    json_filename = os.path.join(map_filename, json_file)
    with open(json_filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        map_number = json_file.split('.')[0].replace('map_', '')
        m = MapData(author=data['author'], filename=json_filename, name=data['name'], number=map_number)
        name_to_map[data['name']] = m
        number_to_map[map_number] = m


class WorldWidget(WidgetBase, WorldWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def start(self):
        import os
        from StarRailAssistant.run import run_map
        from utils.path import PathTool
        map_name = self.mapComboBox.currentText()  # 获取选择的起点地图
        map_data = name_to_map[map_name]  # 转换成地图数据
        number = map_data.number
        os.chdir(os.path.join(PathTool.get_root_path(), 'StarRailAssistant'))  # 切换python运行路径
        run_map(number)  # 运行地图

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        self.updateCardLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__init_combo_box()
        self.__init_update_button()
        self.startButton.clicked.connect(self.start)

    def __init_combo_box(self):
        """
        初始化ComboBox中地图选项
        """
        self.mapComboBox.addItems(list(name_to_map.keys()))
        self.mapComboBox.setCurrentIndex(0)

    def __init_update_button(self):
        menu = RoundMenu(parent=self)
        update_map_action = QAction("更新地图")
        update_script_action = QAction("更新脚本")
        update_image_action = QAction("更新图片")

        # 连接信号
        update_map_action.triggered.connect(lambda: functions_not_open(self.parent().parent()))
        update_image_action.triggered.connect(lambda: functions_not_open(self.parent().parent()))
        update_script_action.triggered.connect(lambda: functions_not_open(self.parent().parent()))
        self.updateButton.clicked.connect(lambda: functions_not_open(self.parent().parent()))

        # 添加至菜单栏
        menu.addActions([
            update_map_action,
            update_script_action,
            update_image_action
        ])

        self.updateButton.setFlyout(menu)
        self.updateButton.setText("全部更新")


if __name__ == '__main__':
    app = QApplication()
    win = WorldWidget()
    win.show()
    app.exec()
