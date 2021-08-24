import os
import dbManager
import encrypt
import secret

unlocked = False

password = ""
while not unlocked:
    password = input("Password:")
    if encrypt.hash_password(password) == secret.get_secret_key():
        unlocked = True
        print("Unlocked!")
    else:
        print("You cant unlock!")

while unlocked:
    print("Choose a option:\n1. Add password\n2. Get password for 1 site\n3. Show all passwords\n4. Exit")
    choose = input("Choose:")
    if choose == "1":
        dbManager.add_password()
    if choose == "2":
        dbManager.print_one()
    if choose == "3":
        dbManager.print_all()
    if choose == "4":
        break
    input("Press enter if you are ready!")
    os.system("clear")
