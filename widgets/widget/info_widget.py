from PySide6.QtCore import QSize
from PySide6.QtGui import QBrush, QColor, QPixmap, Qt
from PySide6.QtWidgets import QGraphicsDropShadowEffect

from widgets import WidgetBase
from .ui.info_widget import InfoWidgetUi


class InfoWidget(WidgetBase, InfoWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

        # 连接信号至槽函数(connect signal to slot)
        self.wechatQRCard.sizeChange.connect(self.setWechatQRSize)
        self.alipayQRCard.sizeChange.connect(self.setAlipayQRSize)

    def __init_widget(self):
        # 设置卡片颜色(set card brush)
        self.payCard.setBrush(QBrush(QColor(253, 253, 253)))
        self.infoCard.setBrush(QBrush(QColor(253, 253, 253)))

        # 支付卡片居中
        self.wechatCardLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.alipayCardLayout.setAlignment(Qt.AlignmentFlag.AlignTop)

        cards = [self.wechatQRCard, self.alipayQRCard, self.infoCard]
        for card in cards:
            shadow = QGraphicsDropShadowEffect(card)
            shadow.setColor(QColor(63, 63, 63, 180))
            shadow.setOffset(0, 0)
            shadow.setBlurRadius(10)
            card.setGraphicsEffect(shadow)

        # QR
        wechat = QPixmap("F:/AutoStarRail/images/QR/wechatQR.png")
        alipay = QPixmap("F:/AutoStarRail/images/QR/alipayQR.png")
        self.wechatQRImage.setPixmap(wechat)
        self.alipayQRImage.setPixmap(alipay)
        self.wechatQRImage.setFixedSize(500, 500)
        self.alipayQRImage.setFixedSize(500, 500)

    def setAlipayQRSize(self, _):
        self.alipayQRImage.setFixedSize(
            self.alipayQRCard.size() - QSize(10, self.alipayLabel.height())
        )

    def setWechatQRSize(self, _):
        self.wechatQRImage.setFixedSize(
            self.wechatQRCard.size() - QSize(10, self.wechatLabel.height())
        )
