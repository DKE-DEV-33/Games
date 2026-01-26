def view():
    for line in open("passwords.txt", "r").readlines():
        data = line.rstrip()
        user, password, site = data.split("|")
        print("Website:", site, "| Account:", user, "| Password:", password)

def add():
    name = input("Account Name: ")
    pwd = input("Password: ")
    site = input("Website: ")


    with open("passwords.txt", "a") as f:
        f.write(name + "|" + pwd + "|" + site + "\n")

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

