import sqlite3
import hashlib

class Database_client:
    def __init__(self, db_file='myshop.db'):
        self.db_file = db_file

    def _get_connection(self):
        return sqlite3.connect(self.db_file)

    def create_tables(self):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                username TEXT UNIQUE,
                                password TEXT
                            )''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS products (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                name TEXT,
                                category TEXT,
                                price REAL
                            )''')

    def create_user(self, username, password):
        if len(password) < 8 or ' ' in password:
            raise ValueError("Password must be at least 8 characters long and cannot contain spaces")

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()

    def authenticate_user(self, username, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, hashed_password))
            user = cursor.fetchone()
            return bool(user)

db = Database_client()

