from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_score = int(file.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"SCORE: {self.score} HIGH SCORE: {self.high_score}",
            font=FONT,
            align=ALIGNMENT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("high_score.txt", mode="w") as file:
                file.write(f"{self.high_score}")

        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.clear()
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.write("GAME OVER", font=("Courier", 40, "normal"), align=ALIGNMENT)
