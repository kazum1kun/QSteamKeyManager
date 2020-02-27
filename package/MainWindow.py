# The main window of the QSteamKeyManager.
import magic
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QRegExp
from PyQt5.QtSql import QSqlTableModel
from PyQt5.QtWidgets import QMainWindow, QActionGroup, QDialog

from package.AboutMe import AboutMe
from package.ENV import ENV
from package.Prompts import Prompts
from package.TableContextMenu import TableContextMenu
from package.utils.DAO import DAO
from package.utils.TextReader import TextReader
from ui.MainWindow import Ui_main_window


class MainWindow(QMainWindow, Ui_main_window):
    def __init__(self):
        super().__init__()

        # Declare some important instance attrs
        self.proxy_model = None

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
        # User clicks on "Open Collection" -> Show a file chooser prompt (limited to .db type)
        self.action_open_collection.triggered.connect(self.load_db)

        # User clicks on "Import From File" -> Shows a file chooser prompt
        self.action_import_from_file.triggered.connect(self.load_file)

        # User clicks on "Exit" -> "Confirm Exit" prompt
        self.action_exit.triggered.connect(Prompts.show_exit_conf)

        # User clicks on "Add" -> Check and add an entry to the table
        self.pushButton_add.clicked.connect(self.add_entry)

        # User clicks on "About" -> "About QSKM" dialog shows
        self.action_about_qskm.triggered.connect(self.show_about_me)

        # User enter or delete text from the search box -> Update model filter
        self.lineEdit_search.textChanged.connect(self.filter_entries)

        # User clicks "Clear" -> Search box gets cleared
        self.pushButton_clear.clicked.connect(self.lineEdit_search.clear)

        # User right clicks the table -> A context menu shows up with various features
        self.table_view_content.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table_view_content.customContextMenuRequested.connect(self.show_table_context_menu)

    # Set up the model in the table and link it to the view
    def setup_model(self):
        # Add a filter model to filter (search) items, which in turn includes a SQL model
        self.proxy_model = QSortFilterProxyModel()
        # Set search column to -1 to search from all columns
        # this will also search for entry's id which might not be a good idea
        # TODO: maybe reimplement QSFPM to have custom columns?
        self.proxy_model.setFilterKeyColumn(-1)

        # Set up underlying SQL model
        self.setup_sql_model(None)

        # Link table model to the table view
        self.table_view_content.setModel(self.proxy_model)

    def setup_sql_model(self, db_path):
        """Set up an SQL model to plug into the proxy model"""
        # Set up a SQL model
        model = QSqlTableModel(self, DAO.get_or_create_conn(db_path))
        model.setTable('Games')
        model.setEditStrategy(QSqlTableModel.OnRowChange)
        self.proxy_model.setSourceModel(model)

        # Customize the name of headers
        model.setHeaderData(1, Qt.Horizontal, 'Game')
        model.setHeaderData(2, Qt.Horizontal, 'Key/URL')
        model.setHeaderData(3, Qt.Horizontal, 'Notes')
        model.select()

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
            DAO.add_a_game(game, key, notes)
            self.lineEdit_game.clear()
            self.lineEdit_key.clear()
            self.lineEdit_notes.clear()

            # Refresh the model to show the changes
            self.table_view_content.model().sourceModel().select()

    # Filter entries after keyword changes
    def filter_entries(self):
        keyword = self.lineEdit_search.text().strip()

        # Apply keywords as regexp (case insensitive)
        self.table_view_content.model().setFilterRegExp(QRegExp(keyword, Qt.CaseInsensitive))

    # Bring up a context menu
    def show_table_context_menu(self, pos):
        TableContextMenu.show(self, pos)

    # Detour close events to the prompt
    def closeEvent(self, event):
        Prompts.show_exit_conf()
        # If the window doesn't get closed at this point, ignore the event.
        event.ignore()

    @staticmethod
    def show_about_me():
        """Shows a 'About QSKM' page along with other nice stuff"""
        about_me = QDialog()
        ui = AboutMe()
        ui.setupUi(about_me)
        ui.setup_signals()
        about_me.exec()

    def load_db(self):
        db_path = Prompts.show_db_chooser()
        self.setup_sql_model(db_path)

    def load_file(self):
        """Invoke the window to read, parse and load user-selected files"""
        user_file = Prompts.show_file_chooser()
        parsed_file = []

        checker = magic.Magic(mime=True)
        file_mime_type = checker.from_file(user_file)
        # Reference:    .xls    	application/vnd.ms-excel
        #               .xlsx       application/vnd.openxmlformats-officedocument.spreadsheetml.sheet
        #               .txt        text/plain
        #               .db         application/x-sqlite3  ------> applicable to only sqlite db
        if file_mime_type == 'text/plain':
            parsed_file = TextReader.read(user_file, ';')
        # TODO process other file type here

        # TODO Ask user if they want to append it to the Collection or make a new one
        # In case the user wants a new one, create a new table
        DAO.create_table()

        # Since empty notes are already taken care of in TextReader, we can safely
        for items in parsed_file:
            DAO.add_a_game(items['game'], items['key'], items['notes'])

        # Refresh the view to show newly imported keys
        self.table_view_content.model().sourceModel().select()
