from turtle import Turtle

NORTH = 90
SOUTH = 270
SPEED = 30


class Paddle(Turtle):
    def __init__(self, coordinates) -> None:
        super().__init__()
        self.create_paddle()
        self.goto(coordinates)

    def move_up(self):
        self.setheading(NORTH)
        self.forward(SPEED)

    def move_down(self):
        self.setheading(SOUTH)
        self.forward(SPEED)

    def create_paddle(self):
        self.shape("square")
        self.speed("fastest")
        self.setheading(NORTH)
        self.penup()
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
