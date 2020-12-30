from tkinter import *


def display_label():
    label.config(text = input.get())




window = Tk()
window.minsize(500, 300)

my_label = Label(text = 'New Text', font = ('Times News Roman', 24, 'bold'))
my_label.grid(row = 0, column = 0)

my_button1 = Button(text = 'Click Me', command = display_label)
my_button1.grid(row = 1, column = 1)

my_button2 = Button(text = 'Click Me', command = display_label)
my_button2.grid(row = 0, column = 2)

input = Entry(width = 10)
input.grid(row = 2, column = 3)

window.mainloop()