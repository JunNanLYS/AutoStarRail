# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'avatar_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect)
from PySide6.QtWidgets import (QVBoxLayout,
                               QWidget)

from qfluentwidgets import (SmoothScrollArea, SubtitleLabel)


class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(605, 481)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SmoothScrollArea = SmoothScrollArea(Frame)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 603, 479))
        self.verticalLayout_2 = QVBoxLayout(self.scroll_widget)
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.dev_members_layout = QVBoxLayout()
        self.dev_members_layout.setSpacing(10)
        self.dev_members_layout.setObjectName(u"dev_members_layout")
        self.dev_members_layout.setContentsMargins(10, -1, 10, -1)
        self.dev_members_label = SubtitleLabel(self.scroll_widget)
        self.dev_members_label.setObjectName(u"dev_members_label")

        self.dev_members_layout.addWidget(self.dev_members_label)

        self.verticalLayout_2.addLayout(self.dev_members_layout)

        self.acknowledgements_layout = QVBoxLayout()
        self.acknowledgements_layout.setSpacing(10)
        self.acknowledgements_layout.setObjectName(u"acknowledgements_layout")
        self.acknowledgements_layout.setContentsMargins(10, -1, 10, -1)
        self.acknowledgements_label = SubtitleLabel(self.scroll_widget)
        self.acknowledgements_label.setObjectName(u"acknowledgements_label")

        self.acknowledgements_layout.addWidget(self.acknowledgements_label)

        self.verticalLayout_2.addLayout(self.acknowledgements_layout)

        self.SmoothScrollArea.setWidget(self.scroll_widget)

        self.verticalLayout.addWidget(self.SmoothScrollArea)

        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)

    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.dev_members_label.setText(QCoreApplication.translate("Frame", u"\u5f00\u53d1\u6210\u5458", None))
        self.acknowledgements_label.setText(QCoreApplication.translate("Frame", u"\u81f4\u8c22", None))
    # retranslateUi
