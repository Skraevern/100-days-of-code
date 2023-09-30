from tkinter import *

MILES_TO_KM_FORMULA = 1.609344

window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)


def calculate():
    km = round(int(user_input.get()) * MILES_TO_KM_FORMULA, 2)
    result_label.config(text=km)


# Column 0
equal_label = Label(text="is equal to")
equal_label.grid(column=0, row=1)

# Column 1
user_input = Entry(width=10)
user_input.insert(END, string="0")
user_input.grid(column=1, row=0)


result_label = Label(text="0")
result_label.grid(column=1, row=1)

calc_button = Button(text="Calculate", command=calculate)
calc_button.grid(column=1, row=2)

# Column 2
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)


window.mainloop()
