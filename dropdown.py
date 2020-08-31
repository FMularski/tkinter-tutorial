from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry('400x400')

day = StringVar()
day.set('Pick a day')

dropdown = OptionMenu(root, day, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday')
dropdown.pack()

day_label = Label(root, text='...')
day_label.pack()


def update():
    day_label['text'] = day.get()


update_btn = Button(root, text='Update', command=update)
update_btn.pack()

root.mainloop()
