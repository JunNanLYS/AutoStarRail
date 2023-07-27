from PySide6.QtCore import Qt
from PySide6.QtGui import QBrush, QColor
from PySide6.QtWidgets import QStackedWidget, QVBoxLayout
from qfluentwidgets import Pivot

from widgets import WidgetBase, SettingWidget, InfoWidget, StaminaWidget, WorldWidget, UniverseWidget,\
    LogWidget, log


class NavigationBar(WidgetBase):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_widget()

        self.resize(400, 400)

    def addSubInterface(self, widget, objectName, text):
        widget.setObjectName(objectName)
        self.stackedWidget.addWidget(widget)
        self.pivot.addItem(
            routeKey=objectName,
            text=text,
            onClick=lambda: self.stackedWidget.setCurrentWidget(widget)
        )

    def onCurrentIndexChanged(self, index):
        widget = self.stackedWidget.widget(index)
        self.pivot.setCurrentItem(widget.objectName())

    def __init_widget(self):
        self.pivot = Pivot(self)
        self.stackedWidget = QStackedWidget(self)
        self.vBoxLayout = QVBoxLayout(self)

        self.vBoxLayout.addWidget(self.pivot, 0, Qt.AlignmentFlag.AlignLeft)
        self.vBoxLayout.addWidget(self.stackedWidget)
        self.vBoxLayout.setContentsMargins(5, 0, 5, 5)

        self.stackedWidget.currentChanged.connect(self.onCurrentIndexChanged)


class ScriptNavigationBar(NavigationBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBrush(QBrush(QColor(240, 240, 240)))

        self.__init_widget()

    def __init_widget(self):
        self.staminaInterface = StaminaWidget(self)  # 清体力
        self.worldInterface = WorldWidget(self)  # 锄大地
        self.universeInterface = UniverseWidget(self)  # 模拟宇宙
        self.settingInterface = SettingWidget(self)  # 设置
        self.infoInterface = InfoWidget(self)  # 信息

        # 添加到项到pivot(add items to pivot)
        self.addSubInterface(self.staminaInterface, "staminaInterface", "体力")
        self.addSubInterface(self.worldInterface, "worldInterface", "世界")
        self.addSubInterface(self.universeInterface, "universeInterface", "模拟宇宙")
        self.addSubInterface(self.settingInterface, "settingInterface", "设置")
        self.addSubInterface(self.infoInterface, "infoInterface", "信息")

        # 设置当前导航栏的item(set current item)
        self.stackedWidget.setCurrentWidget(self.staminaInterface)
        self.pivot.setCurrentItem(self.staminaInterface.objectName())


class LogNavigationBar(NavigationBar):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setBrush(QBrush(QColor(240, 240, 240)))

        self.__init_widget()

    def __init_widget(self):
        self.runLogInterface = LogWidget(self)  # 运行日志
        self.gameLogInterface = LogWidget(self)  # 游戏日志
        log.setRunLogWidget(self.runLogInterface)
        log.setGameLogWidget(self.gameLogInterface)

        # 添加项到pivot
        self.addSubInterface(self.runLogInterface, "runLogInterface", "运行日志")
        self.addSubInterface(self.gameLogInterface, "gameLogInterface", "游戏日志")

        # 设置当前导航栏的item
        self.stackedWidget.setCurrentWidget(self.runLogInterface)
        self.pivot.setCurrentItem(self.runLogInterface.objectName())