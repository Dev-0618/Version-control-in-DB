import sqlite3
from utils import print_box

def connect_git_commit_db(user):
    return sqlite3.connect(f'{user}_git_commits.db')

def create_git_commit_table(conn):
    with conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS git_commits (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                commit_id TEXT NOT NULL,
                branch TEXT NOT NULL,
                message TEXT NOT NULL,
                date TEXT NOT NULL,
                content TEXT NOT NULL
            )
        ''')

def save_git_commit(conn, commit_id, branch, message, date, content):
    with conn:
        conn.execute('''
            INSERT INTO git_commits (commit_id, branch, message, date, content)
            VALUES (?, ?, ?, ?, ?)
        ''', (commit_id, branch, message, date, content))
    print("Commit saved successfully.")

def view_commits(conn):
    with conn:
        cursor = conn.execute('SELECT id, commit_id, branch, message, date, content FROM git_commits')
        commits = cursor.fetchall()
        print_box(["ID", "Commit ID", "Branch", "Message", "Date", "Content"], commits)

def update_commit(conn, commit_id, new_message, new_date, new_content):
    with conn:
        conn.execute('''
            UPDATE git_commits
            SET message = ?, date = ?, content = ?
            WHERE commit_id = ?
        ''', (new_message, new_date, new_content, commit_id))
    print("Commit updated successfully.")

def delete_commit(conn, commit_id):
    with conn:
        conn.execute('''
            DELETE FROM git_commits WHERE commit_id = ?
        ''', (commit_id,))
    print("Commit deleted successfully.")

def search_commits(conn, search_term):
    with conn:
        cursor = conn.execute('''
            SELECT id, commit_id, branch, message, date, content
            FROM git_commits
            WHERE commit_id LIKE ? OR message LIKE ? OR date LIKE ?
        ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))
        commits = cursor.fetchall()
        print_box(["ID", "Commit ID", "Branch", "Message", "Date", "Content"], commits)
