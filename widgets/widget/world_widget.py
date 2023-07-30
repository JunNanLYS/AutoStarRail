import json
import os

from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication
from qfluentwidgets import RoundMenu

from .ui.world_widget import WorldWidgetUi
from widgets import WidgetBase
from utils.dialog import functions_not_open
from script.world import name_to_map, update
from threadpool import function_thread


class WorldWidget(WidgetBase, WorldWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")
        self.updateCardLayout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.__init_combo_box()
        self.__init_update_button()

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
        update_map_action.triggered.connect(lambda: function_thread.submit(update, '地图'))
        update_image_action.triggered.connect(lambda: function_thread.submit(update, '图片'))
        update_script_action.triggered.connect(lambda: function_thread.submit(update, '脚本'))
        self.updateButton.clicked.connect(lambda: function_thread.submit(update, '全部'))

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
