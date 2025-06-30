import sqlite3

def get_db_connection():
    """Establishes and returns a SQLite database connection."""
    conn = sqlite3.connect('user_credentials.db')
    return conn

def initialize_db(cursor, connection):
    """Initializes necessary tables in the database."""
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                 (username TEXT PRIMARY KEY, password TEXT, user_type TEXT)''')
    connection.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS events
                 (event_id INTEGER PRIMARY KEY, title TEXT, description TEXT, photographer TEXT)''')
    connection.commit()

    cursor.execute('''CREATE TABLE IF NOT EXISTS event_images (
        id INTEGER PRIMARY KEY,
        event_id INTEGER,
        image_path TEXT,
        FOREIGN KEY(event_id) REFERENCES events(id)
    )''')
    connection.commit()
