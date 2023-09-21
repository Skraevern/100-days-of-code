from turtle import Turtle

SPEED = 4


class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("fastest")

    def move(self):
        x_cor = self.xcor() + SPEED
        y_cor = self.ycor() + SPEED
        self.goto(x_cor, y_cor)
