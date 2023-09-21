from turtle import Turtle
import random

NORTH = 90
SOUTH = 270
SPEED = 30
COMPUTER_SPEED = 10
RANDOM_HEADING = [NORTH, SOUTH]


class Paddle(Turtle):
    def __init__(self, coordinates) -> None:
        super().__init__()
        self.create_paddle()
        self.goto(coordinates)
        self.random_heading = ""

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

    def reset_pos(self, coordinates):
        self.goto(coordinates)

    def computer_move(self, ball_y, ball_x, difficulty):
        if ball_x > difficulty:
            self.random_heading = ""
            if ball_y > self.ycor():
                self.setheading(NORTH)
                self.forward(COMPUTER_SPEED)
            else:
                self.setheading(SOUTH)
                self.forward(COMPUTER_SPEED)
        else:
            if self.random_heading:
                if self.ycor() > 250 or self.ycor() < -250:
                    pass
                else:
                    self.forward(COMPUTER_SPEED)

            else:
                self.random_heading = random.choice(RANDOM_HEADING)
