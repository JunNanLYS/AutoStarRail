# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'one_avatar.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QSize, Qt)
from PySide6.QtWidgets import (QVBoxLayout)

from qfluentwidgets import (AvatarWidget, StrongBodyLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(106, 125)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.avatar = AvatarWidget(Frame)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setMinimumSize(QSize(96, 96))
        self.avatar.setMaximumSize(QSize(96, 96))

        self.verticalLayout.addWidget(self.avatar)

        self.name = StrongBodyLabel(Frame)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(96, 19))
        self.name.setMaximumSize(QSize(96, 19))
        self.name.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.name)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.name.setText(QCoreApplication.translate("Frame", u"name", None))
    # retranslateUi

