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
            phone TEXT NOT NULL,
                   status TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_user(full_name, email, phone, status):
    """Insert a new user into the database."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO users (full_name, email, phone, status)
        VALUES (?, ?, ?, ?)
    """, (full_name, email, phone, status))

    connection.commit()
    connection.close()

def user_exists(email):
    """Check if a user with the given email already exists."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT * FROM users
        WHERE email = ?
    """, (email,))

    user = cursor.fetchone()

    connection.close()

    return user

def get_all_users():
    """Return all users from the database."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT full_name, email, phone
        FROM users
    """)

    users = cursor.fetchall()

    connection.close()

    return users

def get_records():
    """Return all records from the database."""

    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        SELECT id, full_name, email, phone, status
        FROM users
        ORDER BY id ASC
    """)

    records = cursor.fetchall()

    connection.close()

    return records