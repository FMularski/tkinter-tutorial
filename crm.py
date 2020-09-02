from tkinter import *
import mysql.connector
from keys_and_passwords import mysql_root_pwd


root = Tk()
root.geometry('400x600')

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
cursor.execute("""
    CREATE TABLE IF NOT EXISTS customers(
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    zipcode INT(10),
    price_paid DECIMAL(10, 2),
    customer_id INT AUTO_INCREMENT PRIMARY KEY)
""")

# alter table
# cursor.execute('''
#     ALTER TABLE customers ADD (
#     email VARCHAR(255),
#     address1 VARCHAR(255),
#     address2 VARCHAR(255),
#     city VARCHAR(50),
#     state VARCHAR(50),
#     country VARCHAR(255),
#     phone VARCHAR(255),
#     payment_method VARCHAR(50),
#     discount_code VARCHAR(255)
#     )''')


# show tables
# cursor.execute('SELECT * FROM customers')
# print(cursor.description)

# title label
title_label = Label(root, text='Customer Database', font=('Helvetica', 16))
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# form for customer data
# labels
first_name_label = Label(root, text='First Name:').grid(row=1, column=0, sticky=W, padx=10)
last_name_label = Label(root, text='Last Name:').grid(row=2, column=0, sticky=W, padx=10)
address1_label = Label(root, text='Address 1:').grid(row=3, column=0, sticky=W, padx=10)
address2_label = Label(root, text='Address 2:').grid(row=4, column=0, sticky=W, padx=10)
city_label = Label(root, text='City:').grid(row=5, column=0, sticky=W, padx=10)
state_label = Label(root, text='State:').grid(row=6, column=0, sticky=W, padx=10)
zipcode_label = Label(root, text='Zipcode:').grid(row=7, column=0, sticky=W, padx=10)
country_label = Label(root, text='Country:').grid(row=8, column=0, sticky=W, padx=10)
phone_label = Label(root, text='Phone:').grid(row=9, column=0, sticky=W, padx=10)
email_label = Label(root, text='Email:').grid(row=10, column=0, sticky=W, padx=10)
payment_method_label = Label(root, text='Payment method:').grid(row=11, column=0, sticky=W, padx=10)
discount_code_label = Label(root, text='Discount code:').grid(row=12, column=0, sticky=W, padx=10)
price_paid_label = Label(root, text='Price paid:').grid(row=13, column=0, sticky=W, padx=10)

# entries
first_name_entry = Entry(root)
first_name_entry.grid(row=1, column=1)

last_name_entry = Entry(root)
last_name_entry.grid(row=2, column=1, pady=5)

address1_entry = Entry(root)
address1_entry.grid(row=3, column=1, pady=5)

address2_entry = Entry(root)
address2_entry.grid(row=4, column=1, pady=5)

city_entry = Entry(root)
city_entry.grid(row=5, column=1, pady=5)

state_entry = Entry(root)
state_entry.grid(row=6, column=1, pady=5)

zipcode_entry = Entry(root)
zipcode_entry.grid(row=7, column=1, pady=5)

country_entry = Entry(root)
country_entry.grid(row=8, column=1, pady=5)

phone_entry = Entry(root)
phone_entry.grid(row=9, column=1, pady=5)

email_entry = Entry(root)
email_entry.grid(row=10, column=1, pady=5)

payment_method_entry = Entry(root)
payment_method_entry.grid(row=11, column=1, pady=5)

discount_code_entry = Entry(root)
discount_code_entry.grid(row=12, column=1, pady=5)

price_paid_entry = Entry(root)
price_paid_entry.grid(row=13, column=1, pady=5)

add_button = Button(root, text='Add', width=10, command=None)
add_button.grid(row=14, column=0, pady=(15, 0))


def clear():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    address1_entry.delete(0, END)
    address2_entry.delete(0, END)
    city_entry.delete(0, END)
    state_entry.delete(0, END)
    zipcode_entry.delete(0, END)
    country_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    payment_method_entry.delete(0, END)
    discount_code_entry.delete(0, END)
    price_paid_entry.delete(0, END)


def add_customer():
    sql_command = 'INSERT INTO customers (first_name, last_name, address1, address2, city, state, zipcode,' \
                  'country, phone, email, payment_method, discount_code, price_paid) ' \
                  'VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'
    values = (first_name_entry.get(), last_name_entry.get(), address1_entry.get(), address2_entry.get(),
              city_entry.get(), state_entry.get(), zipcode_entry.get(), country_entry.get(),
              phone_entry.get(), email_entry.get(), payment_method_entry.get(),
              discount_code_entry.get(), price_paid_entry.get())

    cursor.execute(sql_command, values)
    db.commit()
    clear()


add_button = Button(root, text='Add', width=10, command=add_customer)
add_button.grid(row=14, column=0, pady=(15, 0))


clear_button = Button(root, text='Clear', width=10, command=clear)
clear_button.grid(row=14, column=1, pady=(15, 0))

cursor.execute('SELECT * FROM customers')
result = cursor.fetchall()
for record in result:
    print(record)

root.mainloop()
