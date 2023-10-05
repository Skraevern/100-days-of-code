from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"


# --- Canvas config --- #
def canvas_config(word, language, image, color):
    canvas.itemconfig(canvas_image, image=image)
    canvas.itemconfig(language_text, text=language, fill=color)
    canvas.itemconfig(word_text, text=word, fill=color)


# --- Flip Card --- #
def flip_card():
    global random_index
    english_word = data_dict[random_index]["English"]
    canvas_config(english_word, "English", card_back_img, "white")


# ---Change words --- #
def change_words():
    global random_index, flip_card_timer
    window.after_cancel(flip_card_timer)
    random_index = random.randint(0, len(data_dict) - 1)
    french_word = data_dict[random_index]["French"]
    canvas_config(french_word, "French", card_front_img, "black")
    flip_card_timer = window.after(3000, func=flip_card)


# ---Data--- #
with open("./data/french_words.csv") as file:
    data = pandas.read_csv(file)
    data_dict = data.to_dict(orient="records")

# ----UI---- #
window = Tk()
window.title("Flash Card Language Learner")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_card_timer = window.after(3000, func=flip_card)

# Canvas
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=card_front_img)
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
