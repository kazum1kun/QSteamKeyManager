# A context menu for the table
import pyperclip
import webbrowser
from PyQt5.QtWidgets import QMenu, QAction
from package.DAO import DAO


class TableContextMenu:
    @staticmethod
    def show(parent, pos):
        # Define a menu and some actions
        menu = QMenu(parent)
        action_copy_key = QAction("Copy Key", menu)
        action_copy_name = QAction("Copy Name", menu)
        action_copy_notes = QAction("Copy Notes", menu)
        action_delete = QAction("Remove", menu)
        menu_search_game = QMenu("Search on...", menu)
        action_search_steam = QAction("Steam", menu_search_game)
        action_search_gog = QAction("GOG", menu_search_game)
        action_search_itch = QAction("itch.io", menu_search_game)
        action_search_origin = QAction("Origin", menu_search_game)
        action_search_uplay = QAction("Uplay", menu_search_game)
        menu.addAction(action_copy_key)
        menu.addAction(action_copy_name)
        menu.addAction(action_copy_notes)
        menu.addAction(action_delete)
        menu.addSeparator()
        menu.addMenu(menu_search_game)
        menu_search_game.addAction(action_search_steam)
        menu_search_game.addAction(action_search_gog)
        menu_search_game.addAction(action_search_itch)
        menu_search_game.addAction(action_search_origin)
        menu_search_game.addAction(action_search_uplay)

        # Present the menu on the mouse click point and perform accordingly
        action = menu.exec_(parent.table_view_content.viewport().mapToGlobal(pos))

        # Copy the key on the row currently selected by the user
        if action == action_copy_key:
            current_index = parent.table_view_content.selectionModel().currentIndex()
            pyperclip.copy(current_index.sibling(current_index.row(), 2).data())

        # Copy the key on the row currently selected by the user
        elif action == action_copy_name:
            current_index = parent.table_view_content.selectionModel().currentIndex()
            pyperclip.copy(current_index.sibling(current_index.row(), 1).data())

        # Copy the key on the row currently selected by the user
        elif action == action_copy_notes:
            current_index = parent.table_view_content.selectionModel().currentIndex()
            pyperclip.copy(current_index.sibling(current_index.row(), 3).data())

        # Delete row(s) selected by the user
        elif action == action_delete:
            sel = parent.table_view_content.selectionModel().selection()
            rowid_set = set()
            # Select column 0 (hidden) on each row user selected which contains the ID of the row
            # Add them to a set to prevent duplicates
            for index in sel.indexes():
                rowid_set.add(index.sibling(index.row(), 0).data())
            DAO.remove_games(rowid_set)

            # Refresh the model to show changes
            parent.table_view_content.model().sourceModel().select()

        # Launch a browser and search for the game on Steam
        elif action == action_search_steam:
            current_index = parent.table_view_content.selectionModel().currentIndex()
            game = current_index.sibling(current_index.row(), 1).data()
            webbrowser.open("https://store.steampowered.com/search/?term={}".format(game), 2)

