# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setting_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from qfluentwidgets import (LineEdit, SmoothScrollArea, SpinBox, StrongBodyLabel,
                            SwitchButton, TitleLabel, ToolButton)

from widgets import WidgetBase


class SettingWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(618, 473)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SmoothScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 616, 471))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 10, 10, 0)
        self.gameCard = WidgetBase(self.scrollAreaWidget)
        self.gameCard.setObjectName(u"gameCard")
        self.verticalLayout_2 = QVBoxLayout(self.gameCard)
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.gameLabel = TitleLabel(self.gameCard)
        self.gameLabel.setObjectName(u"gameLabel")

        self.verticalLayout_2.addWidget(self.gameLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pathLabel = StrongBodyLabel(self.gameCard)
        self.pathLabel.setObjectName(u"pathLabel")

        self.horizontalLayout_3.addWidget(self.pathLabel)

        self.gamePathEdit = LineEdit(self.gameCard)
        self.gamePathEdit.setObjectName(u"gamePathEdit")
        self.gamePathEdit.setMinimumSize(QSize(0, 33))
        self.gamePathEdit.setReadOnly(True)
        self.gamePathEdit.setProperty("transparent", True)

        self.horizontalLayout_3.addWidget(self.gamePathEdit)

        self.gamePathButton = ToolButton(self.gameCard)
        self.gamePathButton.setObjectName(u"gamePathButton")
        self.gamePathButton.setToolButtonStyle(Qt.ToolButtonIconOnly)

        self.horizontalLayout_3.addWidget(self.gamePathButton)

        self.horizontalLayout_3.setStretch(1, 1)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.autofightLabel = StrongBodyLabel(self.gameCard)
        self.autofightLabel.setObjectName(u"autofightLabel")

        self.horizontalLayout_4.addWidget(self.autofightLabel)

        self.autofightButton = SwitchButton(self.gameCard)
        self.autofightButton.setObjectName(u"autofightButton")

        self.horizontalLayout_4.addWidget(self.autofightButton)

        self.horizontalSpacer_3 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.gameCard)

        self.staminaCard = WidgetBase(self.scrollAreaWidget)
        self.staminaCard.setObjectName(u"staminaCard")
        self.verticalLayout = QVBoxLayout(self.staminaCard)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.staminaLabel = TitleLabel(self.staminaCard)
        self.staminaLabel.setObjectName(u"staminaLabel")

        self.verticalLayout.addWidget(self.staminaLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.fuelLabel = StrongBodyLabel(self.staminaCard)
        self.fuelLabel.setObjectName(u"fuelLabel")
        self.fuelLabel.setMinimumSize(QSize(72, 0))
        self.fuelLabel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout.addWidget(self.fuelLabel)

        self.fuelButton = SwitchButton(self.staminaCard)
        self.fuelButton.setObjectName(u"fuelButton")

        self.horizontalLayout.addWidget(self.fuelButton)

        self.fuelSpinBox = SpinBox(self.staminaCard)
        self.fuelSpinBox.setObjectName(u"fuelSpinBox")

        self.horizontalLayout.addWidget(self.fuelSpinBox)

        self.horizontalSpacer = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.powerLabel = StrongBodyLabel(self.staminaCard)
        self.powerLabel.setObjectName(u"powerLabel")
        self.powerLabel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_2.addWidget(self.powerLabel)

        self.powerButton = SwitchButton(self.staminaCard)
        self.powerButton.setObjectName(u"powerButton")

        self.horizontalLayout_2.addWidget(self.powerButton)

        self.powerSpinBox = SpinBox(self.staminaCard)
        self.powerSpinBox.setObjectName(u"powerSpinBox")

        self.horizontalLayout_2.addWidget(self.powerSpinBox)

        self.horizontalSpacer_2 = QSpacerItem(40, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)

        self.verticalLayout_3.addWidget(self.staminaCard)

        self.verticalSpacer = QSpacerItem(0, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout_4.addWidget(self.scrollArea)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.gameLabel.setText(QCoreApplication.translate("Form", u"\u6e38\u620f", None))
        self.pathLabel.setText(QCoreApplication.translate("Form", u"\u661f\u94c1\u542f\u52a8\u5668\u8def\u5f84", None))
        self.gamePathEdit.setText("")
        self.autofightLabel.setText(QCoreApplication.translate("Form",
                                                               u"\u6e38\u620f\u4e2d\u5df2\u5f00\u542f\u81ea\u52a8\u6cbf\u7528\u6218\u6597",
                                                               None))
        self.autofightButton.setOnText(QCoreApplication.translate("Form", u"Yes", None))
        self.autofightButton.setOffText(QCoreApplication.translate("Form", u"No", None))
        self.staminaLabel.setText(QCoreApplication.translate("Form", u"\u4f53\u529b", None))
        self.fuelLabel.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u71c3\u6599", None))
        self.powerLabel.setText(QCoreApplication.translate("Form", u"\u4f7f\u7528\u5f00\u62d3\u529b", None))
    # retranslateUi
