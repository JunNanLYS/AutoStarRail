from PySide6.QtWidgets import QFrame
from qfluentwidgets import FlowLayout

from .ui.script_widget import Ui_Frame
from .info_card import InfoCard
from .stamina_window import StaminaWindow
from .universe_window import UniverseWindow
from config import cfg


class ScriptInterface(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("脚本")
        self.setStyleSheet(
            """
            background: rgb(250, 250, 250);
            border: none;
            border-radius:10px;
            """
        )
        self.setupUi(self)
        self.flow_layout = FlowLayout(self.scroll_widget)

        # init info card
        self.stamina_card = InfoCard("体力")
        self.commission_card = InfoCard("委托")
        self.universe_card = InfoCard("模拟宇宙")
        self.daily_card = InfoCard("每日任务")
        self.world_card = InfoCard("世界")
        self.abyss_card = InfoCard("深渊")

        self.stamina_window = StaminaWindow()
        self.universe_window = UniverseWindow()

        self.__init_widget()

    def update_info_card(self):
        """update card"""
        from config import cfg
        # stamina card
        sum_stamina = cfg.sum_stamina
        self.stamina_card.set_info("已设置体力", str(sum_stamina))
        self.stamina_card.set_info("占比", f"{round(sum_stamina / 240 * 100, 1)}%")
        self.stamina_card.set_info("上次运行", cfg.last_stamina_time.value)

        # universe card
        self.universe_card.set_info("宇宙", cfg.get(cfg.universe_number))
        self.universe_card.set_info("命途", cfg.get(cfg.universe_fate))
        self.universe_card.set_info("难度", cfg.get(cfg.universe_difficult))
        self.universe_card.set_info("角度误差", cfg.get(cfg.universe_angle))
        self.universe_card.set_info("计数", cfg.get(cfg.universe_count))

    def __connect_signal_to_slot(self):
        self.stamina_card.clicked.connect(self.stamina_window.show)
        self.stamina_window.button_yes.clicked.connect(self.update_info_card)

        self.universe_card.clicked.connect(self.universe_window.show)
        self.universe_window.button_yes.clicked.connect(self.update_info_card)

    def __init_layout(self):
        self.flow_layout.addWidget(self.stamina_card)
        self.flow_layout.addWidget(self.universe_card)
        self.flow_layout.addWidget(self.commission_card)
        self.flow_layout.addWidget(self.daily_card)
        self.flow_layout.addWidget(self.world_card)
        self.flow_layout.addWidget(self.abyss_card)

    def __init_info_card(self):
        # stamina card
        sum_stamina = cfg.sum_stamina
        self.stamina_card.add_info("已设置体力", sum_stamina)
        self.stamina_card.add_info("占比", f"{round(sum_stamina / 240 * 100, 1)}%")
        self.stamina_card.add_info("上次运行", cfg.last_stamina_time.value)
        self.stamina_card.add_info("运行", "False")

        # universe card
        self.universe_card.add_info("宇宙", cfg.get(cfg.universe_number))
        self.universe_card.add_info("命途", cfg.get(cfg.universe_fate))
        self.universe_card.add_info("难度", cfg.get(cfg.universe_difficult))
        self.universe_card.add_info("角度误差", cfg.get(cfg.universe_angle))
        self.universe_card.add_info("计数", cfg.get(cfg.universe_count))
        self.universe_card.add_info("运行", "False")

        # commission card
        self.commission_card.add_info("状态", "待领取")
        self.commission_card.add_info("距离上次", "1天1时1分")
        self.commission_card.add_info("运行", "False")

        # daily card
        self.daily_card.add_info("上次运行", "...")
        self.daily_card.add_info("运行", "False")

        # world card
        self.world_card.add_info("起始", "空间站-基座舱段-1")
        self.world_card.add_info("角度误差", "1.0")
        self.world_card.add_info("距离上次", "1天1时1分")
        self.world_card.add_info("运行", "False")

        # abyss card
        self.abyss_card.add_info("配队1", "1 2 3 4")
        self.abyss_card.add_info("配队2", "5 6 7 8")
        self.abyss_card.add_info("...", "...")

    def __init_widget(self):
        self.__init_layout()
        self.__init_info_card()
        self.__connect_signal_to_slot()
