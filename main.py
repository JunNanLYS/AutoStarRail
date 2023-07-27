import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.resize(500, 500)
window.show()
app.exec()

# pyinstaller --distpath . --workpath pack --specpath pack -i helpme.ico -F -w main.py
