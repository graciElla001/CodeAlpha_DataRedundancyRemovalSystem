import sqlite3

DATABASE_NAME = "data.db"


def create_database():
    """Create the database and users table if they do not already exist."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            phone TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()