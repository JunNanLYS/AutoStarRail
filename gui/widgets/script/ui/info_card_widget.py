# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info_card_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject)
from PySide6.QtWidgets import (QGridLayout, QSizePolicy, QSpacerItem,
                               QVBoxLayout)

from qfluentwidgets import (SubtitleLabel)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(276, 185)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.title_label = SubtitleLabel(Form)
        self.title_label.setObjectName(u"title_label")

        self.verticalLayout.addWidget(self.title_label)

        self.grid_layout = QGridLayout()
        self.grid_layout.setObjectName(u"grid_layout")
        self.grid_layout.setHorizontalSpacing(5)
        self.grid_layout.setVerticalSpacing(15)
        self.grid_layout.setContentsMargins(20, -1, -1, -1)

        self.verticalLayout.addLayout(self.grid_layout)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Script name", None))
    # retranslateUi

