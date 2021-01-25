import sqlite3
from typing import Tuple



def open_db(filename: str) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection, cursor: sqlite3.Cursor):
    connection.commit()
    cursor.close()
    connection.close()


def create_users_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.users(
            userID INTEGER PRIMARY KEY,
            FName TEXT
        );''')

def create_messages_table(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS main.messages(
            messageID INTEGER PRIMARY KEY,
            userID INTEGER,
            message TEXT,
            response TEXT,
            messageDate TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
            FOREIGN KEY (userID) 
            REFERENCES users(userID)
        );''')


def insert_into_users_table(cursor: sqlite3.Cursor, fname: str):
    cursor.execute('''INSERT INTO users(FName)
    VALUES(?)''', (fname,))


def insert_into_messages_table(cursor: sqlite3.Cursor, message: str, response: str, userID: int):
    cursor.execute('''INSERT INTO messages(message, response, userID)
    VALUES(?,?,?)''', (message, response, userID))



if __name__ == '__main__':
    conn, cursor = open_db("goonch_db.sqlite")
    create_users_table(cursor)
    create_messages_table(cursor)

    # insert_into_users_table(cursor, "Kyle")
    close_db(conn, cursor)
