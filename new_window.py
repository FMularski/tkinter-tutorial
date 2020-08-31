from tkinter import *

root = Tk()
root.title('root')

top = Toplevel()
top.title('top')

label = Label(top, text='Hello world')
label.pack()

root.mainloop()