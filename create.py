import mysql.connector

import encrypt

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="qwerasdf00",
    database="PasswordManager"
)

mycursor = mydb.cursor()

master = "qwerasdf00"
hashed = encrypt.hash_password(master)
print(hashed)




#mycursor.execute("CREATE DATABASE PasswordManager")
#mycursor.execute("SHOW DATABASES")
#for db in mycursor:
#    print(db)

#email, password, username, appname
#mycursor.execute("CREATE TABLE accounts (email VARCHAR(255), password VARCHAR(255), username VARCHAR(255), appname VARCHAR(255))")