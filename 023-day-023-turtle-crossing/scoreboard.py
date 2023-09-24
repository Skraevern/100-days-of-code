from turtle import Turtle

FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self, width, height) -> None:
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.screen_with = width
        self.screen_height = height
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(self.screen_with / 2 - 80, self.screen_height / 2 * -1 + 10)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score_board()
