from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letter = [random.choice(letters) for row in range(random.randint(8, 10))]
    password_symbole = [random.choice(symbols) for row in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for row in range(random.randint(2, 4))]

    password_list = password_numbers + password_symbole + password_letter
    random.shuffle(password_list)

    password = "".join(password_list)
    password_Input.delete(0, END)
    password_Input.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    if len(web_Input.get()) ==0 or len(password_Input.get()) == '':
        messagebox.showinfo(title = 'Oops', message = 'Please leave any fields empty!')
    else:
        is_ok = messagebox.askokcancel(title = web_Input.get(), message=(f"These are detial entered: "
                                                                         f"\nEmail: {emil_or_Username_Input.get()} \n"
                                                                         f"Password: {password_Input.get()} "
                                                                         f"is it okay to save?"))
        if is_ok:
            with open(file = 'data.txt', mode = 'a') as data:
                data.write(f"{web_Input.get()} | {emil_or_Username_Input.get()} | {password_Input.get()}\n")


            web_Input.delete(0, END)
            password_Input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx = 60, pady = 40)


canvas = Canvas(width = 200, height = 200)
imageVar = PhotoImage(file = 'logo.png')
canvas.create_image(100, 100, image = imageVar)
canvas.grid(row = 0, column = 0, columnspan = 3)

web_lbl = Label(text = 'Website:')
web_lbl.grid(row = 1, column = 0)

web_Input = Entry(width = 35)
web_Input.grid(row = 1, column = 1, columnspan = 2)
web_Input.focus()

Email_or_Username_lbl = Label(text = "Email/Username:")
Email_or_Username_lbl.grid(row = 2, column = 0)

emil_or_Username_Input = Entry(width = 35)
emil_or_Username_Input.grid(row = 2, column = 1, columnspan = 2)
emil_or_Username_Input.insert(END, 'Ainghongsin9999@gmail.com')

password_lbl = Label(text = 'Password:')
password_lbl.grid(row = 3, column = 0)

password_Input = Entry(width = 21 )
password_Input.grid(row = 3, column = 1)

generate_password_btn = Button(text = 'Generate Password', command = password_generator)
generate_password_btn.grid(row = 3, column = 2)

Adding_btn = Button(text = 'Add',width = 36, command = save)
Adding_btn.grid(row = 4, column = 1, columnspan = 2)





window.mainloop()