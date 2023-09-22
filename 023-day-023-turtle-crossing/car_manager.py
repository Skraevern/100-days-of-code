from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.speed("fastest")
        self.setheading(180)
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(random.randint(-280, 280), random.randint(-260, 290))
        self.random_min = 3
        self.random_max = 6
        self.move_distance = random.randint(self.random_min, self.random_max)

    def move(self):
        self.forward(self.move_distance)

    def random_xcor(self):
        self.goto(random.randint(310, 400), random.randint(-260, 290))
        self.move_distance = random.randint(self.random_min, self.random_max)
