from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication
from qfluentwidgets import RoundMenu

from script.world import name_to_map
from widgets import WidgetBase
from .ui.world_widget import WorldWidgetUi


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
        self.update_map_action = QAction("更新地图")
        self.update_script_action = QAction("更新脚本")
        self.update_picture_action = QAction("更新图片")

        # 添加至菜单栏
        menu.addActions([
            self.update_map_action,
            self.update_script_action,
            self.update_picture_action
        ])

        self.updateButton.setFlyout(menu)
        self.updateButton.setText("全部更新")


if __name__ == '__main__':
    app = QApplication()
    win = WorldWidget()
    win.show()
    app.exec()
