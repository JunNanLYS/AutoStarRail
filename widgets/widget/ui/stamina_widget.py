# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'stamina_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, QRect,
                            QSize, Qt)
from PySide6.QtGui import (QPixmap)
from PySide6.QtWidgets import (QHBoxLayout, QSizePolicy, QSpacerItem,
                               QVBoxLayout, QWidget)
from qfluentwidgets import (BodyLabel, PixmapLabel, PushButton, SmoothScrollArea,
                            SpinBox, SubtitleLabel)

from ..card import StaminaCard
from .resource import resource


class StaminaWidgetUi(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(600, 3500)
        self.verticalLayout_4 = QVBoxLayout(Form)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = SmoothScrollArea(Form)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidget = QWidget()
        self.scrollAreaWidget.setObjectName(u"scrollAreaWidget")
        self.scrollAreaWidget.setGeometry(QRect(0, 0, 598, 3498))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidget)
        self.verticalLayout_3.setSpacing(10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.calyxGoldCard = StaminaCard(self.scrollAreaWidget)
        self.calyxGoldCard.setObjectName(u"calyxGoldCard")
        self.verticalLayout = QVBoxLayout(self.calyxGoldCard)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.calyxGoldLabel = SubtitleLabel(self.calyxGoldCard)
        self.calyxGoldLabel.setObjectName(u"calyxGoldLabel")

        self.verticalLayout.addWidget(self.calyxGoldLabel)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, -1, 0, -1)
        self.characterEXPLabel = BodyLabel(self.calyxGoldCard)
        self.characterEXPLabel.setObjectName(u"characterEXPLabel")

        self.horizontalLayout.addWidget(self.characterEXPLabel)

        self.calyxSpinBox_1 = SpinBox(self.calyxGoldCard)
        self.calyxSpinBox_1.setObjectName(u"calyxSpinBox_1")

        self.horizontalLayout.addWidget(self.calyxSpinBox_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.coneEXPLabel = BodyLabel(self.calyxGoldCard)
        self.coneEXPLabel.setObjectName(u"coneEXPLabel")

        self.horizontalLayout_2.addWidget(self.coneEXPLabel)

        self.calyxSpinBox_2 = SpinBox(self.calyxGoldCard)
        self.calyxSpinBox_2.setObjectName(u"calyxSpinBox_2")

        self.horizontalLayout_2.addWidget(self.calyxSpinBox_2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, -1, 0, -1)
        self.creditLabel = BodyLabel(self.calyxGoldCard)
        self.creditLabel.setObjectName(u"creditLabel")

        self.horizontalLayout_3.addWidget(self.creditLabel)

        self.calyxSpinBox_3 = SpinBox(self.calyxGoldCard)
        self.calyxSpinBox_3.setObjectName(u"calyxSpinBox_3")

        self.horizontalLayout_3.addWidget(self.calyxSpinBox_3)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout.setStretch(3, 1)

        self.verticalLayout_3.addWidget(self.calyxGoldCard)

        self.calyxRedCard = StaminaCard(self.scrollAreaWidget)
        self.calyxRedCard.setObjectName(u"calyxRedCard")
        self.verticalLayout_2 = QVBoxLayout(self.calyxRedCard)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.calyxRedLabel = SubtitleLabel(self.calyxRedCard)
        self.calyxRedLabel.setObjectName(u"calyxRedLabel")

        self.verticalLayout_2.addWidget(self.calyxRedLabel)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.desrructionLabel = BodyLabel(self.calyxRedCard)
        self.desrructionLabel.setObjectName(u"desrructionLabel")

        self.horizontalLayout_4.addWidget(self.desrructionLabel)

        self.calyxSpinBox_4 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_4.setObjectName(u"calyxSpinBox_4")

        self.horizontalLayout_4.addWidget(self.calyxSpinBox_4)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.BodyLabel_5 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_5.setObjectName(u"BodyLabel_5")

        self.horizontalLayout_5.addWidget(self.BodyLabel_5)

        self.calyxSpinBox_5 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_5.setObjectName(u"calyxSpinBox_5")

        self.horizontalLayout_5.addWidget(self.calyxSpinBox_5)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.BodyLabel_6 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_6.setObjectName(u"BodyLabel_6")

        self.horizontalLayout_6.addWidget(self.BodyLabel_6)

        self.calyxSpinBox_6 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_6.setObjectName(u"calyxSpinBox_6")

        self.horizontalLayout_6.addWidget(self.calyxSpinBox_6)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.BodyLabel_7 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_7.setObjectName(u"BodyLabel_7")

        self.horizontalLayout_7.addWidget(self.BodyLabel_7)

        self.calyxSpinBox_7 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_7.setObjectName(u"calyxSpinBox_7")

        self.horizontalLayout_7.addWidget(self.calyxSpinBox_7)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.BodyLabel_8 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_8.setObjectName(u"BodyLabel_8")

        self.horizontalLayout_8.addWidget(self.BodyLabel_8)

        self.calyxSpinBox_8 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_8.setObjectName(u"calyxSpinBox_8")

        self.horizontalLayout_8.addWidget(self.calyxSpinBox_8)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)


        self.verticalLayout_2.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.BodyLabel_9 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_9.setObjectName(u"BodyLabel_9")

        self.horizontalLayout_9.addWidget(self.BodyLabel_9)

        self.calyxSpinBox_9 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_9.setObjectName(u"calyxSpinBox_9")

        self.horizontalLayout_9.addWidget(self.calyxSpinBox_9)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.BodyLabel_10 = BodyLabel(self.calyxRedCard)
        self.BodyLabel_10.setObjectName(u"BodyLabel_10")

        self.horizontalLayout_10.addWidget(self.BodyLabel_10)

        self.calyxSpinBox_10 = SpinBox(self.calyxRedCard)
        self.calyxSpinBox_10.setObjectName(u"calyxSpinBox_10")

        self.horizontalLayout_10.addWidget(self.calyxSpinBox_10)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addLayout(self.horizontalLayout_10)

        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 1)
        self.verticalLayout_2.setStretch(4, 1)
        self.verticalLayout_2.setStretch(5, 1)
        self.verticalLayout_2.setStretch(6, 1)
        self.verticalLayout_2.setStretch(7, 1)

        self.verticalLayout_3.addWidget(self.calyxRedCard)

        self.shadowCard = StaminaCard(self.scrollAreaWidget)
        self.shadowCard.setObjectName(u"shadowCard")
        self.verticalLayout_5 = QVBoxLayout(self.shadowCard)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.stagnantShadowLabel = SubtitleLabel(self.shadowCard)
        self.stagnantShadowLabel.setObjectName(u"stagnantShadowLabel")

        self.verticalLayout_5.addWidget(self.stagnantShadowLabel)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.PixmapLabel = PixmapLabel(self.shadowCard)
        self.PixmapLabel.setObjectName(u"PixmapLabel")
        self.PixmapLabel.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u7a7a\u6d77\u4e4b\u5f62.png"))

        self.horizontalLayout_11.addWidget(self.PixmapLabel)

        self.shadowSpinBox_1 = SpinBox(self.shadowCard)
        self.shadowSpinBox_1.setObjectName(u"shadowSpinBox_1")

        self.horizontalLayout_11.addWidget(self.shadowSpinBox_1)

        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_2 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_2.setObjectName(u"PixmapLabel_2")
        self.PixmapLabel_2.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u5dfd\u98ce\u4e4b\u5f62.png"))

        self.horizontalLayout_12.addWidget(self.PixmapLabel_2)

        self.shadowSpinBox_2 = SpinBox(self.shadowCard)
        self.shadowSpinBox_2.setObjectName(u"shadowSpinBox_2")

        self.horizontalLayout_12.addWidget(self.shadowSpinBox_2)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_12)


        self.verticalLayout_5.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_3 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_3.setObjectName(u"PixmapLabel_3")
        self.PixmapLabel_3.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u9e23\u96f7\u4e4b\u5f62.png"))

        self.horizontalLayout_13.addWidget(self.PixmapLabel_3)

        self.shadowSpinBox_3 = SpinBox(self.shadowCard)
        self.shadowSpinBox_3.setObjectName(u"shadowSpinBox_3")

        self.horizontalLayout_13.addWidget(self.shadowSpinBox_3)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_14)


        self.verticalLayout_5.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setSpacing(5)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_4 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_4.setObjectName(u"PixmapLabel_4")
        self.PixmapLabel_4.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u708e\u534e\u4e4b\u5f62.png"))

        self.horizontalLayout_14.addWidget(self.PixmapLabel_4)

        self.shadowSpinBox_4 = SpinBox(self.shadowCard)
        self.shadowSpinBox_4.setObjectName(u"shadowSpinBox_4")

        self.horizontalLayout_14.addWidget(self.shadowSpinBox_4)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_13)


        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setSpacing(5)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_5 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_5.setObjectName(u"PixmapLabel_5")
        self.PixmapLabel_5.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u950b\u8292\u4e4b\u5f62.png"))

        self.horizontalLayout_15.addWidget(self.PixmapLabel_5)

        self.shadowSpinBox_5 = SpinBox(self.shadowCard)
        self.shadowSpinBox_5.setObjectName(u"shadowSpinBox_5")

        self.horizontalLayout_15.addWidget(self.shadowSpinBox_5)

        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_15)


        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setSpacing(5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_6 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_6.setObjectName(u"PixmapLabel_6")
        self.PixmapLabel_6.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u971c\u6676\u4e4b\u5f62.png"))

        self.horizontalLayout_16.addWidget(self.PixmapLabel_6)

        self.shadowSpinBox_6 = SpinBox(self.shadowCard)
        self.shadowSpinBox_6.setObjectName(u"shadowSpinBox_6")

        self.horizontalLayout_16.addWidget(self.shadowSpinBox_6)

        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_16)


        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setSpacing(5)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_7 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_7.setObjectName(u"PixmapLabel_7")
        self.PixmapLabel_7.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u5e7b\u5149\u4e4b\u5f62.png"))

        self.horizontalLayout_17.addWidget(self.PixmapLabel_7)

        self.shadowSpinBox_7 = SpinBox(self.shadowCard)
        self.shadowSpinBox_7.setObjectName(u"shadowSpinBox_7")

        self.horizontalLayout_17.addWidget(self.shadowSpinBox_7)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_17)


        self.verticalLayout_5.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(5)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_8 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_8.setObjectName(u"PixmapLabel_8")
        self.PixmapLabel_8.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u51b0\u51cc\u4e4b\u5f62.png"))

        self.horizontalLayout_18.addWidget(self.PixmapLabel_8)

        self.shadowSpinBox_8 = SpinBox(self.shadowCard)
        self.shadowSpinBox_8.setObjectName(u"shadowSpinBox_8")

        self.horizontalLayout_18.addWidget(self.shadowSpinBox_8)

        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_18)


        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(5)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_9 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_9.setObjectName(u"PixmapLabel_9")
        self.PixmapLabel_9.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u9707\u5384\u4e4b\u5f62.png"))

        self.horizontalLayout_19.addWidget(self.PixmapLabel_9)

        self.shadowSpinBox_9 = SpinBox(self.shadowCard)
        self.shadowSpinBox_9.setObjectName(u"shadowSpinBox_9")

        self.horizontalLayout_19.addWidget(self.shadowSpinBox_9)

        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_19.addItem(self.horizontalSpacer_19)


        self.verticalLayout_5.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setSpacing(5)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, 0, -1, -1)
        self.PixmapLabel_10 = PixmapLabel(self.shadowCard)
        self.PixmapLabel_10.setObjectName(u"PixmapLabel_10")
        self.PixmapLabel_10.setPixmap(QPixmap(u":/shadow/stargnantShadow/\u5929\u4eba\u4e4b\u5f62.png"))

        self.horizontalLayout_20.addWidget(self.PixmapLabel_10)

        self.shadowSpinBox_10 = SpinBox(self.shadowCard)
        self.shadowSpinBox_10.setObjectName(u"shadowSpinBox_10")

        self.horizontalLayout_20.addWidget(self.shadowSpinBox_10)

        self.horizontalSpacer_20 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_20)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.verticalLayout_5.setStretch(1, 1)
        self.verticalLayout_5.setStretch(2, 1)
        self.verticalLayout_5.setStretch(3, 1)
        self.verticalLayout_5.setStretch(4, 1)
        self.verticalLayout_5.setStretch(5, 1)
        self.verticalLayout_5.setStretch(6, 1)
        self.verticalLayout_5.setStretch(7, 1)
        self.verticalLayout_5.setStretch(8, 1)
        self.verticalLayout_5.setStretch(9, 1)
        self.verticalLayout_5.setStretch(10, 1)

        self.verticalLayout_3.addWidget(self.shadowCard)

        self.cavernCard = StaminaCard(self.scrollAreaWidget)
        self.cavernCard.setObjectName(u"cavernCard")
        self.verticalLayout_6 = QVBoxLayout(self.cavernCard)
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.cavernLabel = SubtitleLabel(self.cavernCard)
        self.cavernLabel.setObjectName(u"cavernLabel")

        self.verticalLayout_6.addWidget(self.cavernLabel)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_14 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_14.setObjectName(u"PixmapLabel_14")
        self.PixmapLabel_14.setPixmap(QPixmap(u":/cavern/cavern/1.png"))

        self.horizontalLayout_28.addWidget(self.PixmapLabel_14)

        self.cavernSpinBox1 = SpinBox(self.cavernCard)
        self.cavernSpinBox1.setObjectName(u"cavernSpinBox1")

        self.horizontalLayout_28.addWidget(self.cavernSpinBox1)

        self.horizontalSpacer_24 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_24)


        self.verticalLayout_6.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_15 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_15.setObjectName(u"PixmapLabel_15")
        self.PixmapLabel_15.setPixmap(QPixmap(u":/cavern/cavern/2.png"))

        self.horizontalLayout_29.addWidget(self.PixmapLabel_15)

        self.cavernSpinBox2 = SpinBox(self.cavernCard)
        self.cavernSpinBox2.setObjectName(u"cavernSpinBox2")

        self.horizontalLayout_29.addWidget(self.cavernSpinBox2)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_26)


        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_16 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_16.setObjectName(u"PixmapLabel_16")
        self.PixmapLabel_16.setPixmap(QPixmap(u":/cavern/cavern/3.png"))

        self.horizontalLayout_27.addWidget(self.PixmapLabel_16)

        self.cavernSpinBox3 = SpinBox(self.cavernCard)
        self.cavernSpinBox3.setObjectName(u"cavernSpinBox3")

        self.horizontalLayout_27.addWidget(self.cavernSpinBox3)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_27)


        self.verticalLayout_6.addLayout(self.horizontalLayout_27)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_17 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_17.setObjectName(u"PixmapLabel_17")
        self.PixmapLabel_17.setPixmap(QPixmap(u":/cavern/cavern/4.png"))

        self.horizontalLayout_30.addWidget(self.PixmapLabel_17)

        self.cavernSpinBox4 = SpinBox(self.cavernCard)
        self.cavernSpinBox4.setObjectName(u"cavernSpinBox4")

        self.horizontalLayout_30.addWidget(self.cavernSpinBox4)

        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_25)


        self.verticalLayout_6.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_18 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_18.setObjectName(u"PixmapLabel_18")
        self.PixmapLabel_18.setPixmap(QPixmap(u":/cavern/cavern/5.png"))

        self.horizontalLayout_26.addWidget(self.PixmapLabel_18)

        self.cavernSpinBox5 = SpinBox(self.cavernCard)
        self.cavernSpinBox5.setObjectName(u"cavernSpinBox5")

        self.horizontalLayout_26.addWidget(self.cavernSpinBox5)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_28)


        self.verticalLayout_6.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(-1, 6, -1, -1)
        self.PixmapLabel_19 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_19.setObjectName(u"PixmapLabel_19")
        self.PixmapLabel_19.setPixmap(QPixmap(u":/cavern/cavern/6.png"))

        self.horizontalLayout_25.addWidget(self.PixmapLabel_19)

        self.cavernSpinBox6 = SpinBox(self.cavernCard)
        self.cavernSpinBox6.setObjectName(u"cavernSpinBox6")

        self.horizontalLayout_25.addWidget(self.cavernSpinBox6)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_29)


        self.verticalLayout_6.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_20 = PixmapLabel(self.cavernCard)
        self.PixmapLabel_20.setObjectName(u"PixmapLabel_20")
        self.PixmapLabel_20.setPixmap(QPixmap(u":/cavern/cavern/7.png"))

        self.horizontalLayout_24.addWidget(self.PixmapLabel_20)

        self.cavernSpinBox7 = SpinBox(self.cavernCard)
        self.cavernSpinBox7.setObjectName(u"cavernSpinBox7")

        self.horizontalLayout_24.addWidget(self.cavernSpinBox7)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)


        self.verticalLayout_6.addLayout(self.horizontalLayout_24)

        self.verticalLayout_6.setStretch(1, 1)
        self.verticalLayout_6.setStretch(2, 1)
        self.verticalLayout_6.setStretch(3, 1)
        self.verticalLayout_6.setStretch(4, 1)
        self.verticalLayout_6.setStretch(5, 1)
        self.verticalLayout_6.setStretch(6, 1)
        self.verticalLayout_6.setStretch(7, 1)

        self.verticalLayout_3.addWidget(self.cavernCard)

        self.warCard = StaminaCard(self.scrollAreaWidget)
        self.warCard.setObjectName(u"warCard")
        self.verticalLayout_7 = QVBoxLayout(self.warCard)
        self.verticalLayout_7.setSpacing(5)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.warLabel = SubtitleLabel(self.warCard)
        self.warLabel.setObjectName(u"warLabel")

        self.verticalLayout_7.addWidget(self.warLabel)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_11 = PixmapLabel(self.warCard)
        self.PixmapLabel_11.setObjectName(u"PixmapLabel_11")
        self.PixmapLabel_11.setPixmap(QPixmap(u":/war/echoOfWar/\u6bc1\u706d.png"))

        self.horizontalLayout_21.addWidget(self.PixmapLabel_11)

        self.echoSpinBox1 = SpinBox(self.warCard)
        self.echoSpinBox1.setObjectName(u"echoSpinBox1")
        self.echoSpinBox1.setMaximum(3)

        self.horizontalLayout_21.addWidget(self.echoSpinBox1)

        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_23)


        self.verticalLayout_7.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_12 = PixmapLabel(self.warCard)
        self.PixmapLabel_12.setObjectName(u"PixmapLabel_12")
        self.PixmapLabel_12.setPixmap(QPixmap(u":/war/echoOfWar/\u53ef\u53ef\u5229\u4e9a.png"))
        self.PixmapLabel_12.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_23.addWidget(self.PixmapLabel_12)

        self.echoSpinBox2 = SpinBox(self.warCard)
        self.echoSpinBox2.setObjectName(u"echoSpinBox2")
        self.echoSpinBox2.setMinimumSize(QSize(0, 33))
        self.echoSpinBox2.setMaximum(3)

        self.horizontalLayout_23.addWidget(self.echoSpinBox2)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_22)


        self.verticalLayout_7.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, 5, -1, -1)
        self.PixmapLabel_13 = PixmapLabel(self.warCard)
        self.PixmapLabel_13.setObjectName(u"PixmapLabel_13")
        self.PixmapLabel_13.setPixmap(QPixmap(u":/war/echoOfWar/\u4e30\u9976.png"))

        self.horizontalLayout_22.addWidget(self.PixmapLabel_13)

        self.echoSpinBox3 = SpinBox(self.warCard)
        self.echoSpinBox3.setObjectName(u"echoSpinBox3")
        self.echoSpinBox3.setMaximum(3)

        self.horizontalLayout_22.addWidget(self.echoSpinBox3)

        self.horizontalSpacer_21 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_21)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.verticalLayout_7.setStretch(1, 1)
        self.verticalLayout_7.setStretch(2, 1)
        self.verticalLayout_7.setStretch(3, 1)

        self.verticalLayout_3.addWidget(self.warCard)

        self.staminaButton = PushButton(self.scrollAreaWidget)
        self.staminaButton.setObjectName(u"staminaButton")

        self.verticalLayout_3.addWidget(self.staminaButton)

        self.vSpacer = QSpacerItem(0, 1000, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.vSpacer)

        self.scrollArea.setWidget(self.scrollAreaWidget)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.calyxGoldLabel.setText(QCoreApplication.translate("Form", u"\u62df\u9020\u82b1\u843c(\u91d1)", None))
        self.characterEXPLabel.setText(QCoreApplication.translate("Form", u"\u89d2\u8272\u7ecf\u9a8c", None))
        self.coneEXPLabel.setText(QCoreApplication.translate("Form", u"\u5149\u9525\u7ecf\u9a8c", None))
        self.creditLabel.setText(QCoreApplication.translate("Form", u"\u4fe1\u7528\u70b9", None))
        self.calyxRedLabel.setText(QCoreApplication.translate("Form", u"\u62df\u9020\u82b1\u843c(\u8d64)", None))
        self.desrructionLabel.setText(QCoreApplication.translate("Form", u"\u6bc1\u706d", None))
        self.BodyLabel_5.setText(QCoreApplication.translate("Form", u"\u5b58\u62a4", None))
        self.BodyLabel_6.setText(QCoreApplication.translate("Form", u"\u5de1\u730e", None))
        self.BodyLabel_7.setText(QCoreApplication.translate("Form", u"\u4e30\u9976", None))
        self.BodyLabel_8.setText(QCoreApplication.translate("Form", u"\u667a\u8bc6", None))
        self.BodyLabel_9.setText(QCoreApplication.translate("Form", u"\u540c\u8c10", None))
        self.BodyLabel_10.setText(QCoreApplication.translate("Form", u"\u865a\u65e0", None))
        self.stagnantShadowLabel.setText(QCoreApplication.translate("Form", u"\u51dd\u6ede\u865a\u5f71", None))
        self.cavernLabel.setText(QCoreApplication.translate("Form", u"\u4fb5\u8680\u96a7\u6d1e", None))
        self.warLabel.setText(QCoreApplication.translate("Form", u"\u5386\u6218\u56de\u54cd", None))
        self.staminaButton.setText(QCoreApplication.translate("Form", u"\u6e05\u7406\u5f00\u62d3\u529b", None))
    # retranslateUi

