from tkinter import *
import mysql.connector
from keys_and_passwords import mysql_root_pwd


root = Tk()
root.geometry('400x400')

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd=mysql_root_pwd
)

print(db)

root.mainloop()
