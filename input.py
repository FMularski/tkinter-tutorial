from tkinter import *


root = Tk()

entry = Entry(root, width=50, borderwidth=5)
entry.pack()
entry.insert(0, 'Enter your name...')


def show_name():
    label = Label(root, text=entry.get())
    label.pack()


btn = Button(root, text='Enter your name and click me', command=show_name)
btn.pack()

root.mainloop()
