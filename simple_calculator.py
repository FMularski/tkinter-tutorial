from tkinter import *


root = Tk()
root.title('Simple Calculator')

label = Label(root, width=32, borderwidth=5, justify=LEFT)
label.grid(row=0, column=0, columnspan=4)   # spans columns 1, 2, 3, 4 in the first row


def add_char(char):
    label['text'] += str(char)


def clear():
    label['text'] = ''


def calculate():
    if '+' in label['text']:
        result = 0
        values = label['text'].split('+')
        for value in values:
            result += int(value)
            label['text'] = str(result)

    elif '-' in label['text']:
        values = label['text'].split('-')
        result = int(values[0])
        for value in values[1:]:
            result -= int(value)
            label['text'] = str(result)

    elif '*' in label['text']:
        result = 1
        values = label['text'].split('*')
        for value in values:
            result *= int(value)
            label['text'] = str(result)

    elif '/' in label['text']:
        values = label['text'].split('/')
        result = int(values[0])
        for value in values[1:]:
            try:
                result /= float(value)
                label['text'] = str(int(result))
            except ZeroDivisionError:
                label['text'] = 'Error: Divided by 0'


# creating and placing digit buttons
digit_buttons = [Button(root, text=str(i), padx=30, pady=10, command=lambda num=i: add_char(num)) for i in range(10)]

digit_buttons[0].grid(row=4, column=0)
digit_buttons[1].grid(row=3, column=0)
digit_buttons[2].grid(row=3, column=1)
digit_buttons[3].grid(row=3, column=2)
digit_buttons[4].grid(row=2, column=0)
digit_buttons[5].grid(row=2, column=1)
digit_buttons[6].grid(row=2, column=2)
digit_buttons[7].grid(row=1, column=0)
digit_buttons[8].grid(row=1, column=1)
digit_buttons[9].grid(row=1, column=2)


# creating and placing operation buttons
operation_buttons = {
    'add': Button(root, text='+', padx=30, pady=10, command=lambda: add_char('+')),
    'sub': Button(root, text='-', padx=30, pady=10, command=lambda: add_char('-')),
    'mul': Button(root, text='*', padx=30, pady=10, command=lambda: add_char('*')),
    'div': Button(root, text='/', padx=30, pady=10, command=lambda: add_char('/'))
}

operation_buttons['add'].grid(row=4, column=4)
operation_buttons['sub'].grid(row=3, column=4)
operation_buttons['mul'].grid(row=2, column=4)
operation_buttons['div'].grid(row=1, column=4)


# creating and placing clear and equals buttons
equals_button = Button(root, text='=', padx=30, pady=10, command=calculate)
clear_button = Button(root, text='C', padx=30, pady=10, command=clear)

equals_button.grid(row=4, column=2)
clear_button.grid(row=4, column=1)

root.mainloop()
