from auth import authenticate_user, authorize_admin
from user_db import connect_user_db, create_user_table, add_user, delete_user, update_user, view_users
from git_commit_db import connect_git_commit_db, create_git_commit_table, save_git_commit, view_commits
from git_ops import fetch_commit_file, save_commit_file
from animations import welcome_animation, loading_animation
from utils import clear_screen
import os
import time

print(r"""
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
$   ____   _   ____    _   _   _____   ____    $
$  / ___| (_) |  _ \  | | | | |___ /  |  _ \   $
$  | |    | | | |_) | | |_| |   |_ \  | |_) |  $
$  | |___ | | |  __/  |  _  |  ___) | |  _ <   $
$  \____| |_| |_|  ___|_| |_| |____/  |_| \_\  $
$  | | | |  _   _  | __ )                      $
$  | |_| | | | | | |  _ \                      $ 
$  |  _  | | |_| | | |_) |                     $
$  |_| |_|  \__,_| |____/                      $
$                                              $
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
      Developed by: Team CiPH3rHuB
      Team members: https://github.com/Dev-0618/
                    Jaslin Ebenezer I
                    https://github.com/bushrazmulla/
                    Nazima Khanum""")
time.sleep(1)

print("Welcome....")
time.sleep(1.5)

def main():
    welcome_animation()
    
    user_conn = connect_user_db()
    create_user_table(user_conn)
    
    git_commit_conn = connect_git_commit_db()
    create_git_commit_table(git_commit_conn)
    
    users_db = {
        "admin": {"password": "adminpass", "role": "admin"},
        "guest": {"password": "guestpass", "role": "guest"}
    }
    
    role = authenticate_user(users_db)
    if role:
        loading_animation()
        
        while True:
            clear_screen()  # Clear the screen before showing the menu
            print("1. View Users")
            if role == 'admin':
                print("2. Add User")
                print("3. Delete User")
                print("4. Update User")
            print("5. Fetch and Save Git Commit File")
            print("6. View Git Commits")
            print("7. Exit")
            choice = input("Enter your choice: ")
            
            clear_screen()  # Clear the screen after a choice is made
            
            if choice == '1':
                view_users(user_conn)
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

                # Validate paths
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
                    save_git_commit(git_commit_conn, commit_id, branch_name, commit_message, content)
            elif choice == '6':
                view_commits(git_commit_conn)
            elif choice == '7':
                break
            else:
                print("Invalid choice!")
            
            input("Press Enter to continue...")  # Wait for user input before clearing the screen

if __name__ == "__main__":
    main()
