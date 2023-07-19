# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'feature_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from qfluentwidgets import (BodyLabel, PushButton, SmoothScrollArea, SpinBox,
                            SubtitleLabel)

from ..card import FeatureCard


class FeatureWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(628, 651)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SmoothScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 626, 697))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.calyxGoldCard = FeatureCard(self.scrollAreaWidget)
        self.calyxGoldCard.setObjectName(u"calyxGoldCard")
        self.verticalLayout = QVBoxLayout(self.calyxGoldCard)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.calyxGoldLabel = SubtitleLabel(self.calyxGoldCard)
        self.calyxGoldLabel.setObjectName(u"calyxGoldLabel")

        self.verticalLayout.addWidget(self.calyxGoldLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.characterEXPLabel = BodyLabel(self.calyxGoldCard)
        self.characterEXPLabel.setObjectName(u"characterEXPLabel")

        self.horizontalLayout.addWidget(self.characterEXPLabel)

        self.characterEXPSpinBox = SpinBox(self.calyxGoldCard)
        self.characterEXPSpinBox.setObjectName(u"characterEXPSpinBox")

        self.horizontalLayout.addWidget(self.characterEXPSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.coneEXPLabel = BodyLabel(self.calyxGoldCard)
        self.coneEXPLabel.setObjectName(u"coneEXPLabel")

        self.horizontalLayout_2.addWidget(self.coneEXPLabel)

        self.coneEXPSpinBox = SpinBox(self.calyxGoldCard)
        self.coneEXPSpinBox.setObjectName(u"coneEXPSpinBox")

        self.horizontalLayout_2.addWidget(self.coneEXPSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.creditLabel = BodyLabel(self.calyxGoldCard)
        self.creditLabel.setObjectName(u"creditLabel")

        self.horizontalLayout_3.addWidget(self.creditLabel)

        self.creditSpinBox = SpinBox(self.calyxGoldCard)
        self.creditSpinBox.setObjectName(u"creditSpinBox")

        self.horizontalLayout_3.addWidget(self.creditSpinBox)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.verticalLayout_3.addWidget(self.calyxGoldCard)

        self.calyxRedCard = FeatureCard(self.scrollAreaWidget)
        self.calyxRedCard.setObjectName(u"calyxRedCard")
        self.verticalLayout_2 = QVBoxLayout(self.calyxRedCard)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.calyxRedLabel = SubtitleLabel(self.calyxRedCard)
        self.calyxRedLabel.setObjectName(u"calyxRedLabel")

        self.verticalLayout_2.addWidget(self.calyxRedLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.desrructionLabel = BodyLabel(self.calyxRedCard)
        self.desrructionLabel.setObjectName(u"desrructionLabel")

        self.horizontalLayout_4.addWidget(self.desrructionLabel)

        self.desrructionSpinBox = SpinBox(self.calyxRedCard)
        self.desrructionSpinBox.setObjectName(u"desrructionSpinBox")

        self.horizontalLayout_4.addWidget(self.desrructionSpinBox)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BodyLabel_5 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout_5.addWidget(self.BodyLabel_5)

        self.SpinBox_2 = SpinBox(self.calyxRedCard)
        self.SpinBox_2.setObjectName(u"SpinBox_2")

        self.horizontalLayout_5.addWidget(self.SpinBox_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BodyLabel_6 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.horizontalLayout_6.addWidget(self.BodyLabel_6)

        self.SpinBox_3 = SpinBox(self.calyxRedCard)
        self.SpinBox_3.setObjectName(u"SpinBox_3")

        self.horizontalLayout_6.addWidget(self.SpinBox_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BodyLabel_7 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.horizontalLayout_7.addWidget(self.BodyLabel_7)

        self.SpinBox_7 = SpinBox(self.calyxRedCard)
        self.SpinBox_7.setObjectName(u"SpinBox_7")

        self.horizontalLayout_7.addWidget(self.SpinBox_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BodyLabel_8 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.horizontalLayout_8.addWidget(self.BodyLabel_8)

        self.SpinBox_8 = SpinBox(self.calyxRedCard)
        self.SpinBox_8.setObjectName(u"SpinBox_8")

        self.horizontalLayout_8.addWidget(self.SpinBox_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.BodyLabel_9 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")

        self.horizontalLayout_9.addWidget(self.BodyLabel_9)

        self.SpinBox_9 = SpinBox(self.calyxRedCard)
        self.SpinBox_9.setObjectName(u"SpinBox_9")

        self.horizontalLayout_9.addWidget(self.SpinBox_9)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)

        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.BodyLabel_10 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")

        self.horizontalLayout_10.addWidget(self.BodyLabel_10)

        self.SpinBox_10 = SpinBox(self.calyxRedCard)
        self.SpinBox_10.setObjectName(u"SpinBox_10")

        self.horizontalLayout_10.addWidget(self.SpinBox_10)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)

        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 1)

        self.verticalLayout_3.addWidget(self.calyxRedCard)

        self.shadowCard = FeatureCard(self.scrollAreaWidget)
        self.shadowCard.setObjectName(u"shadowCard")
        self.verticalLayout_5 = QVBoxLayout(self.shadowCard)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.shadowLabel = SubtitleLabel(self.shadowCard)
        self.shadowLabel.setObjectName(u"shadowLabel")

        self.verticalLayout_5.addWidget(self.shadowLabel)

        self.verticalLayout_3.addWidget(self.shadowCard)

        self.cavernCard = FeatureCard(self.scrollAreaWidget)
        self.cavernCard.setObjectName(u"cavernCard")
        self.verticalLayout_6 = QVBoxLayout(self.cavernCard)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.cavernLabel = SubtitleLabel(self.cavernCard)
        self.cavernLabel.setObjectName(u"cavernLabel")

        self.verticalLayout_6.addWidget(self.cavernLabel)

        self.verticalLayout_3.addWidget(self.cavernCard)

        self.warCard = FeatureCard(self.scrollAreaWidget)
        self.warCard.setObjectName(u"warCard")
        self.verticalLayout_7 = QVBoxLayout(self.warCard)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.warLabel = SubtitleLabel(self.warCard)
        self.warLabel.setObjectName(u"warLabel")

        self.verticalLayout_7.addWidget(self.warLabel)

        self.verticalLayout_3.addWidget(self.warCard)

        self.staminaButton = PushButton(self.scrollAreaWidget)
        self.staminaButton.setObjectName(u"staminaButton")

        self.verticalLayout_3.addWidget(self.staminaButton)

        self.vSpacer = QSpacerItem(0, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.calyxGoldLabel.setText(QCoreApplication.translate("Form", u"\u62df\u9020\u82b1\u843c(\u91d1)", None))
        self.characterEXPLabel.setText(QCoreApplication.translate("Form", u"\u89d2\u8272\u7ecf\u9a8c", None))
        self.coneEXPLabel.setText(QCoreApplication.translate("Form", u"\u5149\u9525\u7ecf\u9a8c", None))
        self.creditLabel.setText(QCoreApplication.translate("Form", u"\u4fe1\u7528\u70b9", None))
        self.calyxRedLabel.setText(QCoreApplication.translate("Form", u"\u62df\u9020\u82b1\u843c(\u8d64)", None))
        self.desrructionLabel.setText(QCoreApplication.translate("Form", u"\u6bc1\u706d", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5b58\u62a4", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u5de1\u730e", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4e30\u9976", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Form", u"\u667a\u8bc6", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Form", u"\u540c\u8c10", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Form", u"\u865a\u65e0", None))
        self.shadowLabel.setText(QCoreApplication.translate("Form", u"\u51dd\u6ede\u865a\u5f71", None))
        self.cavernLabel.setText(QCoreApplication.translate("Form", u"\u4fb5\u8680\u96a7\u6d1e", None))
        self.warLabel.setText(QCoreApplication.translate("Form", u"\u5386\u6218\u56de\u54cd", None))
        self.staminaButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7406\u5f00\u62d3\u529b", None))
    # retranslateUi
