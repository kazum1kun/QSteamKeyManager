from os.path import expanduser

from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog

from package.ENV import ENV


class Prompts(QWidget):
    """A collection of prompts used in QSKM."""
    def __init__(self):
        super().__init__()

    @staticmethod
    def show_db_chooser():
        """A file chooser prompt that asks for a database file."""
        db_chooser = QFileDialog()
        db_chooser.setWindowTitle('Open a QSKM Collection...')
        # User may only select the files that exists in the hdd
        db_chooser.setFileMode(QFileDialog.ExistingFile)
        db_chooser.setNameFilter('Database File (*.db)')
        db_chooser.setDirectory(expanduser(ENV.default_db_folder_path))

        # Return the full path to file back to main window if the execution was successful
        if db_chooser.exec():
            return db_chooser.selectedFiles()[0]

    @staticmethod
    def show_file_chooser():
        """A file chooser prompt that asks for a (text) file to import."""
        file_chooser = QFileDialog()
        file_chooser.setWindowTitle('Open a QSKM Collection...')
        # User may only select the files that exists in the hdd
        file_chooser.setFileMode(QFileDialog.ExistingFile)
        # Will use the file's MIME type to determine autodetect
        filters = ['Auto Detect (*)',
                   'Text File (*.txt)',
                   'Excel File (*.xlsx, *.xls)',
                   'Database File (*.db)']

        file_chooser.setNameFilters(filters)
        file_chooser.setDirectory(expanduser(ENV.default_db_folder_path))

        # Return the full path to file back to main window if the execution was successful
        if file_chooser.exec():
            return file_chooser.selectedFiles()[0]

    @staticmethod
    def show_exit_conf():
        """A prompt asking for confirmation on exit."""
        exit_conf = QMessageBox()
        exit_conf.setIcon(QMessageBox.Question)
        exit_conf.setText('<b>Confirm Exit</b>')
        exit_conf.setInformativeText('Do you want to exit?\n'
                                     'All changes have been saved automatically.')
        exit_conf.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        exit_conf.setDefaultButton(QMessageBox.Yes)
        exit_conf.setWindowTitle('Exiting QSKM')
        user_choice = exit_conf.exec()

        if user_choice == QMessageBox.Yes:
            exit(0)
