from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.goto(0, 270)
        self.color("white")
        self.write(f"Score: {self.score}", align=ALIGNMENT, move=False, font=FONT)
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(
            f"Score: {self.score}",
            align="center",
            move=False,
            font=("Arial", 24, "normal"),
        )
