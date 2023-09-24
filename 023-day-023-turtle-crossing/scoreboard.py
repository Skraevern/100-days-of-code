from turtle import Turtle

FONT = ("Courier", 24, "normal")
FONT_LARGE = ("Courier", 50, "normal")


class ScoreBoard(Turtle):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.goto(width / 2 - 80, height / 2 * -1 + 10)
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"Game over! Score: {self.score}", align="center", font=FONT_LARGE)
