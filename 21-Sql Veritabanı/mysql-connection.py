import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user = "root",
    password = "q123",
    database = 'mydatabase'
   )

mycursor = mydb.cursor()

# mycursor.execute('create database mydatabase')

# mycursor.execute('show databases')

# for x in mycursor:
#     print(x)

# print(mydb)

mycursor.execute('create table customers(name VARCHAR(255),address VARCHAR(255))')