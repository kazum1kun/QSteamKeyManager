# The main window of the QSteamKeyManager.
from PyQt5.QtWidgets import (QMainWindow, QActionGroup)
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtCore import Qt

from package.ENV import ENV
from package.DBO import DBO
from package.Prompts import Prompts
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

        # Internal wiring (slots & signals)
        self.setup_signals()

        # Showtime!
        self.show()

    # Define events (signals) in the main window
    def setup_signals(self):
        # User clicks on "Open Collection" -> Show a file chooser promptp
        self.action_open_collection.triggered.connect(Prompts.show_db_chooser)

        # User clicks on "Exit" -> "Confirm Exit" prompt
        self.action_exit.triggered.connect(Prompts.show_exit_conf)

        # User clicks on "Add" -> Check and add an entry to the table
        self.pushButton_add.clicked.connect(self.add_entry)

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

    # Add a new entry to the collection
    def add_entry(self):
        game = self.lineEdit_game.text().strip()
        key = self.lineEdit_key.text().strip()
        notes = self.lineEdit_notes.text().strip()
        # Check if both game and key fields are filled
        # Note: PEP 8: For sequences, (strings, lists, tuples), use the fact that empty sequences are false.
        if game and key:
            # Add the texts in the database and clear the contents
            # Changes are automatically saved
            DBO.add_a_game(game, key, notes)
            self.lineEdit_game.clear()
            self.lineEdit_key.clear()
            self.lineEdit_notes.clear()

            # Refresh the model to show the changes
            self.table_view_content.model().select()
