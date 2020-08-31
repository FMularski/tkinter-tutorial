from tkinter import *
from PIL import ImageTk, Image


root = Tk()

images = [ImageTk.PhotoImage(Image.open(f'img/nature0.png')),
          ImageTk.PhotoImage(Image.open(f'img/nature1.png')),
          ImageTk.PhotoImage(Image.open(f'img/nature2.png')),
          ImageTk.PhotoImage(Image.open(f'img/nature3.png'))]

current_img_index = [0]     # this needs to be a mutable type ( a list, not a int
# to be changed within back/forward function

image_label = Label(root, image=images[current_img_index[0]])
image_label.grid(row=0, column=0, columnspan=3)

back_btn = Button(root, text='<<', command=lambda: img_back(current_img_index, images, image_label))
exit_btn = Button(root, text='Exit', command=root.quit)
forward_btn = Button(root, text='>>', command=lambda: img_forward(current_img_index, images, image_label))

back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2)


def img_forward(index, imgs, label):
    index[0] = index[0] + 1 if index[0] < len(imgs) - 1 else 0
    label['image'] = imgs[index[0]]


def img_back(index, imgs, label):
    index[0] = index[0] - 1 if index[0] > 0 else len(imgs) - 1
    label['image'] = imgs[index[0]]


root.mainloop()
