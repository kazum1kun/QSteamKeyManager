# Database Operation object that handles initialization of the db and CRUD operations on records.
from sqlite3 import Error

from PyQt5 import QtSql

from package.ENV import ENV


class DAO:
    # Initially, a database is created in memory until the user save to/load from a file on disk
    # The following is a placeholder for actual connections
    conn = None

    # Initialize a table where all entries will be stored
    @classmethod
    def create_table(cls):
        query = QtSql.QSqlQuery()

        # id in the table is for "bookkeeping" use only and should be transparent to the user
        query.prepare('''CREATE TABLE IF NOT EXISTS Games (
            id INTEGER PRIMARY KEY, 
            game TEXT NOT NULL, 
            key TEXT, 
            notes TEXT,
            category TEXT, 
            tag TEXT
        );''')

        query.exec()

    @classmethod
    # Add an entry to the game table
    def add_a_game(cls, game, key, notes):
        query = QtSql.QSqlQuery()

        query.prepare('INSERT INTO Games (game, key, notes) VALUES (:game, :key, :notes)')
        query.bindValue(':game', game)
        query.bindValue(':key', key)
        query.bindValue(':notes', notes)

        query.exec()

    @classmethod
    # Remove one or more entries from the game table
    def remove_games(cls, id_list):
        query = QtSql.QSqlQuery()

        query.prepare('DELETE FROM Games WHERE id = (:id)')

        # Remove all entries on the list (identified by their ID)
        for game_id in id_list:
            query.bindValue(':id', game_id)
            query.exec()

    # Auxiliary method to get existing connection or create a new one if not existing
    @classmethod
    def get_or_create_conn(cls, db_path=None):
        try:
            # If no db_path is supplied, load the default on
            if db_path is None:
                cls.conn = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                cls.conn.setDatabaseName('db/test.db')
            else:
                cls.conn.setDatabaseName(db_path)
            return cls.conn
        except Error as e:
            # TODO: further error handling
            print(e)

    @classmethod
    def __clear_conn(cls):
        """Auxiliary method to clear current connection to the db"""
        cls.conn = None
