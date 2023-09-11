from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame

from .ui.one_avatar import Ui_Frame


class AvatarGroup(QFrame, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._url = None
        self.avatar.clicked.connect(self.to_url)

    def set_name(self, name: str) -> None:
        self.name.setText(name)

    def set_pixmap(self, pixmap: QPixmap) -> None:
        self.avatar.setImage(pixmap)

    def set_url(self, url: str):
        from PySide6.QtCore import QUrl
        self._url = QUrl(url)

    def to_url(self):
        from PySide6.QtGui import QDesktopServices
        if self._url is None:
            return
        QDesktopServices.openUrl(self._url)

