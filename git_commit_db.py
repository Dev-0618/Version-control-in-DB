import sqlite3

def connect_git_commit_db(db_name='git_commit_database.db'):
    conn = sqlite3.connect(db_name)
    return conn

def create_git_commit_table(conn):
    with conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS commits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                commit_id TEXT NOT NULL,
                branch_name TEXT NOT NULL,
                commit_message TEXT NOT NULL,
                file_content TEXT NOT NULL
            );
        """)

def save_git_commit(conn, commit_id, branch_name, commit_message, file_content):
    with conn:
        conn.execute("INSERT INTO commits (commit_id, branch_name, commit_message, file_content) VALUES (?, ?, ?, ?);", 
                     (commit_id, branch_name, commit_message, file_content))

def view_commits(conn):
    cursor = conn.execute("SELECT * FROM commits;")
    for row in cursor:
        print(row)
