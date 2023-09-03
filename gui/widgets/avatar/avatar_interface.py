from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame
from qfluentwidgets import FlowLayout

from .ui.avatar_widget import Ui_Frame
from .avatar_group import AvatarGroup


def get_img_path(name: str) -> str:
    import os
    f = os.path.dirname(__file__)
    path = os.path.join(f, "img", name)
    return path


class AvatarInterface(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("NanJun")
        self.setStyleSheet(
            """
            background: rgb(250, 250, 250);
            border: none;
            border-radius:10px;
            """
        )
        self.setupUi(self)
        self.avatar_layout1 = FlowLayout()  # dev members
        self.avatar_layout2 = FlowLayout()  # acknowledgements

        self.__init_widget()

    def __init_layout(self):
        self.dev_members_layout.addLayout(self.avatar_layout1)
        self.acknowledgements_layout.addLayout(self.avatar_layout2)

        # add dev members to layout
        self.avatar_layout1.addWidget(self.NanJun)  # NanJun is the main developer of this project

        # add acknowledgements to layout
        self.avatar_layout2.addWidget(self.zhiyiYo)  # zhiyiYo is the main developer of PySide6-Fluent-Widgets
        self.avatar_layout2.addWidget(self.CHNZYX)

    def __init_avatar(self):
        # NanJun
        self.NanJun = AvatarGroup(self.scroll_widget)
        self.NanJun.set_name("NanJun")
        self.NanJun.set_pixmap(QPixmap(get_img_path("NanJun.png")))
        self.NanJun.set_url(r"https://github.com/JunNanLYS")

        # zhiyiYo
        self.zhiyiYo = AvatarGroup(self.scroll_widget)
        self.zhiyiYo.set_name("zhiyiYo")
        self.zhiyiYo.set_pixmap(QPixmap(get_img_path("zhiyiYo.png")))
        self.zhiyiYo.set_url(r"https://github.com/zhiyiYo")

        # CHNZYX
        self.CHNZYX = AvatarGroup(self.scroll_widget)
        self.CHNZYX.set_name("CHNZYX")
        self.CHNZYX.set_pixmap(QPixmap(get_img_path("CHNZYX.png")))
        self.CHNZYX.set_url(r"https://github.com/CHNZYX")

    def __init_widget(self):
        self.__init_avatar()
        self.__init_layout()
