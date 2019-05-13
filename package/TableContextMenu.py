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

        # Present the menu on the mouse click point and perform accordingly
        action = menu.exec_(parent.table_view_content.viewport().mapToGlobal(pos))

        if action == action_copy:
            print(parent.table_view_content.selectionModel().currentIndex().data)


