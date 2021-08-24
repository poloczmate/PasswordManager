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
record_to_insert = ("matepolocz@gmail.com", "qwerasdf00", "matepolocz", "apple.com")
mycursor.execute(insert_data,record_to_insert)
#mycursor.execute("SELECT * FROM accounts")
mydb.commit()

for d in mycursor:
    print(d)

while True:
    os.system("clear")
    choose = input("Choose a option:\n1. Add password\n2. Get password\n3. Exit\nChoose:")
    #Statements
    if choose == "3":
        break
