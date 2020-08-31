from tkinter import *
import sqlite3


root = Tk()

# create connection
conn = sqlite3.connect('address_book.db')

# create cursor
cur = conn.cursor()

# create table
cur.execute(
    """
    CREATE TABLE addresses(
    first_name text,
    last_name text,
    address text,
    city text,
    state text,
    zipcode integer
    )
    """
)

# commit changes
conn.commit()

# close connection
conn.close()

root.mainloop()
