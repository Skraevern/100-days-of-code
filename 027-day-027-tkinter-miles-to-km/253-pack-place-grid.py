from tkinter import *


def button_clicked():
    print("I got clicked")
    if user_input.get() != "":
        new_text = user_input.get()
        my_label.config(text=new_text)


window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label
my_label = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_label.config(text="New Text")
# my_label.place(x=100, y=0)
my_label.config(padx=30, pady=30)
my_label.grid(column=0, row=0)

# Button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

new_button = Button(text="Click Me", command=button_clicked)
new_button.grid(column=2, row=0)

# Entry
user_input = Entry(width=10)
print(user_input.get())
user_input.grid(column=3, row=3)

window.mainloop()
