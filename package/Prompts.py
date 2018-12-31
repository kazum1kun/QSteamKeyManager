# A collection of prompts used in QSKM
from PyQt5.QtWidgets import QWidget, QMessageBox, QFileDialog
from os.path import expanduser
from package.ENV import ENV


class Prompts(QWidget):
    def __init__(self):
        super().__init__()

    # A file chooser prompt that asks for database file
    @staticmethod
    def show_db_chooser():
        db_chooser = QFileDialog()
        db_chooser.setWindowTitle('Open a QSKM Collection...')
        # User may only select the files that exists in the hdd
        db_chooser.setFileMode(QFileDialog.ExistingFile)
        db_chooser.setNameFilter('Database File (*.db)')
        db_chooser.setDirectory(expanduser(ENV.default_db_folder_path))

        # Return the full path to file back to main window if the execution was successful
        if db_chooser.exec():
            return db_chooser.selectedFiles()[0]

    # A prompt asking for confirmation on exit
    @staticmethod
    def show_exit_conf():
        exit_conf = QMessageBox()
        exit_conf.setText('<b>Save changes?</b>')
        exit_conf.setInformativeText('Your Collection has been modified. '
                                     'Do you wish to save the Collection before exit?')
        exit_conf.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        exit_conf.setDefaultButton(QMessageBox.Save)
        exit_conf.setWindowTitle('Confirm Exit')
        exit_conf.setIcon(QMessageBox.Question)


