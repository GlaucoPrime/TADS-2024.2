import sqlite3

def connect_db(db_name: str):
    """
    CONNECT to an existent data base
    IF not exist, it will create one.

    args
        db_name (str): A database name
    """
    conn = sqlite3.connect(db_name)

    return conn
 