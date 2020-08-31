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

status = Label(root, text=f'Image 1 of {len(images)}', bd=1, relief=SUNKEN, anchor=E)


back_btn = Button(root, text='<<', command=lambda: img_back(current_img_index, images, image_label, status))
exit_btn = Button(root, text='Exit', command=root.quit)
forward_btn = Button(root, text='>>', command=lambda: img_forward(current_img_index, images, image_label, status))

back_btn.grid(row=1, column=0)
exit_btn.grid(row=1, column=1)
forward_btn.grid(row=1, column=2)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)


def img_forward(index, imgs, label, status):
    index[0] = index[0] + 1 if index[0] < len(imgs) - 1 else 0
    label['image'] = imgs[index[0]]
    status['text'] = f'Image {index[0] + 1} of {len(imgs)}'


def img_back(index, imgs, label, status):
    index[0] = index[0] - 1 if index[0] > 0 else len(imgs) - 1
    label['image'] = imgs[index[0]]
    status['text'] = f'Image {index[0] + 1} of {len(imgs)}'


root.mainloop()
