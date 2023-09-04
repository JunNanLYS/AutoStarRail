from PySide6.QtWidgets import QFrame
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

        self.__init_widget()

    def get_script_name(self):
        """get script name"""
        return self.combobox.currentText()

    def __init_combobox(self):
        items = ["体力", "模拟宇宙", "委托", "每日任务", "世界", "运行所有"]
        self.combobox.addItems(items)
        self.combobox.setCurrentIndex(0)

    def __init_widget(self):
        self.__init_combobox()
        self.PlainTextEdit.setReadOnly(True)

