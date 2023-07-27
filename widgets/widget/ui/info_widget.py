# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QVBoxLayout)
from qfluentwidgets import (BodyLabel, PixmapLabel, TitleLabel)

from widgets import WidgetBase


class InfoWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(602, 519)
        self.vBoxLayout = QVBoxLayout(Form)
        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setObjectName(u"vBoxLayout")
        self.vBoxLayout.setContentsMargins(20, 10, 20, 10)
        self.titleLabel = TitleLabel(Form)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.vBoxLayout.addWidget(self.titleLabel)

        self.payCard = WidgetBase(Form)
        self.payCard.setObjectName(u"payCard")
        self.payCardLayout = QVBoxLayout(self.payCard)
        self.payCardLayout.setSpacing(10)
        self.payCardLayout.setObjectName(u"payCardLayout")
        self.payCardLayout.setContentsMargins(10, 10, 10, 10)
        self.payLabel = BodyLabel(self.payCard)
        self.payLabel.setObjectName(u"payLabel")
        self.payLabel.setAlignment(Qt.AlignCenter)

        self.payCardLayout.addWidget(self.payLabel)

        self.QRCardLayout = QHBoxLayout()
        self.QRCardLayout.setSpacing(10)
        self.QRCardLayout.setObjectName(u"QRCardLayout")
        self.QRCardLayout.setContentsMargins(10, 10, 10, 10)
        self.wechatQRCard = WidgetBase(self.payCard)
        self.wechatQRCard.setObjectName(u"wechatQRCard")
        self.wechatCardLayout = QVBoxLayout(self.wechatQRCard)
        self.wechatCardLayout.setSpacing(0)
        self.wechatCardLayout.setObjectName(u"wechatCardLayout")
        self.wechatCardLayout.setContentsMargins(5, 5, 5, 5)
        self.wechatLabel = BodyLabel(self.wechatQRCard)
        self.wechatLabel.setObjectName(u"wechatLabel")
        self.wechatLabel.setAlignment(Qt.AlignCenter)

        self.wechatCardLayout.addWidget(self.wechatLabel)

        self.wechatQRImage = PixmapLabel(self.wechatQRCard)
        self.wechatQRImage.setObjectName(u"wechatQRImage")

        self.wechatCardLayout.addWidget(self.wechatQRImage)

        self.wechatCardLayout.setStretch(1, 2)

        self.QRCardLayout.addWidget(self.wechatQRCard)

        self.alipayQRCard = WidgetBase(self.payCard)
        self.alipayQRCard.setObjectName(u"alipayQRCard")
        self.alipayCardLayout = QVBoxLayout(self.alipayQRCard)
        self.alipayCardLayout.setSpacing(0)
        self.alipayCardLayout.setObjectName(u"alipayCardLayout")
        self.alipayCardLayout.setContentsMargins(5, 5, 5, 5)
        self.alipayLabel = BodyLabel(self.alipayQRCard)
        self.alipayLabel.setObjectName(u"alipayLabel")
        self.alipayLabel.setAlignment(Qt.AlignCenter)

        self.alipayCardLayout.addWidget(self.alipayLabel)

        self.alipayQRImage = PixmapLabel(self.alipayQRCard)
        self.alipayQRImage.setObjectName(u"alipayQRImage")

        self.alipayCardLayout.addWidget(self.alipayQRImage)

        self.alipayCardLayout.setStretch(1, 2)

        self.QRCardLayout.addWidget(self.alipayQRCard)

        self.payCardLayout.addLayout(self.QRCardLayout)

        self.vBoxLayout.addWidget(self.payCard)

        self.infoCard = WidgetBase(Form)
        self.infoCard.setObjectName(u"infoCard")
        self.verticalLayout = QVBoxLayout(self.infoCard)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.label1 = BodyLabel(self.infoCard)
        self.label1.setObjectName(u"label1")

        self.verticalLayout.addWidget(self.label1)

        self.label2 = BodyLabel(self.infoCard)
        self.label2.setObjectName(u"label2")

        self.verticalLayout.addWidget(self.label2)

        self.label3 = BodyLabel(self.infoCard)
        self.label3.setObjectName(u"label3")

        self.verticalLayout.addWidget(self.label3)

        self.vBoxLayout.addWidget(self.infoCard)

        self.vBoxLayout.setStretch(1, 2)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLabel.setText(
            QCoreApplication.translate("Form", u"Auto\u5d29\u574f\uff1a\u661f\u7a79\u94c1\u9053", None))
        self.payLabel.setText(
            QCoreApplication.translate("Form", u"\u8d5e\u8d4f\u4e00\u4e0b\u66f4\u6709\u52a8\u529b\uff01", None))
        self.wechatLabel.setText(QCoreApplication.translate("Form", u"\u5fae\u4fe1", None))
        self.alipayLabel.setText(QCoreApplication.translate("Form", u"\u652f\u4ed8\u5b9d", None))
        self.label1.setText(QCoreApplication.translate("Form",
                                                       u"1. \u6b64\u4e3a\u514d\u8d39\u5f00\u6e90\u9879\u76ee\uff0c\u8bf7\u52ff\u7528\u6b64\u9879\u76ee\u8fdd\u6cd5\u72af\u7f6a",
                                                       None))
        self.label2.setText(QCoreApplication.translate("Form",
                                                       u"2. \u5982\u679c\u4f60\u662f\u4ece\u522b\u7684\u5730\u65b9\u8d2d\u4e70\u7684\uff0c\u90a3\u4e48\u606d\u559c\u4f60\u88ab\u9a97\u4e86",
                                                       None))
        self.label3.setText(QCoreApplication.translate("Form",
                                                       u"3. \u9879\u76ee\u81f4\u529b\u4e8e\u7ef4\u62a4\u4e2a\u4eba\u8eab\u5fc3\u5065\u5eb7\uff0c\u4e0d\u518d\u56e0\u4e3a\u6ca1\u6709\u6e05\u4f53\u529b\u7b49\u7410\u4e8b\u800c\u70e6\u607c",
                                                       None))
    # retranslateUi
