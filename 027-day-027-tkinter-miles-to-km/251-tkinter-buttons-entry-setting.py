import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack(side="left")
my_label.pack(side="top")

my_label["text"] = "New Text"
my_label.config(text="New Text Again")


# Buttons
def button_clicked():
    # my_label["text"] = "I got clicked!"
    my_label["text"] = user_input.get()


button = tkinter.Button(text="Click mich", command=button_clicked)
button.pack()


# Entry
user_input = tkinter.Entry(width=10)
user_input.pack()


window.mainloop()
