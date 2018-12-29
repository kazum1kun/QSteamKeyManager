# A collection of prompts used in QSKM
from PyQt5.QtWidgets import QWidget, QMessageBox


class Prompts(QWidget):
    def __init__(self):
        super().__init__()

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
        print(exit_conf.exec())
