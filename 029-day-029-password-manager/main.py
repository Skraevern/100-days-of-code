from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# Column 1
website_label = Label(text="Website:")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:")
password_label.grid(column=1, rows=4)

# Column 2
img = PhotoImage(file=("./logo.png"))
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=img)
canvas.grid(column=2, row=1)

website_input = Entry(width=46)
website_input.insert(END, string="")
website_input.grid(column=2, row=2, columnspan=2, sticky="w")

email_input = Entry(width=46)
email_input.insert(END, string="")
email_input.grid(column=2, row=3, columnspan=2, sticky="w")

password_output = Entry(width=25)
password_output.insert(END, string="")
password_output.grid(column=2, row=4, sticky="w")

add_btn = Button(text="Add")
# add_btn.grid(column=2, row=5)

# Column 3
gen_psw_btn = Button(text="Generate Password")
gen_psw_btn.grid(column=3, row=4)

window.mainloop()
