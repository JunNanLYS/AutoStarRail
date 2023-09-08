# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'universe.ui'
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
    QVBoxLayout, QWidget)

from qfluentwidgets import (CheckBox, ComboBox, PushButton, StrongBodyLabel)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(400, 181)
        Frame.setMinimumSize(QSize(400, 0))
        self.verticalLayout_3 = QVBoxLayout(Frame)
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 32, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkbox_show_map = CheckBox(Frame)
        self.checkbox_show_map.setObjectName(u"checkbox_show_map")
        self.checkbox_show_map.setTristate(False)

        self.horizontalLayout.addWidget(self.checkbox_show_map)

        self.checkbox_debug = CheckBox(Frame)
        self.checkbox_debug.setObjectName(u"checkbox_debug")
        self.checkbox_debug.setTristate(False)

        self.horizontalLayout.addWidget(self.checkbox_debug)

        self.checkbox_speed = CheckBox(Frame)
        self.checkbox_speed.setObjectName(u"checkbox_speed")
        self.checkbox_speed.setTristate(False)

        self.horizontalLayout.addWidget(self.checkbox_speed)

        self.checkbox_update = CheckBox(Frame)
        self.checkbox_update.setObjectName(u"checkbox_update")
        self.checkbox_update.setTristate(False)

        self.horizontalLayout.addWidget(self.checkbox_update)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_difficulty = StrongBodyLabel(Frame)
        self.label_difficulty.setObjectName(u"label_difficulty")
        self.label_difficulty.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_2.addWidget(self.label_difficulty)

        self.combobox_difficulty = ComboBox(Frame)
        self.combobox_difficulty.setObjectName(u"combobox_difficulty")

        self.verticalLayout_2.addWidget(self.combobox_difficulty)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_fate = StrongBodyLabel(Frame)
        self.label_fate.setObjectName(u"label_fate")
        self.label_fate.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout.addWidget(self.label_fate)

        self.combobox_fate = ComboBox(Frame)
        self.combobox_fate.setObjectName(u"combobox_fate")

        self.verticalLayout.addWidget(self.combobox_fate)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(10)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_number = StrongBodyLabel(Frame)
        self.label_number.setObjectName(u"label_number")
        self.label_number.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.verticalLayout_4.addWidget(self.label_number)

        self.combobox_number = ComboBox(Frame)
        self.combobox_number.setObjectName(u"combobox_number")

        self.verticalLayout_4.addWidget(self.combobox_number)


        self.horizontalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 5)
        self.button_no = PushButton(Frame)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout_3.addWidget(self.button_no)

        self.button_yes = PushButton(Frame)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout_3.addWidget(self.button_yes)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.checkbox_show_map.setText(QCoreApplication.translate("Frame", u"\u663e\u793a\u5730\u56fe", None))
        self.checkbox_debug.setText(QCoreApplication.translate("Frame", u"\u8c03\u8bd5\u6a21\u5f0f", None))
        self.checkbox_speed.setText(QCoreApplication.translate("Frame", u"\u901f\u901a\u6a21\u5f0f", None))
        self.checkbox_update.setText(QCoreApplication.translate("Frame", u"\u5f3a\u5236\u66f4\u65b0", None))
        self.label_difficulty.setText(QCoreApplication.translate("Frame", u"\u96be\u5ea6", None))
        self.label_fate.setText(QCoreApplication.translate("Frame", u"\u547d\u9014", None))
        self.label_number.setText(QCoreApplication.translate("Frame", u"\u6a21\u62df\u5b87\u5b99\u7f16\u53f7", None))
        self.button_no.setText(QCoreApplication.translate("Frame", u"\u53d6\u6d88", None))
        self.button_yes.setText(QCoreApplication.translate("Frame", u"\u4fdd\u5b58", None))
    # retranslateUi

