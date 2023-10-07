from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = "Arial"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

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
            150,
            125,
            width=280,
            text="Question",
            fill="black",
            font=(FONT, 20, "italic"),
        )

        self.true_img = PhotoImage(file="./images/true.png")
        self.true_btn = Button(
            image=self.true_img, highlightthickness=0, command=self.true_btn_press
        )
        self.true_btn.grid(column=1, row=3, padx=20, pady=20)

        # Column 2
        self.score_text = Label(
            text="Score: 0/10", bg=THEME_COLOR, fg="white", font=(FONT, 15, "normal")
        )
        self.score_text.grid(column=2, row=1, padx=20, pady=20)

        self.false_img = PhotoImage(file="./images/false.png")
        self.false_btn = Button(
            image=self.false_img, highlightthickness=0, command=self.false_btn_press
        )
        self.false_btn.grid(column=2, row=3, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_info = self.quiz.next_question()
            self.category_text.config(text=q_info["category"])
            self.canvas.itemconfig(
                self.question_text, text=f'Q.{q_info["nr"]}: {q_info["text"]}'
            )
        else:
            self.canvas.itemconfig(
                self.question_text,
                text=f"You've reached the end of the quiz.\n"
                f"You answered correct on {self.quiz.score} of 10 questions",
            )
            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def true_btn_press(self):
        self.answer_feedback(self.quiz.check_answer("True"))

    def false_btn_press(self):
        self.answer_feedback(self.quiz.check_answer("False"))

    def answer_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.score_text.config(text=f"Score: {self.quiz.score}/10")
        self.window.after(1500, func=self.get_next_question)
