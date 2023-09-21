from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.color("white")
        self.write("Game over!", font=("Courier", 40, "normal"), align=ALIGNMENT)
