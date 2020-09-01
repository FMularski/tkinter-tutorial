from tkinter import *
import mysql.connector
from keys_and_passwords import mysql_root_pwd


root = Tk()
root.geometry('400x400')

# create the connection
db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=mysql_root_pwd,
    database='mydatabase'
)

# create a cursor
cursor = db.cursor()

# create database (once)
# cursor.execute('CREATE DATABASE mydatabase')

# test if db exists - display all databases
cursor.execute('SHOW DATABASES')
for database in cursor:
    print(database)

# create a table
# cursor.execute("""
#     CREATE TABLE customers(
#     first_name VARCHAR(255),
#     last_name VARCHAR(255),
#     zipcode INT(10),
#     price_paid DECIMAL(10, 2),
#     customer_id INT AUTO_INCREMENT PRIMARY KEY)
# """)

# show tables
cursor.execute('SELECT * FROM customers')
print(cursor.description)

root.mainloop()
