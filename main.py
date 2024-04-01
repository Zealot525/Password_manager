from tkinter import *
from tkinter import messagebox
import random
import pyperclip

FONT = "Times New Roman"
FONT_SIZE = 10
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)] + \
                    [random.choice(symbols) for char in range(nr_symbols)] + \
                    [random.choice(numbers) for char in range(nr_numbers)]

    random.shuffle(password_list)
    password = "".join(password_list)
    
    if len(password_textbox.get()) > 0:
        password_textbox.delete(0, END)
    password_textbox.insert(END, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website =website_textbox.get()
    email = email_textbox.get()
    password = password_textbox.get()
    if len(website) <= 0 or  len(email) <= 0 or len(password) <= 0:
        messagebox.showerror("ERROR", "Oops! Looks like you left something blank!")
    else:
        proceed = messagebox.askokcancel(website, "Do you want to save the current information?")
        if proceed:
            with open("password.txt", "a") as file:
                file.write(f"{website.title()}| {email} | {password}\n")
            website_textbox.delete(0, END)
            password_textbox.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Generator")
window.config(padx=50, pady=50)

# logo
canvas = Canvas(width=200,height = 200)
lock_image = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_image)
canvas.grid(column=1, row=0)

#  website text
website_label = Label(text="Website:", font=(FONT,FONT_SIZE))
website_label.grid(column=0, row=1)
# email/username text
email_label = Label(text="email/Username:", font=(FONT,FONT_SIZE))
email_label.grid(column=0, row=2)
# password text
password_label = Label(text="Password:", font=(FONT,FONT_SIZE))
password_label.grid(column=0, row=3)



# website textbox 
website_textbox = Entry(width=43, font=(FONT,FONT_SIZE))
website_textbox.focus()
website_textbox.grid(column=1, row=1, columnspan=2)
# email textbox
email_textbox = Entry(width=43, font=(FONT,FONT_SIZE))
email_textbox.insert(0,"@gmail.com")
email_textbox.grid(column=1, row=2, columnspan=2)
# password textbox
password_textbox = Entry(width=25, font=(FONT,FONT_SIZE))
password_textbox.grid(column=1, row=3)


# generate password  button
generate_button = Button(text="Generate Password", font=(FONT,FONT_SIZE), command=generator)
generate_button.grid(column=2, row=3, )
# add button
add_button = Button(text="Add", width=37, font=(FONT,FONT_SIZE), command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
