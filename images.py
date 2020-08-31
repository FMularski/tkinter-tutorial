from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.ico'))

img = ImageTk.PhotoImage(Image.open('python.png'))
label = Label(image=img)
label.pack()


button_quit = Button(root, text='Exit', command=root.quit)
button_quit.pack()

root.mainloop()
