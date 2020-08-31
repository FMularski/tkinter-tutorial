from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.tk.call('wm', 'iconphoto', root._w, PhotoImage(file='icon.ico'))

variable = StringVar()
variable.set('value')


def click_radio(value):
    Label(root, text=value).pack()


# Radiobutton(root, text='Option A', variable=variable, value='A', command=lambda: click_radio(variable.get())).pack()
# Radiobutton(root, text='Option B', variable=variable, value='B', command=lambda: click_radio(variable.get())).pack()

radio_buttons = [Radiobutton(root, text=f'Option {i + 1}', variable=variable, value=str(i + 1),
                             command=lambda i=i: click_radio(i)) for i in range(10)]

for btn in radio_buttons:
    btn.pack()


label = Label(root, text=variable.get())
label.pack()

root.mainloop()
