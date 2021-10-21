from tkinter import *
from tkinter import messagebox
import random
import pyperclip  #library that make copy automatically to your care memmory

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    # Password Generator Project

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_numbers = [random.choice(numbers) for _ in range(random.randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    input_password.delete(0, "end")
    input_password.insert(0, f"{password}")
    pyperclip.copy(password) #make copy automatically to your cache memory



# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(input_website.get()) == 0 or len(input_password.get()) == 0 or len(input_email_username.get()) == 0:
        messagebox.askokcancel(title="Oops", message=f"Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=input_website.get(), message=f"These are details entered: \nEmail: "
                                                                  f"{input_email_username.get()}\nPassword: {input_password.get()}"
                                                                  f"\nIs it ok to save?")
        if is_ok:
            file = open("data.txt", "a")
            file.write(f"{input_website.get()} | {input_email_username.get()} | {input_password.get()} \n")
            file.close()

            input_website.delete(0,"end")
            # input_email_username.delete(0, "end")
            input_password.delete(0, "end")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Generator")
# window.minsize(height=220,  width=220)
window.config(padx=40, pady=25)

canvas = Canvas(width=200, height=200, )
ImageMyPass = PhotoImage(file="logo.png")
canvas.create_image(80, 100, image=ImageMyPass)
canvas.grid(column=1, row=0)

Label_Website = Label(text="Website:", font=("Arial",10, "normal"), )
Label_Website.grid(column=0, row=1, sticky="N")
Label_Email_Username = Label(text="Email/Username:", font=("Arial",10, "normal"))
Label_Email_Username.grid(column=0, row=2)
Label_Password = Label(text="Password:", font=("Arial",10, "normal"))
Label_Password.grid(column=0, row=3)

input_website = Entry(width=43)
input_website.grid(column=1, row=1, columnspan=2, sticky="W")
input_website.focus() #Allows to write after the window appear
input_email_username = Entry(width=43)
input_email_username.grid(column=1, row=2, columnspan=2, sticky="W")
input_email_username.insert(0,"testemail1998123@gmail.com") #Default value
input_password = Entry(width=21)
input_password.grid(column=1, row=3, sticky="W")

button_generate = Button(text="Generate Password", font=("Arial", 9, "normal"), width=16, command=password_generator)
button_generate.grid(column=1, row=3, columnspan=2, sticky="E")
button_add = Button(text="Add", font=("Arial", 9, "normal"), width=36, command=save)
button_add.grid(column=1, row=4, columnspan=2, sticky="w")


window.mainloop()

