import getpass

def authenticate_user(users_db):
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")
    if username in users_db and users_db[username]['password'] == password:
        return users_db[username]['role']
    else:
        print("Authentication failed.")
        return None

def authorize_admin(role):
    return role == 'admin'
