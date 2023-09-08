from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QFrame
from qfluentwidgets import (ExpandLayout, SettingCardGroup, PushSettingCard, FluentIcon,
                            SwitchSettingCard, HyperlinkCard, StrongBodyLabel)
from .ui.settingWidget import Ui_Frame
from config import cfg


class SettingInterface(QFrame, Ui_Frame):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("设置")
        self.setupUi(self)
        self.setStyleSheet(
            """
            background: rgb(250, 250, 250);
            border: none;
            border-radius:10px;
            """
        )
        self.expand_layout = ExpandLayout(self.scrollWidget)

        # game group
        self.game_group = SettingCardGroup("游戏", self.scrollWidget)
        self.game_path = PushSettingCard("选择游戏路径", FluentIcon.FOLDER,
                                         title="游戏路径",
                                         content=cfg.game_path.value,
                                         parent=self.game_group)
        self.open_map = PushSettingCard("设置按键", icon=QIcon(),
                                        title="地图按键",
                                        content=f"当前为: {cfg.open_map.value}",
                                        parent=self.game_group)
        self.auto_fight = SwitchSettingCard(QIcon(), title="自动战斗", content="游戏内沿用上次一自动战斗是否开启",
                                            configItem=cfg.auto_fight)

        # stamina
        self.stamina_group = SettingCardGroup("体力", self.scrollWidget)
        self.use_fuel = SwitchSettingCard(QIcon(), title="燃料", content="开启后将使用体力",
                                          configItem=cfg.use_fuel)
        self.use_explore = SwitchSettingCard(QIcon(), title="星穹", content="开启后将使用星穹",
                                             configItem=cfg.use_explore)

        # universe
        self.universe_group = SettingCardGroup("模拟宇宙", self.scrollWidget)
        self.get_angle = SwitchSettingCard(QIcon(), title="校准角度", content="每次启动模拟宇宙校准角度",
                                           configItem=cfg.universe_auto_angle)

        # more
        self.more_group = SettingCardGroup("更多", self.scrollWidget)
        self.github_link = HyperlinkCard(r"https://github.com/JunNanLYS/AutoStarRail",
                                         "前往Github",
                                         FluentIcon.GITHUB,
                                         "整合包作者主页",
                                         "点个⭐给予动力源泉")
        self.universe_link = HyperlinkCard(r"https://github.com/CHNZYX/Auto_Simulated_Universe",
                                           "前往Github",
                                           FluentIcon.GITHUB,
                                           "模拟宇宙作者主页",
                                           "点个⭐给予动力源泉")
        self.fluent_link = HyperlinkCard(r"https://github.com/zhiyiYo/PyQt-Fluent-Widgets",
                                         "前往Github",
                                         FluentIcon.GITHUB,
                                         "Fluent-Widgets作者主页",
                                         "点个⭐给予动力源泉")
        self.warning_label = StrongBodyLabel(self.more_group)
        self.warning_label.setText("该项目仅用于学习交流，造成的一切后果由使用者自己承担")
        self.info_label = StrongBodyLabel(self.more_group)
        self.info_label.setText("从任何渠道购买到该项目请立即退款并差评")

        self.__init_widget()

    def __init_layout(self):
        # add setting card to game group
        self.game_group.addSettingCard(self.game_path)
        self.game_group.addSettingCard(self.open_map)
        self.game_group.addSettingCard(self.auto_fight)

        # add setting card to stamina group
        self.stamina_group.addSettingCard(self.use_fuel)
        self.stamina_group.addSettingCard(self.use_explore)

        # add setting card to universe group
        self.universe_group.addSettingCard(self.get_angle)

        # add setting card to more group
        self.more_group.addSettingCard(self.github_link)
        self.more_group.addSettingCard(self.universe_link)
        self.more_group.addSettingCard(self.fluent_link)
        self.more_group.addSettingCard(self.warning_label)
        self.more_group.addSettingCard(self.info_label)

        # add setting group to expand layout
        self.expand_layout.setSpacing(28)
        self.expand_layout.setContentsMargins(30, 10, 30, 0)
        self.expand_layout.addWidget(self.game_group)
        self.expand_layout.addWidget(self.stamina_group)
        self.expand_layout.addWidget(self.universe_group)
        self.expand_layout.addWidget(self.more_group)

    def __on_game_path_clicked(self):
        """game path clicked slot"""
        from PySide6.QtWidgets import QFileDialog
        dialog = QFileDialog.getOpenFileName(self.window(), "选择游戏路径")
        if not dialog:
            return
        filename = dialog.__str__().split(',')[0]
        filename = filename.replace("(", "")
        filename = filename.replace("'", "")
        if not filename:
            return
        self.game_path.setContent(filename)
        cfg.set(cfg.game_path, filename)

    def __on_open_map_clicked(self):
        """open map clicked slot"""
        from qfluentwidgets import MessageBox

        class SetKeyBoardDialog(MessageBox):
            def __init__(self, title, content, parent, key):
                super().__init__(title, content, parent)
                self.key = key

            def keyPressEvent(self, event):
                key = event.text()
                self.key = key
                self.contentLabel.setText(f"当前为: {key}")

        dialog = SetKeyBoardDialog("设置打开地图的按键", f"当前为: {cfg.open_map.value}", self.window(),
                                   cfg.open_map.value)
        dialog.show()
        dialog.yesSignal.connect(lambda: cfg.set(cfg.open_map, dialog.key))
        dialog.exec()
        self.open_map.setContent(f"当前为: {cfg.open_map.value}")

    def __connect_signal_to_slot(self):
        # game group
        self.game_path.clicked.connect(self.__on_game_path_clicked)
        self.open_map.clicked.connect(self.__on_open_map_clicked)

        # stamina

        # universe

        # more

    def __init_widget(self):
        self.__init_layout()
        self.__connect_signal_to_slot()
