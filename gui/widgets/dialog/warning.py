from PySide6.QtCore import Qt, QTimer, QEventLoop
from PySide6.QtWidgets import QVBoxLayout, QSpacerItem, QSizePolicy
from qfluentwidgets import SimpleCardWidget, TitleLabel, StrongBodyLabel


class WarningDialog(SimpleCardWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.v_layout = QVBoxLayout(self)
        self.v_layout.setContentsMargins(20, 20, 20, 20)
        self.v_layout.setSpacing(20)
        self.spacer = QSpacerItem(0, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.__init_widget()
        self.show()
        loop = QEventLoop()
        QTimer.singleShot(10000, loop.quit)
        loop.exec()
        self.close()

    def __init_label(self):
        self.title = TitleLabel(self)
        self.title.setText("此软件为免费开源项目，如果你付了钱请立即退款并举报！")
        self.title.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.sub_label = StrongBodyLabel(self)
        self.sub_label.setText("咸鱼倒狗4000+！你付给倒狗的每一分钱都会让开源自动化更加困难，请退款并举报商家！\n"
                               "本项目已经因为倒卖行为受到严重威胁，请帮助我们！\n"
                               "整合包链接：https://github.com/JunNanLYS/AutoStarRail\n"
                               "模拟宇宙作者链接：https://github.com/CHNZYX/Auto_Simulated_Universe\n"
                               "如果喜欢该项目可以请喝杯奶茶捏\n"
                               "10s后关闭")
        self.sub_label.setAlignment(Qt.AlignmentFlag.AlignTop)

    def __init_layout(self):
        self.v_layout.addWidget(self.title)
        self.v_layout.addWidget(self.sub_label)

        self.v_layout.addItem(self.spacer)

    def __init_widget(self):
        self.__init_label()
        self.__init_layout()
        self.setFixedSize(770, 240)
        self.setBorderRadius(10)
        if self.parent():
            self.move((self.parent().width() // 2) - (self.width() // 2),
                      (self.parent().height() // 2) - (self.height() // 2))


if __name__ == "__main__":
    from PySide6.QtWidgets import QApplication

    app = QApplication([])
    warning_dialog = WarningDialog()
    print(warning_dialog.size())
    app.exec()
