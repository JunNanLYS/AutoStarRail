from PySide6.QtWidgets import QFrame, QPushButton
from qfluentwidgets import PushButton

from .ui.run_widget import Ui_Frame


class RunInterface(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("运行")
        self.setStyleSheet(
            """
            background: rgb(250, 250, 250);
            border: none;
            border-radius:10px;
            """
        )
        self.setupUi(self)
        self.button_angle = PushButton("校准角度", self)

        self.__init_widget()

    def get_script_name(self):
        """get script name"""
        return self.combobox.currentText()

    def __connect_signal_to_slot(self):
        self.combobox.currentTextChanged.connect(self.__on_combobox_text_changed)

    def __on_combobox_text_changed(self, text):
        texts = ["模拟宇宙", "世界", "深渊"]
        if text in texts:
            self.button_angle.show()
        else:
            self.button_angle.hide()

    def __init_combobox(self):
        items = ["体力", "模拟宇宙", "深渊", "委托", "每日任务", "世界", "运行所有"]
        self.combobox.addItems(items)
        self.combobox.setCurrentIndex(0)

    def __init_layout(self):
        self.button_layout.addWidget(self.button_angle)

    def __init_widget(self):
        self.PlainTextEdit.setReadOnly(True)
        self.button_angle.hide()

        self.__init_combobox()
        self.__init_layout()
        self.__connect_signal_to_slot()

