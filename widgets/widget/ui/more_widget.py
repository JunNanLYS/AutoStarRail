# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'more_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from qfluentwidgets import (PlainTextEdit, PushButton, SmoothScrollArea)

from ..card import Card


class MoreWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(571, 452)
        self.horizontalLayout_2 = QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SmoothScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 569, 450))
        self.verticalLayout = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 20, 10, 20)
        self.commissionCard = Card(self.scrollAreaWidget)
        self.commissionCard.setObjectName(u"commissionCard")
        self.horizontalLayout = QHBoxLayout(self.commissionCard)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.commissionButton = PushButton(self.commissionCard)
        self.commissionButton.setObjectName(u"commissionButton")

        self.horizontalLayout.addWidget(self.commissionButton)


        self.verticalLayout.addWidget(self.commissionCard)

        self.mandateCard = Card(self.scrollAreaWidget)
        self.mandateCard.setObjectName(u"mandateCard")
        self.horizontalLayout_3 = QHBoxLayout(self.mandateCard)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.mandateButton = PushButton(self.mandateCard)
        self.mandateButton.setObjectName(u"mandateButton")

        self.horizontalLayout_3.addWidget(self.mandateButton)


        self.verticalLayout.addWidget(self.mandateCard)

        self.widget = Card(self.scrollAreaWidget)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.autoPlainTextEdit = PlainTextEdit(self.widget)
        self.autoPlainTextEdit.setObjectName(u"autoPlainTextEdit")

        self.verticalLayout_2.addWidget(self.autoPlainTextEdit)

        self.autoButton = PushButton(self.widget)
        self.autoButton.setObjectName(u"autoButton")

        self.verticalLayout_2.addWidget(self.autoButton)


        self.verticalLayout.addWidget(self.widget)

        self.verticalSpacer = QSpacerItem(20, 303, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.commissionButton.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u9886\u53d6\u59d4\u6258", None))
        self.mandateButton.setText(QCoreApplication.translate("Form", u"\u5b8c\u6210\u6bcf\u65e5\u4efb\u52a1", None))
        self.autoPlainTextEdit.setPlainText(QCoreApplication.translate("Form", u"\u4ec0\u4e48\u60c5\u51b5\u9002\u5408\u4f7f\u7528\u8be5\u529f\u80fd\uff1f\n"
"1. \u60f3\u8981\u6240\u6709\u529f\u80fd\u4e00\u952e\u6267\u884c\u5230\u4f4d\n"
"2. \u4e0d\u60f3\u81ea\u5df1\u50bb\u50bb\u7684\u7b49\u5f85\u7a0b\u5e8f\u6267\u884c\u7ed3\u675f\n"
"3. ", None))
        self.autoButton.setText(QCoreApplication.translate("Form", u"\u4e00\u952e\u5f00\u59cb\u81ea\u52a8", None))
    # retranslateUi

