from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def appending(item, nr_item):
    for i in range(nr_item):
        password_table.append(random.choice(item))

password_table = []


def random_password():
    global password_table
    password_input.delete(0, END)
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    appending(letters, nr_letters)
    appending(symbols, nr_symbols)
    appending(numbers, nr_numbers)

    random.shuffle(password_table)
    password = ''.join(password_table)
    password_input.insert(END, password)
    pyperclip.copy(password)
    password_table = []


# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
    website = website_input.get()
    eu = eu_input.get()
    password = password_input.get()
    record = f"{website} | {eu} | {password}\n"

    confirmation = False
    if password and website:
        confirmation = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {eu}\n"
                                                                     f"Password: {password}\nIs it ok to save?")
    else:
        messagebox.showinfo(title="Error", message="You have to fill the gaps")

    if confirmation:
        with open("data.txt", "a") as file:
            file.write(record)
            password_input.delete(0, END)
            website_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# --- Canvas
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# --- Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()

eu_label = Label(text="Email/Username:", anchor="w")
eu_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# --- inputs

website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2, sticky="w", padx=5, pady=5)

eu_input = Entry(width=52)
eu_input.grid(column=1, row=2, columnspan=2, sticky="w", padx=5, pady=5)
eu_input.insert(END, "mail.bozecki@gmail.com")

password_input = Entry()
password_input.grid(column=1, row=3, sticky="ew", padx=5, pady=5)

# -- buttons

generate_button = Button(width=14, text="Generate Password", command=random_password)
generate_button.grid(column=2, row=3, sticky="w")

add_button = Button(text="Add", command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky="ew", padx=5, pady=5)

window.mainloop()
