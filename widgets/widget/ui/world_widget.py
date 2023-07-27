# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'world_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

from ..card import Card
from qfluentwidgets import (ComboBox, PushButton, SmoothScrollArea, SplitPushButton,
    SubtitleLabel)

class WorldWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(618, 566)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SmoothScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 616, 564))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.mapCard = Card(self.scrollAreaWidget)
        self.mapCard.setObjectName(u"mapCard")
        self.mapCardLayout = QVBoxLayout(self.mapCard)
        self.mapCardLayout.setSpacing(10)
        self.mapCardLayout.setObjectName(u"mapCardLayout")
        self.mapCardLayout.setContentsMargins(20, 20, 20, 20)
        self.mapLabel = SubtitleLabel(self.mapCard)
        self.mapLabel.setObjectName(u"mapLabel")
        self.mapLabel.setMinimumSize(QSize(0, 30))
        self.mapLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.mapCardLayout.addWidget(self.mapLabel)

        self.mapComboBox = ComboBox(self.mapCard)
        self.mapComboBox.setObjectName(u"mapComboBox")
        self.mapComboBox.setMinimumSize(QSize(0, 32))

        self.mapCardLayout.addWidget(self.mapComboBox)

        self.startButton = PushButton(self.mapCard)
        self.startButton.setObjectName(u"startButton")

        self.mapCardLayout.addWidget(self.startButton)


        self.verticalLayout_4.addWidget(self.mapCard)

        self.updateCard = Card(self.scrollAreaWidget)
        self.updateCard.setObjectName(u"updateCard")
        self.updateCardLayout = QVBoxLayout(self.updateCard)
        self.updateCardLayout.setSpacing(10)
        self.updateCardLayout.setObjectName(u"updateCardLayout")
        self.updateCardLayout.setContentsMargins(20, 20, 20, 20)
        self.scripLabel = SubtitleLabel(self.updateCard)
        self.scripLabel.setObjectName(u"scripLabel")
        self.scripLabel.setMinimumSize(QSize(0, 30))
        self.scripLabel.setMaximumSize(QSize(16777215, 16777215))
        self.scripLabel.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.updateCardLayout.addWidget(self.scripLabel)

        self.updateButton = SplitPushButton(self.updateCard)
        self.updateButton.setObjectName(u"updateButton")

        self.updateCardLayout.addWidget(self.updateButton)


        self.verticalLayout_4.addWidget(self.updateCard)

        self.verticalSpacer = QSpacerItem(20, 307, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.mapLabel.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u8d77\u59cb\u5730\u56fe", None))
        self.startButton.setText(QCoreApplication.translate("Form", u"\u9504\u5927\u5730", None))
        self.scripLabel.setText(QCoreApplication.translate("Form", u"\u66f4\u65b0\u811a\u672c", None))
        self.updateButton.setProperty("text_", QCoreApplication.translate("Form", u"Split push button", None))
    # retranslateUi

