from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.geometry('400x400')

var = IntVar()

label = Label(root, text=var.get())
label.pack()

checkbox = Checkbutton(root, text='Accept the terms', variable=var, onvalue=100, offvalue=-100)
checkbox.pack()


def update():
    label['text'] = var.get()


update_btn = Button(root, text='Update', command=update)
update_btn.pack()


root.mainloop()
