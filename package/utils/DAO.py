# Database Operation object that handles initialization of the db and CRUD operations on records.
import sqlite3
from sqlite3 import Error

from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery

from package.ENV import ENV


class DAO:
    # Placeholder database connection object
    db = None
    conn = None

    # Initialize a table where all entries will be stored
    @classmethod
    def create_table(cls, db_path=None):
        # cls.__clear_conn()
        # conn = cls.__get_or_create_conn(db_path)
        #
        # cur = conn.cursor()
        #
        # # id in the table is for "bookkeeping" use only and should be transparent to the user
        # cur.execute('''CREATE TABLE IF NOT EXISTS {} (
        #     id INTEGER PRIMARY KEY,
        #     game TEXT NOT NULL,
        #     key TEXT,
        #     notes TEXT,
        #     category TEXT,
        #     tag TEXT
        # );'''.format(ENV.game_table_name))
        #
        # cls.conn.commit()

        query = QSqlQuery()
        query.exec(
            '''CREATE TABLE IF NOT EXISTS Games (
                        id INTEGER PRIMARY KEY, 
                        game TEXT NOT NULL, 
                        key TEXT, 
                        notes TEXT,
                        category TEXT, 
                        tag TEXT)'''
        )

    # Load all games from the game table
    def load_all_games(self):
        conn = self.__get_or_create_conn()
        cur = conn.cursor()

        cur.execute('SELECT * FROM {}'.format(ENV.game_table_name))
        return cur.fetchall()

    @classmethod
    # Add an entry to the game table
    def add_a_game(cls, game, key, notes):
        # conn = cls.__get_or_create_conn()
        # cur = conn.cursor()
        #
        # cur.execute('''INSERT INTO {} (game, key, notes)
        # VALUES (?, ?, ?)'''.format(ENV.game_table_name), (game, key, notes))
        #
        # conn.commit()

        query = QSqlQuery()
        query.prepare('INSERT INTO Games (game, key, notes) VALUES (:game, :key, :notes)')
        query.bindValue(':game', game)
        query.bindValue(':key', key)
        query.bindValue(':notes', notes)
        r = query.exec()

    @classmethod
    # Remove one or more entries from the game table
    def remove_games(cls, id_list):
        conn = cls.__get_or_create_conn()
        cur = conn.cursor()

        # Remove all entries on the list (identified by their ID)
        for game_id in id_list:
            cur.execute('''DELETE FROM {} 
                WHERE id = (?)'''.format(ENV.game_table_name), (game_id,))

        conn.commit()

    # Auxiliary method to get existing connection or create a new one if not existing
    @classmethod
    def get_or_create_db(cls, db_path):
        if cls.db is None:
            try:
                # If no db_path is supplied, load the default on
                if db_path is None:
                    cls.db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
                    cls.db.setDatabaseName(':memory:')
                else:
                    cls.db.setDatabaseName(db_path)
                cls.db.open()
                return cls.db
            except Error as e:
                # TODO: further error handling
                print(e)
        else:
            if db_path is not None:
                cls.db.setDatabaseName(db_path)
                cls.db.open()
            return cls.db

    @classmethod
    # Auxiliary method to get existing connection or create a new one if not existing
    def __get_or_create_conn(cls, db_path=None):
        if cls.conn is None:
            if db_path is None:
                try:
                    cls.conn = sqlite3.connect(':memory:')
                except Error as e:
                    print(e)
            else:
                try:
                    cls.conn = sqlite3.connect(db_path)
                except Error as e:
                    print(e)

        return cls.conn

    @classmethod
    def __clear_conn(cls):
        """Auxiliary method to clear current connection to the db"""
        cls.conn = None
