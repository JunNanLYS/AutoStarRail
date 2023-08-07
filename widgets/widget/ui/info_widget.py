# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QLayout, QSizePolicy,
                               QSpacerItem, QVBoxLayout)
from qfluentwidgets import (BodyLabel, DropDownPushButton, HyperlinkButton, PushButton,
                            TitleLabel)

from ..card import Card


class InfoWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(602, 519)
        self.vBoxLayout = QVBoxLayout(Form)
        self.vBoxLayout.setSpacing(10)
        self.vBoxLayout.setObjectName(u"vBoxLayout")
        self.vBoxLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.vBoxLayout.setContentsMargins(20, 10, 20, 10)
        self.titleLabel = TitleLabel(Form)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.vBoxLayout.addWidget(self.titleLabel)

        self.infoCard = Card(Form)
        self.infoCard.setObjectName(u"infoCard")
        self.verticalLayout = QVBoxLayout(self.infoCard)
        self.verticalLayout.setSpacing(5)
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

        self.label4 = BodyLabel(self.infoCard)
        self.label4.setObjectName(u"label4")

        self.verticalLayout.addWidget(self.label4)

        self.vBoxLayout.addWidget(self.infoCard)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.githubButton = HyperlinkButton(Form)
        self.githubButton.setObjectName(u"githubButton")

        self.horizontalLayout_2.addWidget(self.githubButton)

        self.viewInfoButton = DropDownPushButton(Form)
        self.viewInfoButton.setObjectName(u"viewInfoButton")

        self.horizontalLayout_2.addWidget(self.viewInfoButton)

        self.vBoxLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 0, -1, -1)
        self.viewLogButton = PushButton(Form)
        self.viewLogButton.setObjectName(u"viewLogButton")

        self.horizontalLayout.addWidget(self.viewLogButton)

        self.saveLogButton = PushButton(Form)
        self.saveLogButton.setObjectName(u"saveLogButton")

        self.horizontalLayout.addWidget(self.saveLogButton)

        self.QRButton = PushButton(Form)
        self.QRButton.setObjectName(u"QRButton")

        self.horizontalLayout.addWidget(self.QRButton)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)

        self.vBoxLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.vBoxLayout.addItem(self.verticalSpacer)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLabel.setText(
            QCoreApplication.translate("Form", u"Auto\u5d29\u574f\uff1a\u661f\u7a79\u94c1\u9053", None))
        self.label1.setText(QCoreApplication.translate("Form",
                                                       u"1. \u6b64\u4e3a\u514d\u8d39\u5f00\u6e90\u9879\u76ee\uff0c\u8bf7\u52ff\u7528\u6b64\u9879\u76ee\u8fdd\u6cd5\u72af\u7f6a",
                                                       None))
        self.label2.setText(QCoreApplication.translate("Form",
                                                       u"2. \u5982\u679c\u4f60\u662f\u4ece\u522b\u7684\u5730\u65b9\u8d2d\u4e70\u7684\uff0c\u90a3\u4e48\u606d\u559c\u4f60\u88ab\u9a97\u4e86\uff0c\u8bf7\u7acb\u5373\u9000\u6b3e",
                                                       None))
        self.label3.setText(QCoreApplication.translate("Form",
                                                       u"3. \u9879\u76ee\u81f4\u529b\u4e8e\u7ef4\u62a4\u4e2a\u4eba\u8eab\u5fc3\u5065\u5eb7\uff0c\u8ba9\u811a\u672c\u4ee3\u66ff\u4f60\u6253\u5de5\u5c82\u4e0d\u662f\u66f4\u68d2\uff1f",
                                                       None))
        self.label4.setText(QCoreApplication.translate("Form",
                                                       u"4. \u8bf7\u4e0d\u8981\u4f7f\u7528\u8be5\u9879\u76ee\u725f\u53d6\u5229\u76ca\u5426\u5219\u540e\u679c\u81ea\u8d1f",
                                                       None))
        self.githubButton.setText(QCoreApplication.translate("Form", u"\u7ed9\u9879\u76ee\u70b9\u4e2aStar\u2b50", None))
        self.viewInfoButton.setText(QCoreApplication.translate("Form", u"\u67e5\u770b", None))
        self.viewLogButton.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u65e5\u5fd7", None))
        self.saveLogButton.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58\u65e5\u5fd7", None))
        self.QRButton.setText(QCoreApplication.translate("Form", u"\u8bf7\u4f5c\u8005\u559d\u676f\u2615", None))
    # retranslateUi
