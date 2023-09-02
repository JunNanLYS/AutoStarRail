from .ui.info_card_widget import Ui_Form
from qfluentwidgets import StrongBodyLabel, CaptionLabel, ElevatedCardWidget


class InfoCard(ElevatedCardWidget, Ui_Form):
    def __init__(self, title: str, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self._row = 0
        self.setStyleSheet(
            """
            background: rgb(255, 255, 255, 80);
            """
        )
        self.title_label.setText(title)
        self.title_label.setStyleSheet(
            """
            background: rgb(255, 255, 255, 255);
            """
        )
        self.setFixedSize(400, 270)
        self.verticalLayout.setSpacing(20)

    def _get_title_label(self, text: str):
        from PySide6.QtCore import Qt
        label = StrongBodyLabel(self)
        label.setStyleSheet(
            """
            background:rgb(255, 255, 255, 255);
            """
        )
        label.setText(text)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        return label

    def _get_content_label(self, text: str):
        from PySide6.QtCore import Qt
        label = CaptionLabel(self)
        label.setStyleSheet(
            """
            background:rgb(255, 255, 255, 255);
            """
        )
        label.setText(text)
        label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        return label

    def add_info(self, title: str, content: str):
        self.grid_layout.addWidget(self._get_title_label(title), self._row, 0)
        self.grid_layout.addWidget(self._get_content_label(content), self._row, 1)
        self._row += 1
