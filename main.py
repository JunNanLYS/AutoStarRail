import sys

from PySide6.QtWidgets import QApplication

from gui.main_window import MainWindow

app = QApplication(sys.argv)
window = MainWindow()
window.resize(700, 600)
window.show()
sys.exit(app.exec())

# pyinstaller --distpath . --workpath pack --specpath pack -i helpme.ico -F -w main.py
# pyinstaller --hidden-import PySide6 -F -w main.py
