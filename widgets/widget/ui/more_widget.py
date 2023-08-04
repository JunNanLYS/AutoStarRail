# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'more_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from ..card import Card
from qfluentwidgets import (PushButton, SmoothScrollArea)

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
    # retranslateUi

