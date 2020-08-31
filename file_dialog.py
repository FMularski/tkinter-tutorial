from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()


def open_file():
    global img
    filename = filedialog.askopenfilename(initialdir='./', title='Select a file',
                                          filetypes=(('png files', '*.png'), ('all files', '*')))
    file_path_label = Label(root, text=filename).pack()
    img = ImageTk.PhotoImage(Image.open(filename))
    img_label = Label(image=img)
    img_label.pack()


open_file_btn = Button(root, text='Open file', command=open_file)
open_file_btn.pack()

root.mainloop()
