from widgets import WidgetBase
from .ui.stamina_widget import StaminaWidgetUi


class StaminaWidget(WidgetBase, StaminaWidgetUi):
    def __init__(self, parent):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def get_copies_count(self) -> dict:
        copies_count = {
            "characterEXP": self.characterEXPSpinBox.value(),
            "coneEXP": self.coneEXPSpinBox.value(),
            "credit": self.creditSpinBox.value(),
            "calyxDestruction": self.calyxDestructionSpinBox.value(),
            "calyxPreservation": self.calyxPreservationSpinBox.value(),
            "calyxHunt": self.calyxHuntSpinBox.value(),
            "calyxAbundance": self.calyxAbundanceSpinBox.value(),
            "calyxErudition": self.calyxEruditionSpinBox.value(),
            "calyxHarmony": self.calyxHarmonySpinBox.value(),
            "calyxNihility": self.calyxNihilitySpinBox.value()
        }

        return copies_count

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")  # 关闭边框
        labels = [self.characterEXPLabel, self.coneEXPLabel, self.creditLabel]
        for label in labels:
            label.setFixedWidth(60)
        self.calyxGoldCard.setTitleLabel(self.calyxGoldLabel)
        self.calyxRedCard.setTitleLabel(self.calyxRedLabel)
        # self.shadowCard.setTitleLabel()
        # self.cavernCard.setTitleLabel()
        # self.warCard.setTitleLabel()