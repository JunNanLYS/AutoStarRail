# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'universe_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QVBoxLayout)
from qfluentwidgets import (BodyLabel, PushButton, SubtitleLabel)

from ..card import Card


class UniverseWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(566, 490)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.widget_2 = Card(Form)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.titleLabel = SubtitleLabel(self.widget_2)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.titleLabel)

        self.label1 = BodyLabel(self.widget_2)
        self.label1.setObjectName(u"label1")

        self.verticalLayout_3.addWidget(self.label1)

        self.label2 = BodyLabel(self.widget_2)
        self.label2.setObjectName(u"label2")

        self.verticalLayout_3.addWidget(self.label2)

        self.label3 = BodyLabel(self.widget_2)
        self.label3.setObjectName(u"label3")

        self.verticalLayout_3.addWidget(self.label3)

        self.verticalLayout.addWidget(self.widget_2)

        self.widget = Card(Form)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.checkButton = PushButton(self.widget)
        self.checkButton.setObjectName(u"checkButton")

        self.verticalLayout_2.addWidget(self.checkButton)

        self.universeButton = PushButton(self.widget)
        self.universeButton.setObjectName(u"universeButton")

        self.verticalLayout_2.addWidget(self.universeButton)

        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.titleLabel.setText(QCoreApplication.translate("Form", u"\u6e29\u99a8\u63d0\u793a", None))
        self.label1.setText(QCoreApplication.translate("Form",
                                                       u"\u7b2c\u4e00\u6b21\u8fd0\u884c\u8bf7\u5148\u6821\u51c6(\u8bf7\u5728\u5e73\u5730\u8fd0\u884c\u6821\u51c6)",
                                                       None))
        self.label2.setText(QCoreApplication.translate("Form",
                                                       u"\u8fd0\u884c\u5c06\u8fdb\u5165\u9ed8\u8ba4\u7684\u6a21\u62df\u5b87\u5b99\uff0c\u82e5\u60f3\u66f4\u6539\u8bf7\u81ea\u884c\u66f4\u6539\u9ed8\u8ba4\u7684\u6a21\u62df\u5b87\u5b99",
                                                       None))
        self.label3.setText(QCoreApplication.translate("Form",
                                                       u"\u89d2\u8272\u5c06\u6309\u7167\u6a21\u62df\u5b87\u5b99\u4e2d\u9ed8\u8ba4\u914d\u961f\u6765(\u5efa\u8bae\u7b2c\u4e00\u4e2a\u89d2\u8272\u653e\u8fdc\u7a0b)",
                                                       None))
        self.checkButton.setText(QCoreApplication.translate("Form", u"\u6821\u51c6", None))
        self.universeButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u81ea\u52a8\u5316", None))
    # retranslateUi
