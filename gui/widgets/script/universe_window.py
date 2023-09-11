from qframelesswindow import FramelessDialog

from .ui.universe import Ui_Frame


class UniverseWindow(FramelessDialog, Ui_Frame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.__init_widget()

    def __init_combobox(self):
        from config import cfg
        difficulty = ["1", "2", "3", "4", "5"]
        fate = ["存护", "记忆", "虚无", "丰饶", "巡猎", "毁灭", "欢愉", "繁育"]
        number = ["3", "4", "5", "6", "7"]
        self.combobox_difficulty.addItems(difficulty)
        self.combobox_difficulty.setCurrentText(str(cfg.get(cfg.universe_difficult)))

        self.combobox_fate.addItems(fate)
        self.combobox_fate.setCurrentText(str(cfg.get(cfg.universe_fate)))

        self.combobox_number.addItems(number)
        self.combobox_number.setCurrentText(str(cfg.get(cfg.universe_number)))

    def __init_checkbox(self):
        from config import cfg
        self.checkbox_show_map.setChecked(cfg.get(cfg.universe_show_map))
        self.checkbox_speed.setChecked(cfg.get(cfg.universe_speed))
        self.checkbox_debug.setChecked(cfg.get(cfg.universe_debug))
        self.checkbox_update.setChecked(cfg.get(cfg.universe_update))

    def __on_yes_button_clicked(self):
        """yes button clicked slot"""
        from config import cfg
        difficulty = self.combobox_difficulty.currentText()
        fate = self.combobox_fate.currentText()
        number = self.combobox_number.currentText()
        show_map = int(self.checkbox_show_map.isChecked())
        speed = int(self.checkbox_speed.isChecked())
        debug = int(self.checkbox_debug.isChecked())
        update = int(self.checkbox_update.isChecked())

        cfg.set(cfg.universe_difficult, int(difficulty))
        cfg.set(cfg.universe_fate, fate)
        cfg.set(cfg.universe_number, int(number))
        cfg.set(cfg.universe_show_map, show_map)
        cfg.set(cfg.universe_speed, speed)
        cfg.set(cfg.universe_debug, debug)
        cfg.set(cfg.universe_update, update)

    def __connect_signal_to_slot(self):
        # close button disconnect and connect to hide slot
        self.titleBar.closeBtn.clicked.disconnect(self.close)
        self.titleBar.closeBtn.clicked.connect(self.hide)

        self.button_no.clicked.connect(self.__init_checkbox)
        self.button_no.clicked.connect(self.__init_combobox)
        self.button_no.clicked.connect(self.hide)

        self.button_yes.clicked.connect(self.__on_yes_button_clicked)
        self.button_yes.clicked.connect(self.hide)

    def __init_widget(self):
        self.__init_checkbox()
        self.__init_combobox()
        self.__connect_signal_to_slot()
