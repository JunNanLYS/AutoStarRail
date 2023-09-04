from PySide6.QtWidgets import QFrame
from qfluentwidgets import FlowLayout

from .ui.script_widget import Ui_Frame
from .info_card import InfoCard
from .stamina_window import StaminaWindow
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

        self.stamina_window = StaminaWindow()

        self.__init_widget()

    def __connect_signal_to_slot(self):
        self.stamina_card.clicked.connect(self.stamina_window.show)
        self.stamina_window.button_yes.clicked.connect(self.__on_stamina_window_clicked_slot)

    def __on_stamina_window_clicked_slot(self):
        stamina = self.stamina_window.get_stamina()
        cfg.set(cfg.last_stamina, stamina)
        sum_stamina = cfg.sum_stamina
        self.stamina_card.set_info("已设置体力", str(sum_stamina))
        self.stamina_card.set_info("占比", f"{round(sum_stamina / 240 * 100, 1)}%")

    def __init_layout(self):
        self.flow_layout.addWidget(self.stamina_card)
        self.flow_layout.addWidget(self.universe_card)
        self.flow_layout.addWidget(self.commission_card)
        self.flow_layout.addWidget(self.daily_card)
        self.flow_layout.addWidget(self.world_card)

    def __init_info_card(self):
        # stamina card
        sum_stamina = cfg.sum_stamina
        self.stamina_card.add_info("已设置体力", str(sum_stamina))
        self.stamina_card.add_info("占比", f"{round(sum_stamina / 240 * 100, 1)}%")
        self.stamina_card.add_info("距离上次", "1天1时1分")
        self.stamina_card.add_info("运行", "False")

        # universe card
        self.universe_card.add_info("上次运行", "6")
        self.universe_card.add_info("角度误差", "1.0")
        self.universe_card.add_info("本周运行次数", "34")
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

    def __init_widget(self):
        self.__init_layout()
        self.__init_info_card()
        self.__connect_signal_to_slot()
