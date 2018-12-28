# All "global" environment variables (such as filename, path to db file) are stored here for
# easy access and modification


class Env:
    # Name of the database file (with extension)
    db_name = 'qskm.db'

    # TODO: check if this is ok in production environment
    # Relative path of the database file in the project
    rel_db_path = '..\\db\\' + db_name

    # Name of the table that stores all data related to the game, including
    # id (transparent to user), name of the game, key/url of the game, notes, category, and more
    game_table_name = 'Games'

