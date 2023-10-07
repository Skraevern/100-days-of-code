from tkinter import *

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self) -> None:
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # Column 1
        self.category_text = Label(
            text="Category", bg=THEME_COLOR, fg="white", font=(FONT, 15, "normal")
        )
        self.category_text.grid(column=1, row=1, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(column=1, row=2, columnspan=2, padx=20, pady=20)
        self.question_text = self.canvas.create_text(
            150, 125, text="Question", fill="black", font=(FONT, 20, "italic")
        )

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(image=self.true_img, highlightthickness=0)
        self.true_btn.grid(column=1, row=3, padx=20, pady=20)

        # Column 2
        self.score_text = Label(
            text="Score: 0", bg=THEME_COLOR, fg="white", font=(FONT, 15, "normal")
        )
        self.score_text.grid(column=2, row=1, padx=20, pady=20)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(image=self.false_img, highlightthickness=0)
        self.false_btn.grid(column=2, row=3, padx=20, pady=20)

        self.window.mainloop()
