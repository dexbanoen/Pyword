import hashlib #hashlib for security
import getpass #getpass to hide typing

password_manager = {} # empty dictionnary to be populated

def create_account():
    username = input("Enter a username: ")
    password = getpass.getpass("Enter a password: ") #getpass visibly hides password 
    hashed_password = hashlib.sha256(password.encode()).hexdigest() #into bytes, then hashed (binary), into hexadecimal form
    password_manager[username] = hashed_password # key value pairing
    print("Account created successfully!")

def login():
    username = input("Enter your username: ")
    password = getpass.getpass("Enter your password: ")
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    if username in password_manager.keys() and password_manager[username] == hashed_password: # checks if in dictionnary and password matches
        print("Login successful!")
    else:
        print("Invalid username or password.")

def main(): # basic interface
    while True:
        choice = input("Enter 1 to create an account, 2 to login, or 0 to exit: ")
        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "0":
            break
        else:
            print("Invalid choice.")

main()
