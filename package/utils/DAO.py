# Database Operation object that handles initialization of the db and CRUD operations on records.
from PyQt5 import QtSql
from PyQt5.QtSql import QSqlQuery


class DAO:
    # Placeholder database connection object
    db = None

    # Initialize a table where all entries will be stored
    @classmethod
    def create_table(cls, db_conn=None):
        db = db_conn if db_conn else cls.db
        query = QSqlQuery(db)
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
    @classmethod
    def load_all_games(cls, db_conn=None):
        db = db_conn if db_conn else cls.db
        query = QSqlQuery(db)
        query.exec('SELECT * FROM Games')

        return query

    @classmethod
    # Add an entry to the game table
    def add_a_game(cls, game, key, notes, db_conn=None):
        db = db_conn if db_conn else cls.db
        query = QSqlQuery(db)
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

    @classmethod
    # Save current database content in memory to a file on HDD
    def create_memory_dump(cls, db_path):
        # Create the connection to new db
        dump_db = QtSql.QSqlDatabase.addDatabase('QSQLITE', 'dump-db')
        dump_db.setDatabaseName(db_path)
        dump_db.open()

        # Create the table and fill it with data
        cls.create_table(dump_db)
        temp_records = cls.load_all_games()
        while temp_records.next():
            cls.add_a_game(temp_records.value('game'), temp_records.value('key'), temp_records.value('notes'), dump_db)

    # Auxiliary method to get existing connection or create a new one if not existing
    @classmethod
    def get_or_create_db(cls, db_path):
        if cls.db is None:
            # If no db_path is supplied, load the default on
            cls.db = QtSql.QSqlDatabase.addDatabase('QSQLITE', 'in-memory')
            if db_path is None:
                cls.db.setDatabaseName(':memory:')
            else:
                cls.db.setDatabaseName(db_path)
            cls.db.open()
        else:
            if db_path is not None:
                cls.db.setDatabaseName(db_path)
                cls.db.open()
        return cls.db

    @classmethod
    def __clear_db(cls):
        """Auxiliary method to clear current connection to the db"""
        cls.db = None
