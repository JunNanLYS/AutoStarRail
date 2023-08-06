import os

from PySide6.QtGui import QAction, QBrush, QColor, QPixmap
from PySide6.QtWidgets import QHBoxLayout
from qfluentwidgets import RoundMenu, PixmapLabel
from qframelesswindow import FramelessDialog

from widgets import WidgetBase
from utils.tool import PathTool
from .ui.info_widget import InfoWidgetUi
from .card import Card


class QRWindow(FramelessDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__init_widget()
        self.resize(1200, 600)

    def resizeEvent(self, e):
        super().resizeEvent(e)
        self.background_widget.resize(self.width(), self.height() - self.titleBar.height())
        print(e.size())

    def __init_widget(self):
        # 背景
        self.background_widget = WidgetBase(self, False)
        self.background_widget.move(0, self.titleBar.height())
        self.background_widget.resize(self.width(), self.height() - self.titleBar.height())
        self.background_widget.setBrush(QBrush(QColor(240, 240, 240)))

        # 布局
        self.hBoxLayout = QHBoxLayout(self.background_widget)
        self.hBoxLayout.setContentsMargins(5, 0, 5, 0)
        self.hBoxLayout.setSpacing(20)

        # 二维码卡片
        self.wechat_card = Card(self.background_widget)
        self.wechat_card_layout = QHBoxLayout(self.wechat_card)
        self.wechat_card_layout.setContentsMargins(5, 5, 5, 5)
        self.alipay_card = Card(self.background_widget)
        self.alipay_card_layout = QHBoxLayout(self.alipay_card)
        self.alipay_card_layout.setContentsMargins(5, 5, 5, 5)

        # 二维码
        self.wechat_qr = PixmapLabel(self.wechat_card)
        self.alipay_qr = PixmapLabel(self.alipay_card)
        self.wechat_qr.setPixmap(QPixmap(os.path.join(
            PathTool.get_root_path(), r"images\QR\wechatQR.png")))
        self.alipay_qr.setPixmap(QPixmap(os.path.join(
            PathTool.get_root_path(), r"images\QR\alipayQR.png")))

        self.wechat_card.sizeChange.connect(
            lambda: self.wechat_qr.setFixedSize(self.wechat_card.width() - 20,
                                                self.wechat_card.height() - 20)
        )
        self.alipay_card.sizeChange.connect(
            lambda: self.alipay_qr.setFixedSize(self.alipay_card.width() - 20,
                                                self.alipay_card.height() - 20)
        )

        # 二维码添加进布局
        self.hBoxLayout.addWidget(self.wechat_card)
        self.hBoxLayout.addWidget(self.alipay_card)

        self.wechat_card_layout.addWidget(self.wechat_qr)
        self.alipay_card_layout.addWidget(self.alipay_qr)


def show_qr_widget():
    """
    显示赞助窗口
    """
    qr_window = QRWindow()
    qr_window.show()


class InfoWidget(WidgetBase, InfoWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def __init_widget(self):
        # 按钮连接到项目主页
        self.githubButton.setUrl("https://github.com/zjnGitHub/AutoStarRail")

        # 设置下拉按钮
        menu = RoundMenu(self)
        self.all_action = QAction("查看全部信息")
        self.universe_action = QAction("查看模拟宇宙信息")
        menu.addActions([
            self.all_action,
            self.universe_action
        ])
        self.viewInfoButton.setMenu(menu)
        self.viewInfoButton.setText("查看信息")

        self.QRButton.clicked.connect(show_qr_widget)
