# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'run_widget.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QSizePolicy, QVBoxLayout,
    QWidget)

from qfluentwidgets import (ComboBox, PlainTextEdit, PushButton)

class Ui_Frame(object):
    def setupUi(self, Frame):
        if not Frame.objectName():
            Frame.setObjectName(u"Frame")
        Frame.resize(581, 398)
        self.verticalLayout = QVBoxLayout(Frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.PlainTextEdit = PlainTextEdit(Frame)
        self.PlainTextEdit.setObjectName(u"PlainTextEdit")

        self.verticalLayout.addWidget(self.PlainTextEdit)

        self.combobox = ComboBox(Frame)
        self.combobox.setObjectName(u"combobox")

        self.verticalLayout.addWidget(self.combobox)

        self.button_run = PushButton(Frame)
        self.button_run.setObjectName(u"button_run")

        self.verticalLayout.addWidget(self.button_run)


        self.retranslateUi(Frame)

        QMetaObject.connectSlotsByName(Frame)
    # setupUi

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(QCoreApplication.translate("Frame", u"Frame", None))
        self.PlainTextEdit.setPlainText(QCoreApplication.translate("Frame", u"\u5012\u5356\u53ef\u803b\uff01\u5012\u5356\u53ef\u803b\uff01\u5012\u5356\u53ef\u803b\uff01\n"
"\u672c\u9879\u76eeAutoStarRail\u4e3a\u5f00\u6e90\u514d\u8d39\u516c\u76ca\u9879\u76ee\n"
"\u5982\u679c\u4f60\u4eceGithub\u4e4b\u5916\u6e20\u9053\u4ed8\u8d39\u5f97\u5230\u8be5\u9879\u76ee\u8bf7\u7acb\u5373\u5dee\u8bc4\u5e76\u4e3e\u62a5\u5546\u5bb6\uff01\n"
"\u9879\u76ee\u7528\u4e8e\u5b66\u4e60\u4ea4\u6d41\n"
"", None))
        self.button_run.setText(QCoreApplication.translate("Frame", u"\u8fd0\u884c\u811a\u672c", None))
    # retranslateUi

