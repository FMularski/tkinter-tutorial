from tkinter import *


root = Tk()


def click():
    label = Label(root, text='Clicked!')
    label.pack()


btn = Button(master=root, text='Click', padx=50, pady=25, command=click, fg='yellow', bg='black')
btn.pack()

root.mainloop()
