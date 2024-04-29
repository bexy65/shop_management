import sqlite3
import hashlib

class DatabaseClient:
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
                                name TEXT UNIQUE,
                                category TEXT,
                                price REAL,
                                count INTEGER,
                                FOREIGN KEY (category_id) REFERENCES categories(id)
                            )''')
            cursor.execute('''CREATE TABLE IF NOT EXISTS categories (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    name TEXT UNIQUE
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

    def add_category(self, name):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO categories (name) VALUES (?)', (name,))
            conn.commit()
    
    def get_categories(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT name FROM categories')
                categories = cursor.fetchall()
                category_names = [category[0] for category in categories]
                return category_names
            
        except Exception as e:
            print("Error:", e)
            return None
    
    
    def get_products(self):
        try:
            with self._get_connection() as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT name, price, count, category FROM products')
                products = cursor.fetchall()
                print(products)
                return products                
        except Exception as e:
            print('Error:', e)
            return None
    
    def add_product(self, product):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO products (name, category, price, count) VALUES (?, ?, ?, ?)', (product['name'], product['category'], product['price'], product['count']))
            conn.commit()
    
    def remove_product(self, product_name):
        with self._get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM products WHERE name=?', (product_name))
            conn.commit()
    
 
            
db = DatabaseClient()

db.get_products()