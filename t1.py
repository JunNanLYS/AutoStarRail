from PySide6.QtWidgets import QApplication, QPlainTextEdit
from qfluentwidgets import PlainTextEdit


app = QApplication()
win = QPlainTextEdit()
win.setReadOnly(True)
win.show()
app.exec()