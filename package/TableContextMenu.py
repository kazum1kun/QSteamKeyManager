# A context menu for the table
from PyQt5.QtWidgets import QMenu, QAction
from package.DBO import DBO


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

        # Delete row(s) selected by the user
        if action == action_delete:
            sel = parent.table_view_content.selectionModel().selection()
            rowid_set = set()
            # Select column 0 (hidden) on each row user selected which contains the ID of the row
            # Add them to a set to prevent duplicates
            for index in sel.indexes():
                rowid_set.add(index.sibling(index.row(), 0).data())
            DBO.remove_games(rowid_set)

            # Refresh the model to show changes
            parent.table_view_content.model().sourceModel().select()

