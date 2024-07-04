import sqlite3

def connect_user_db(db_name='user_database.db'):
    conn = sqlite3.connect(db_name)
    return conn

def create_user_table(conn):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            );
        """)

def add_user(conn, username, password, role):
    with conn:
        conn.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?);", (username, password, role))

def delete_user(conn, username):
    with conn:
        conn.execute("DELETE FROM users WHERE username = ?;", (username,))

def update_user(conn, username, new_password, new_role):
    with conn:
        conn.execute("UPDATE users SET password = ?, role = ? WHERE username = ?;", (new_password, new_role, username))

def view_users(conn):
    cursor = conn.execute("SELECT * FROM users;")
    for row in cursor:
        print(row)
