from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_psw():
    from importlib import reload
    import generator

    password_output.delete(0, END)
    password_output.insert(END, string=generator.password)
    pyperclip.copy(generator.password)
    reload(generator)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_psw():
    website = website_input.get().lower()
    email = email_input.get().lower()
    password = password_output.get()
    new_data = {website: {"email": email, "password": password}}

    if (len(website) == 0) or (len(email) == 0) or (len(password)) == 0:
        messagebox.showerror(title="Ooops", message="Missing inputs!")
    else:
        is_ok = messagebox.askokcancel(
            title="Password Manager",
            message=f"These are the details entered:\n"
            f"\n"
            f"Website: {website}\n"
            f"\n"
            f"Email/Username: {email}\n"
            f"\n"
            f"Password: {password}\n"
            f"\n"
            f"Is it okay to save?",
        )
        if is_ok:
            try:
                with open("passwords.json", mode="r") as file:
                    # Reading old data
                    data = json.load(file)
                    # Updating old data
                    data.update(new_data)
                with open("passwords.json", mode="w") as file:
                    # Saving updated data
                    json.dump(data, file, indent=4)
            except FileNotFoundError:  # if no file. Write new.
                with open("passwords.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
            finally:
                website_input.delete(0, END)
                password_output.delete(0, END)
                website_input.focus()


# ----------------------------- Search -------------------------------- #
def search():
    website = website_input.get().lower()
    found = False

    if len(website) == 0:
        messagebox.showerror(title="Ooops", message="Missing inputs!")
    else:
        try:
            with open("passwords.json", mode="r") as file:
                data = json.load(file)
                for key, value in data.items():
                    if key == website:
                        found = True
                        username = value["email"]
                        psw = value["password"]
                        messagebox.showinfo(
                            title="Password",
                            message=f'Login for "{key}" is:\n\n'
                            f"Username:\n"
                            f"{username}\n\n"
                            f"Password:\n"
                            f"{psw}",
                        )
                if not found:
                    messagebox.showinfo(
                        title="Password",
                        message=f'Password for "{website}" not found',
                    )
        except:
            messagebox.showinfo(title="Password", message=f"No stored passwords")


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
password_label.grid(column=1, row=4)

# Column 2
img = PhotoImage(file=("./logo.png"))
canvas = Canvas(width=200, height=200)
canvas.create_image(125, 100, image=img)
canvas.grid(column=2, row=1)

website_input = Entry(width=25)
website_input.insert(END, string="")
website_input.grid(column=2, row=2, sticky="w")
website_input.focus()  # Start courser at

email_input = Entry(width=45)
email_input.insert(END, string="standard.email@icloud.com")
email_input.grid(column=2, row=3, columnspan=2, sticky="w")

password_output = Entry(width=25)
password_output.insert(END, string="")
password_output.grid(column=2, row=4, sticky="w")

add_btn = Button(text="Add", width=42, command=save_psw)
add_btn.grid(column=2, row=5, columnspan=2, sticky="w")

# Column 3
search_btn = Button(text="Search", command=search, width=15)
search_btn.grid(column=3, row=2)

gen_psw_btn = Button(text="Generate Password", command=gen_psw, width=15)
gen_psw_btn.grid(column=3, row=4)

window.mainloop()
