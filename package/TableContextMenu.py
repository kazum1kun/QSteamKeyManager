# A context menu for the table
from PyQt5.QtWidgets import QMenu, QAction


class TableContextMenu:
    @staticmethod
    def show(parent, pos):
        # Define a menu and some actions
        menu = QMenu(parent)
        action_delete = QAction("Delete", parent)
        action_copy = QAction("Copy Key", parent)
        menu.addAction(action_copy)
        menu.addAction(action_delete)
        # action = menu.exec_(parent.mapToGlobal(pos))

        # Present the menu on the mouse click point
        menu.popup(parent.table_view_content.viewport().mapToGlobal(pos))
