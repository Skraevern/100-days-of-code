from turtle import Turtle

NORTH = 90
SOUTH = 270
SPEED = 30


class Paddle(Turtle):
    def __init__(self) -> None:
        super().__init__()
        # self.paddle = Turtle("square")
        self.shape("square")
        self.speed("fastest")
        self.setheading(NORTH)
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=4, stretch_wid=1)

    def move_up(self):
        self.setheading(NORTH)
        self.forward(SPEED)

    def move_down(self):
        self.setheading(SOUTH)
        self.forward(SPEED)
