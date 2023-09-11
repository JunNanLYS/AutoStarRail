# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stamina.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

from qfluentwidgets import (CardWidget, HeaderCardWidget, PushButton, SimpleCardWidget,
    SmoothScrollArea)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(639, 517)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.SmoothScrollArea = SmoothScrollArea(Frame)
        self.SmoothScrollArea.setObjectName(u"SmoothScrollArea")
        self.SmoothScrollArea.setWidgetResizable(True)
        self.scroll_widget = QWidget()
        self.scroll_widget.setObjectName(u"scroll_widget")
        self.scroll_widget.setGeometry(QRect(0, 0, 637, 565))
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setSpacing(10)
        self.scroll_layout.setObjectName(u"scroll_layout")
        self.scroll_layout.setContentsMargins(10, 10, 10, 10)
        self.calyx_gold_card = HeaderCardWidget(self.scroll_widget)
        self.calyx_gold_card.setObjectName(u"calyx_gold_card")
        self.calyx_gold_card.setBorderRadius(5)

        self.scroll_layout.addWidget(self.calyx_gold_card)

        self.calyx_red_card = HeaderCardWidget(self.scroll_widget)
        self.calyx_red_card.setObjectName(u"calyx_red_card")

        self.scroll_layout.addWidget(self.calyx_red_card)

        self.shadow_card = HeaderCardWidget(self.scroll_widget)
        self.shadow_card.setObjectName(u"shadow_card")

        self.scroll_layout.addWidget(self.shadow_card)

        self.cavern_card = HeaderCardWidget(self.scroll_widget)
        self.cavern_card.setObjectName(u"cavern_card")

        self.scroll_layout.addWidget(self.cavern_card)

        self.echo_card = HeaderCardWidget(self.scroll_widget)
        self.echo_card.setObjectName(u"echo_card")

        self.scroll_layout.addWidget(self.echo_card)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.scroll_layout.addItem(self.verticalSpacer)

        self.scroll_layout.setStretch(0, 1)
        self.scroll_layout.setStretch(1, 1)
        self.scroll_layout.setStretch(2, 1)
        self.scroll_layout.setStretch(4, 1)
        self.scroll_layout.setStretch(5, 1)
        self.SmoothScrollArea.setWidget(self.scroll_widget)

        self.verticalLayout.addWidget(self.SmoothScrollArea)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.button_no = PushButton(Frame)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout.addWidget(self.button_no)

        self.button_yes = PushButton(Frame)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout.addWidget(self.button_yes)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.calyx_gold_card.setTitle("")
        self.button_no.setText(QCoreApplication.translate("Frame", u"\u53d6\u6d88", None))
        self.button_yes.setText(QCoreApplication.translate("Frame", u"\u786e\u5b9a", None))
    # retranslateUi

