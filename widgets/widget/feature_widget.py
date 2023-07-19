from widgets import WidgetBase
from .ui.feature_widget import FeatureWidgetUi


class FeatureWidget(WidgetBase, FeatureWidgetUi):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def get_copies_count(self) -> dict:
        copies_count = {
            "characterEXP": self.characterEXPSpinBox.value(),
            "coneEXP": self.coneEXPSpinBox.value(),
            "credit": self.creditSpinBox.value(),
        }

        return copies_count

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")  # 关闭边框
        labels = [self.characterEXPLabel, self.coneEXPLabel, self.creditLabel]
        for label in labels:
            label.setFixedWidth(60)
