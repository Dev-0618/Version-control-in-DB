import os
import time
from rich.console import Console
from rich.align import Align
from auth import authenticate_user, authorize_admin
from user_db import connect_user_db, create_user_table, add_user, delete_user, update_user, view_users
from git_commit_db import connect_git_commit_db, create_git_commit_table, save_git_commit, view_commits, update_commit, delete_commit, search_commits
from git_ops import fetch_commit_file, save_commit_file
from animations import welcome_animation, loading_animation
from utils import clear_screen, print_box

console = Console()

def main():
    console.print(Align.center(r"""     Developed by: Team CiPH3rHuB""", style="bold red"))
                               
    console.print(Align.center(r"""      Team members: https://github.com/Dev-0618/
                    Jaslin Ebenezer I
                    https://github.com/bushrazmulla/
                    Nazima Khanum""", style="bold blue"))
    time.sleep(1)

    welcome_animation()
    print()
    loading_animation()
    print()
    time.sleep(1)
    user_conn = connect_user_db()
    create_user_table(user_conn)
    
    users_db = {
        "admin": {"password": "adminpass", "role": "admin"},
        "guest": {"password": "guestpass", "role": "guest"}
    }
    
    role = authenticate_user(users_db)
    if role:
        clear_screen()
        loading_animation()
        
        git_commit_conn = connect_git_commit_db(role)
        create_git_commit_table(git_commit_conn)
        
        while True:
            clear_screen()
            user_actions = [
                "1. View Users",
                "2. Add User",
                "3. Delete User",
                "4. Update User",
            ]
            
            git_commit_actions = [
                "5. Fetch and Save Git Commit File",
                "6. View Git Commits",
                "7. Update Git Commit",
                "8. Delete Git Commit",
                "9. Search Git Commits",
            ]
            
            menu_options = [
                [user_actions[i] if i < len(user_actions) else "", 
                 git_commit_actions[i] if i < len(git_commit_actions) else ""]
                for i in range(max(len(user_actions), len(git_commit_actions)))
            ]
            
            print_box(["User Actions", "Git Commit Actions"], menu_options)
            print("\n10. Exit")
            
            choice = input("Enter your choice: ")
            clear_screen()
            
            if choice == '1':
                view_users(user_conn, role)
            elif choice == '2' and authorize_admin(role):
                username = input("Enter new username: ")
                password = input("Enter new password: ")
                user_role = input("Enter role (admin/guest): ")
                add_user(user_conn, username, password, user_role)
            elif choice == '3' and authorize_admin(role):
                username = input("Enter username to delete: ")
                delete_user(user_conn, username)
            elif choice == '4' and authorize_admin(role):
                username = input("Enter username to update: ")
                new_password = input("Enter new password: ")
                new_role = input("Enter new role (admin/guest): ")
                update_user(user_conn, username, new_password, new_role)
            elif choice == '5':
                repo_path = input("Enter the path to your local Git repository: ")
                commit_id = input("Enter the commit ID: ")
                file_path = input("Enter the relative file path in the repository: ")
                save_path = input("Enter the full path to save the file: ")

                if not os.path.isdir(repo_path):
                    print("Invalid repository path.")
                    continue
                if not os.path.isabs(save_path):
                    print("Save path must be an absolute path.")
                    continue

                content = fetch_commit_file(commit_id, repo_path, file_path)
                if content:
                    save_commit_file(content, save_path)
                    branch_name = input("Enter the branch name: ")
                    commit_message = input("Enter the commit message: ")
                    date = time.strftime("%Y-%m-%d %H:%M:%S")
                    save_git_commit(git_commit_conn, commit_id, branch_name, commit_message, date, content)
            elif choice == '6':
                view_commits(git_commit_conn)
            elif choice == '7':
                commit_id = input("Enter the commit ID to update: ")
                new_message = input("Enter the new commit message: ")
                new_date = time.strftime("%Y-%m-%d %H:%M:%S")
                new_content = input("Enter the new content: ")
                update_commit(git_commit_conn, commit_id, new_message, new_date, new_content)
            elif choice == '8':
                commit_id = input("Enter the commit ID to delete: ")
                delete_commit(git_commit_conn, commit_id)
            elif choice == '9':
                search_term = input("Enter the search term (commit ID, message, or date): ")
                search_commits(git_commit_conn, search_term)
            elif choice == '10':
                break
            else:
                print("Invalid choice!")
            
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()
