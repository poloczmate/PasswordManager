import mysql.connector
from encrypt import encrypt
from encrypt import decrypt
from secret import get_secret_key
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
    record_to_insert = (encrypt(email,get_secret_key()), encrypt(password,get_secret_key()), encrypt(username,get_secret_key()), encrypt(appname,get_secret_key()))
    mycursor.execute(insert_data, record_to_insert)
    mydb.commit()

def print_all():
    mycursor.execute("SELECT * FROM accounts")
    print("E-mail address" + "\t" + "Password" + "\t" + "Username" + "\t" + "Application name")
    for r in mycursor:
        print(decrypt(r[0], get_secret_key()) + "\t" + decrypt(r[1], get_secret_key()) + "\t" + decrypt(r[2], get_secret_key()) + "\t" + decrypt(r[3], get_secret_key()))

def print_one():
    appname = input("Application name:")
    get_one = "SELECT * FROM accounts WHERE appname = '" + encrypt(appname,get_secret_key()) + "'"
    mycursor.execute(get_one)
    myresult = mycursor.fetchall()
    print("E-mail address" + "\t" + "Password" + "\t" + "Username" + "\t" + "Application name")
    print(decrypt(myresult[0][0], get_secret_key()) + "\t" + decrypt(myresult[0][1], get_secret_key()) + "\t" + decrypt(myresult[0][2], get_secret_key()) + "\t" + decrypt(myresult[0][3], get_secret_key()))