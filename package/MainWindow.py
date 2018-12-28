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

        # Table view and model
        self.setup_model()
        self.setup_view()

        # Top toolbar
        self.setup_language_grouping()

        # Showtime!
        self.show()

    # Set up the model in the table and link it to the view
    def setup_model(self):
        # Set up a SQL model
        model = QSqlTableModel(self, DBO.get_or_create_db())
        model.setTable(ENV.game_table_name)
        model.setEditStrategy(QSqlTableModel.OnRowChange)

        # Customize the name of headers
        model.setHeaderData(1, Qt.Horizontal, 'Game')
        model.setHeaderData(2, Qt.Horizontal, 'Key/URL')
        model.setHeaderData(3, Qt.Horizontal, 'Notes')
        model.select()

        # Link table model to the table view
        self.table_view_content.setModel(model)

    # Tweak some setting in the view
    def setup_view(self):
        # Set the size of each columns
        self.table_view_content.setColumnWidth(1, 250)
        self.table_view_content.setColumnWidth(2, 250)
        self.table_view_content.setColumnWidth(3, 100)

        # Hide some columns: id, category, and tag
        self.table_view_content.hideColumn(0)
        self.table_view_content.hideColumn(4)
        self.table_view_content.hideColumn(5)

    # Set up grouping in the language selector
    def setup_language_grouping(self):
        # Group language selector actions
        language_group = QActionGroup(self)
        self.action_english.setActionGroup(language_group)
        self.action_chinese_simplified.setActionGroup(language_group)
        self.action_japanese.setActionGroup(language_group)
