from widgets import WidgetBase
from .ui.stamina_widget import StaminaWidgetUi


class StaminaWidget(WidgetBase, StaminaWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def get_copies_count(self) -> dict:
        copies_count = {
            "calyx_1": self.calyxSpinBox_1.value(),
            "calyx_2": self.calyxSpinBox_2.value(),
            "calyx_3": self.calyxSpinBox_3.value(),
            "calyx_4": self.calyxSpinBox_4.value(),
            "calyx_5": self.calyxSpinBox_5.value(),
            "calyx_6": self.calyxSpinBox_6.value(),
            "calyx_7": self.calyxSpinBox_7.value(),
            "calyx_8": self.calyxSpinBox_8.value(),
            "calyx_9": self.calyxSpinBox_9.value(),
            "calyx_10": self.calyxSpinBox_10.value(),
            "shadow_1":  self.shadowSpinBox_1.value(),
            "shadow_2": self.shadowSpinBox_2.value(),
            "shadow_3": self.shadowSpinBox_3.value(),
            "shadow_4": self.shadowSpinBox_4.value(),
            "shadow_5": self.shadowSpinBox_5.value(),
            "shadow_6": self.shadowSpinBox_6.value(),
            "shadow_7": self.shadowSpinBox_7.value(),
            "shadow_8": self.shadowSpinBox_8.value(),
            "shadow_9": self.shadowSpinBox_9.value(),
            "shadow_10": self.shadowSpinBox_10.value(),
            "cavern_1": self.cavernSpinBox1.value(),
            "cavern_2": self.cavernSpinBox2.value(),
            "cavern_3": self.cavernSpinBox3.value(),
            "cavern_4": self.cavernSpinBox4.value(),
            "cavern_5": self.cavernSpinBox5.value(),
            "cavern_6": self.cavernSpinBox6.value(),
            "cavern_7": self.cavernSpinBox7.value(),
            "echo_1": self.echoSpinBox1.value(),
            "echo_2": self.echoSpinBox2.value(),
            "echo_3": self.echoSpinBox3.value(),
        }

        return copies_count

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")  # 关闭边框
        labels = [self.characterEXPLabel, self.coneEXPLabel, self.creditLabel]
        for label in labels:
            label.setFixedWidth(60)
        self.calyxGoldCard.setTitleLabel(self.calyxGoldLabel)
        self.calyxRedCard.setTitleLabel(self.calyxRedLabel)
        self.shadowCard.setTitleLabel(self.stagnantShadowLabel)
        self.cavernCard.setTitleLabel(self.cavernLabel)
        self.warCard.setTitleLabel(self.warLabel)

        # 将卡片收起来
        self.calyxGoldCard.setStretch(False)
        self.calyxRedCard.setStretch(False)
        self.shadowCard.setStretch(False)
        self.cavernCard.setStretch(False)
        self.warCard.setStretch(False)