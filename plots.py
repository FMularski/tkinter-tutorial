from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.geometry('400x200')


def graph():
    house_prices = np.random.normal(200_000, 25_000, 5000)
    plt.hist(house_prices, bins=50)
    plt.show()


btn = Button(root, text='Graph', command=graph)
btn.pack()

root.mainloop()
