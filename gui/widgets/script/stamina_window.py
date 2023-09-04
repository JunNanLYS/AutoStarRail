import os

from qfluentwidgets import SimpleCardWidget, ImageLabel, SpinBox, FlowLayout
from qframelesswindow import FramelessDialog
from PySide6.QtWidgets import QHBoxLayout

import config
from .ui.stamina import Ui_Frame


class StaminaCard(SimpleCardWidget):
    def __init__(self, img: str, parent):
        super().__init__(parent)
        self.layout = QHBoxLayout(self)
        self.image = ImageLabel(img, self)
        self.spin_box = SpinBox(self)

        # add to layout
        self.layout.addWidget(self.image)
        self.layout.addWidget(self.spin_box)

    @property
    def value(self):
        return self.spin_box.value()


class StaminaWindow(FramelessDialog, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._path = os.path.dirname(__file__)
        self._dict = dict()

        # creat a layout on view of card
        self.calyx_gold_card_layout = FlowLayout()
        self.calyx_red_card_layout = FlowLayout()
        self.shadow_card_layout = FlowLayout()
        self.cavern_card_layout = FlowLayout()
        self.echo_card_layout = FlowLayout()

        self.__init_widget()
        self.titleBar.raise_()

    def get_stamina(self):
        """获取每个参数"""
        lis = self.cavern_card.view.children() + self.calyx_gold_card.view.children() + \
              self.calyx_red_card.view.children() + self.echo_card.view.children() + \
              self.shadow_card.view.children()

        for widget in lis:
            if isinstance(widget, StaminaCard):
                self._dict[widget.objectName()] = widget.value

        return self._dict

    def __add_card_to_layout(self, name):
        from config import cfg
        NAME_TO_VIEW = {"calyx_gold": self.calyx_gold_card.view,
                        "calyx_red": self.calyx_red_card.view,
                        "shadow": self.shadow_card.view,
                        "cavern": self.cavern_card.view,
                        "echo": self.echo_card.view}
        NAME_TO_LAYOUT = {"calyx_gold": self.calyx_gold_card_layout,
                          "calyx_red": self.calyx_red_card_layout,
                          "shadow": self.shadow_card_layout,
                          "cavern": self.cavern_card_layout,
                          "echo": self.echo_card_layout}
        parent = NAME_TO_VIEW[name]
        layout = NAME_TO_LAYOUT[name]
        path = self.__get_img_root_path(name)
        n = len(os.listdir(path))
        for i in range(1, n + 1):
            card = StaminaCard(os.path.join(path, str(i) + '.png'), parent)
            object_name = name + "_" + str(i)
            card.setObjectName(object_name)
            card.spin_box.setValue(cfg.last_stamina.value.get(object_name, 0))
            layout.addWidget(card)

    def __connect_signal_to_slot(self):
        self.button_yes.clicked.connect(self.hide)
        self.button_no.clicked.connect(self.hide)

    def __get_img_root_path(self, name):
        return os.path.join(self._path, "img", name)

    def __init_layout(self):
        # add flow layout to card view layout
        self.calyx_gold_card.viewLayout.addLayout(self.calyx_gold_card_layout)
        self.calyx_red_card.viewLayout.addLayout(self.calyx_red_card_layout)
        self.shadow_card.viewLayout.addLayout(self.shadow_card_layout)
        self.cavern_card.viewLayout.addLayout(self.cavern_card_layout)
        self.echo_card.viewLayout.addLayout(self.echo_card_layout)

        self.__add_card_to_layout("calyx_gold")
        self.__add_card_to_layout("calyx_red")
        self.__add_card_to_layout("shadow")
        self.__add_card_to_layout("cavern")
        self.__add_card_to_layout("echo")

    def __init_widget(self):
        self.__init_layout()
        self.__connect_signal_to_slot()

        self.calyx_gold_card.setTitle("拟造花萼(金)")
        self.calyx_red_card.setTitle("拟造花萼(红)")
        self.shadow_card.setTitle("凝滞虚影")
        self.cavern_card.setTitle("侵蚀隧道")
        self.echo_card.setTitle("历战回响")

        self.titleBar.closeBtn.clicked.disconnect(self.close)
        self.titleBar.closeBtn.clicked.connect(self.hide)

        self.resize(1240, 800)
