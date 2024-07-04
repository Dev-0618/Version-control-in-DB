import os

def clear_screen():
    # Clear command based on the OS
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
