from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = [3, 6]
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(random.randint(-280, 280), random.randint(-250, 290))
        self.random_min = STARTING_MOVE_DISTANCE[0]
        self.random_max = STARTING_MOVE_DISTANCE[1]
        self.set_move_speed()

    def move(self):
        self.forward(self.move_distance)

    def random_xcor(self):
        self.goto(random.randint(310, 400), random.randint(-250, 290))
        self.set_move_speed()

    def set_move_speed(self):
        self.move_distance = random.randint(self.random_min, self.random_max)

    def increase_speed(self):
        self.random_min += MOVE_INCREMENT
        self.random_max += MOVE_INCREMENT
        self.set_move_speed()
