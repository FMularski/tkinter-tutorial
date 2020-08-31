from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()

horizontal = Scale(root, from_=0, to=100, orient=HORIZONTAL)
horizontal.pack()

label = Label(root, text='0')
label.pack()


def update(arg):
    label['text'] = horizontal.get()


horizontal.bind(sequence='<ButtonRelease-1>', func=update)


root.mainloop()
