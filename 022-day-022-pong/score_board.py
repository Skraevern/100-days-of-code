from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.player_score = 0
        self.computer_score = 0
        self.update_score_board()

    def update_score_board(self):
        self.clear()
        self.goto(-100, 230)
        self.write(self.player_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 230)
        self.write(self.computer_score, align="center", font=("Courier", 50, "normal"))

    def increase_player_score(self):
        self.player_score += 1
        self.update_score_board()

    def increase_computer_score(self):
        self.computer_score += 1
        self.update_score_board()
