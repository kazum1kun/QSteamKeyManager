# The main window of the QSteamKeyManager.
from PyQt5.QtWidgets import (QMainWindow, QActionGroup)
from ui.MainWindow import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        # Load UI layout defined in the ui file
        self.setupUi(self)
        self.retranslateUi(self)

        # Group language selector actions
        language_group = QActionGroup(self)
        self.action_english.setActionGroup(language_group)
        self.action_chinese_simplified.setActionGroup(language_group)
        self.action_japanese.setActionGroup(language_group)

        self.show()
