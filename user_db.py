import sqlite3
from utils import print_box
import getpass
from rich.console import Console
console = Console()

def authenticate_user(users_db):
    username = input("Enter username: ",style="bold green")
    password = getpass.getpass("Enter password: ")
    
    print(f"Entered username: {username}")
    print(f"Entered password: {password}")
    
    if username in users_db and users_db[username]['password'] == password:
        print("Authentication successful!")
        return users_db[username]['role']
    else:
        print("Authentication failed.")
        return None

def connect_user_db():
    return sqlite3.connect('users.db')

def create_user_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        ''')

def add_user(conn, username, password, role):
    with conn:
        conn.execute('''
            INSERT INTO users (username, password, role)
            VALUES (?, ?, ?)
        ''', (username, password, role))
    print("User added successfully.")

def delete_user(conn, username):
    with conn:
        conn.execute('''
            DELETE FROM users WHERE username = ?
        ''', (username,))
    print("User deleted successfully.")

def update_user(conn, username, new_password, new_role):
    with conn:
        conn.execute('''
            UPDATE users SET password = ?, role = ? WHERE username = ?
        ''', (new_password, new_role, username))
    print("User updated successfully.")

from utils import print_box

def view_users(conn, role):
    with conn:
        cursor = conn.execute('SELECT id, username, password, role FROM users')
        users = cursor.fetchall()
        
        if role == 'admin':
            print_box(["ID", "Username", "Password", "Role"], users)
        else:
            users_sanitized = [(user[0], user[1], "****", user[3]) for user in users]
            print_box(["ID", "Username", "Password", "Role"], users_sanitized)
