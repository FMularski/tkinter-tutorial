from tkinter import *
from tkinter import messagebox

root = Tk()


# showinfo, showwarning, showerror, askquestion, askokcancel, askyesno

def popup():
    response = messagebox.askokcancel(title='This is a title', message='Hello world')
    print(response)


Button(root, text='Popup', command=popup).pack()

root.mainloop()
