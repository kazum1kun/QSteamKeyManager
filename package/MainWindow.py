# The main window of the QSteamKeyManager.
from PyQt5.QtWidgets import (QMainWindow, QActionGroup)
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt

from package.ENV import ENV
from package.DBO import DBO
from ui.MainWindow import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()
        # Load UI layout defined in the ui file
        self.setupUi(self)

        # Group language selector actions
        language_group = QActionGroup(self)
        self.action_english.setActionGroup(language_group)
        self.action_chinese_simplified.setActionGroup(language_group)
        self.action_japanese.setActionGroup(language_group)

        # Set up a SQL model
        self.model = QSqlTableModel(self, DBO.get_or_create_db())
        self.model.setTable(ENV.game_table_name)
        self.model.setEditStrategy(QSqlTableModel.OnRowChange)

        # Customize the name of headers
        self.model.setHeaderData(0, Qt.Horizontal, 'Game')
        self.model.setHeaderData(1, Qt.Horizontal, 'Key/URL')
        self.model.setHeaderData(2, Qt.Horizontal, 'Notes')
        print('{}, {}'.format(self.model.columnCount(), self.model.rowCount()))

        self.table_view_content.setModel(self.model)

        # Set the size of each columns
        self.table_view_content.setColumnWidth(0, 100)
        self.table_view_content.setColumnWidth(1, 100)
        self.table_view_content.setColumnWidth(2, 100)

        self.show()
