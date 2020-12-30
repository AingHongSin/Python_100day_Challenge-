from tkinter import *


def Calculator():
    result = round(int(Mile_input.get()) * 1.609)
    
    lbl_result.config(text = result)



window = Tk()
window.title("Mile to Kilometer Converter")

Mile_input = Entry()
Mile_input.grid(row = 0, column = 1)

lbl_mile = Label(text = 'Miles')
lbl_mile.grid(row = 0, column = 2)

lbl_equal = Label(text = 'is equal to ')
lbl_equal.grid(row = 1, column = 0)

lbl_result = Label(text = '0')
lbl_result.grid(row = 1, column = 1)

lbl_km = Label(text = 'Km')
lbl_km.grid(row = 1, column = 2)

btn_Calculate = Button(text = 'Calculate', command = Calculator)
btn_Calculate.grid(row = 2, column = 1)
