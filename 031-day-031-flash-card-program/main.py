from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# ---Change words --- #
def change_words():
    random_word = data_dict[random.randint(0, len(data_dict) - 1)]["French"]
    canvas.itemconfig(word_text, text=random_word)


# ---Data--- #
with open("./data/french_words.csv") as file:
    data = pandas.read_csv(file)
    data_dict = data.to_dict(orient="records")

# ----UI---- #
window = Tk()
window.title("Flash Card Language Learner")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Canvas
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas.create_image(400, 263, image=card_front_img)
canvas.grid(column=1, row=1, columnspan=2)
language_text = canvas.create_text(
    400, 150, text="Title", fill="black", font=("Ariel", 40, "italic")
)
word_text = canvas.create_text(
    400, 263, text="Word", fill="black", font=("Ariel", 60, "bold")
)

# Buttons
right_img = PhotoImage(file="./images/right.png")
wrong_img = PhotoImage(file="./images/wrong.png")

right_btn = Button(image=right_img, highlightthickness=0, command=change_words)
right_btn.grid(column=1, row=2)

wrong_btn = Button(image=wrong_img, highlightthickness=0, command=change_words)
wrong_btn.grid(column=2, row=2)

change_words()
window.mainloop()
