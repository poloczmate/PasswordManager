import os
import mysql.connector

#Credentials
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerasdf00",
    database="PasswordManager"
)
mycursor = mydb.cursor()
insert_data = "INSERT INTO accounts (email, password, username, appname) VALUES (%s, %s, %s, %s)"

def add_password():
    email = input("E-mail:")
    password = input("Password:")
    username = input("Username:")
    appname = input("Application name:")
    record_to_insert = (email, password, username, appname)
    mycursor.execute(insert_data, record_to_insert)
    mydb.commit()

def print_all():
    mycursor.execute("SELECT * FROM accounts")
    print("E-mail address" + "\t" + "Password" + "\t" + "Username" + "\t" + "Application name")
    for r in mycursor:
        print(r[0] + "\t" + r[1] + "\t" + r[2] + "\t" + r[3])

def print_one():
    appname = input("Application name:")
    get_one = "SELECT * FROM accounts WHERE appname = '" + appname + "'"
    mycursor.execute(get_one)
    myresult = mycursor.fetchall()
    print("E-mail address" + "\t" + "Password" + "\t" + "Username" + "\t" + "Application name")
    print(myresult[0][0] + "\t" + myresult[0][1] + "\t" + myresult[0][2] + "\t" + myresult[0][3])


while True:
    print("Choose a option:\n1. Add password\n2. Get password for 1 site\n3. Show all passwords\n4. Exit")
    choose = input("Choose:")
    if choose == "1":
        add_password()
    if choose == "2":
        print_one()
    if choose == "3":
        print_all()
    if choose == "4":
        break
    input("Press enter if you are ready!")
    os.system("clear")
