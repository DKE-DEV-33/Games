# Import Fernet module for encryption/decryption
from cryptography.fernet import Fernet

# Function to write a new key (only run once)
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# Function to load the existing key
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

# Function to encrypt a password
def view():
    for line in open("passwords.txt", "r").readlines():
        data = line.rstrip()
        user, password, site = data.split("|")
        print("Website:", site, "| Account:", user, "| Password:", fer.decrypt(password.encode()))

# Function to add a new password
def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    site = input("Website: ")

    with open("passwords.txt", "a") as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "|" + site + "\n")


# Prompt for master password (not used in this simple version)
master_pwd = input("Enter the master password: ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)

# Main loop where user chooses to add or view passwords
while True:
    mode = input("Would you like to add a new password or view existing ones (view, add)? ")

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        quit = input("Would you like to quit? (y/n) ")
        if quit.lower() == "y":
            break

