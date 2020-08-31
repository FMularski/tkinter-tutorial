from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.ico'))

frame = LabelFrame(root, text='This is a frame', padx=50, pady=50)
frame.pack(padx=10, pady=10)

btn = Button(frame, text='Click')
btn.grid(row=0, column=0)

btn2 = Button(frame, text='Click')
btn2.grid(row=1, column=1)

# widgets can use grid inside of a 

root.mainloop()
