import sqlite3
import hashlib

class Database_client:
    db_connection = sqlite3.connect('myshop.db')
    cursor = db_connection.cursor()
    def __init__(self) -> None:
        print('in db client')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE,
                password TEXT
            )
        ''')
        
    def create_user(self, username, password):

        if len(password) < 8 or ' ' in password:
            print("Password must be at least 8 characters long and cannot contain spaces")
            return

        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        self.db_connection.commit()


    
    def authenticate_user(self, username, password):
        decoded_password = hashlib.sha256(password.encode()).hexdigest()
        self.cursor.execute('SELECT * FROM users WHERE username=? AND password=?', (username, decoded_password))
        user = self.cursor.fetchone()
        return user is not None
    

db = Database_client()