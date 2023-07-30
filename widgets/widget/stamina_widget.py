from widgets import WidgetBase
from .ui.stamina_widget import StaminaWidgetUi


class StaminaWidget(WidgetBase, StaminaWidgetUi):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def get_copies_count(self) -> dict:
        copies_count = dict()
        cards = [self.calyxGoldCard, self.calyxRedCard, self.shadowCard, self.cavernCard, self.warCard]
        spin_boxs = ['calyxSpinBox', 'shadowSpinBox', 'cavernSpinBox', 'echoSpinBox']
        for card in cards:
            for widget in card.children():
                for name in spin_boxs:
                    if name in widget.objectName():
                        number = widget.objectName().split('_')[1]
                        name = name.replace('SpinBox', '')
                        copies_count[f'{name}_{number}'] = widget.value()
                        break
        return copies_count

    def __init_widget(self):
        self.scrollArea.setStyleSheet("QScrollArea { border: none; }")  # 关闭边框
        labels = [self.characterEXPLabel, self.coneEXPLabel, self.creditLabel]
        for label in labels:
            label.setFixedWidth(60)
        # 设置卡片标题
        self.calyxGoldCard.setTitleLabel(self.calyxGoldLabel)
        self.calyxRedCard.setTitleLabel(self.calyxRedLabel)
        self.shadowCard.setTitleLabel(self.stagnantShadowLabel)
        self.cavernCard.setTitleLabel(self.cavernLabel)
        self.warCard.setTitleLabel(self.warLabel)

        # 将卡片收起来
        # self.calyxGoldCard.setStretch(False)
        self.calyxRedCard.setStretch(False)
        self.shadowCard.setStretch(False)
        self.cavernCard.setStretch(False)
        self.warCard.setStretch(False)