# Database Operation object that handles initialization of the db and CRUD operations on records.
import sqlite3
from sqlite3 import Error

from package.Env import Env


class DBO:
    # Create a placeholder connection object
    def __init__(self):
        self.conn = None

    # Initialize a table where all entries will be stored
    def create_table(self):
        conn = self.get_or_create_conn()
        cur = conn.cursor()

        # id in the table is for "bookkeeping" use only and should be transparent to the user
        cur.execute('''CREATE TABLE IF NOT EXISTS {} (
            id INTEGER PRIMARY KEY, 
            game TEXT NOT NULL, 
            key TEXT, 
            notes TEXT,
            category TEXT, 
            tag TEXT
        );'''.format(Env.game_table_name))

        conn.commit()

    # Load all games from the game table
    def load_all_games(self):
        conn = self.get_or_create_conn()
        cur = conn.cursor()

        cur.execute('SELECT * FROM {}'.format(Env.game_table_name))
        return cur.fetchall()

    # Add an entry to the game table
    def add_a_game(self, game, key, notes):
        conn = self.get_or_create_conn()
        cur = conn.cursor()

        cur.execute('''INSERT INTO {} (game, key, notes) 
        VALUES (?, ?, ?)'''.format(Env.game_table_name), (game, key, notes))

        conn.commit()

    # Auxiliary method to get existing connection or create a new one if not existing
    def get_or_create_conn(self):
        if self.conn is None:
            try:
                self.conn = sqlite3.connect(Env.rel_db_path)
                return self.conn
            except Error as e:
                # TODO: further error handling
                print(e)
        else:
            return self.conn

dbo = DBO()
dbo.create_table()
dbo.add_a_game("Sid Meier's Civilization V", "22222-44444-66666", "All-time classic")
dbo.add_a_game("PAYDAY 2", "PPPPP-DDDDD-22222", "Funnier with friends")
dbo.add_a_game("BATTLEFIELD 5", "https://www.humblebundle.com/gift?key=AbhFOhj72h8yrHG7", "URL fits here too!")
dbo.add_a_game("STEINS;GATE", "ELPSY-CONGR-OOOOO", "EL PSY CONGROO!")
dbo.add_a_game("Mount & Blade II: Bannerlord", "GGGGG-GGGGG-GGGGG", "Not gonna happen anyways")
