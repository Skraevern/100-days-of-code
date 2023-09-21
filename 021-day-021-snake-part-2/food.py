from turtle import Turtle
import random

FOOD_COLOR = (111, 209, 3)


class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # 10 * 10
        self.color(FOOD_COLOR)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        random_angle = random.randint(0, 360)
        self.goto(random_x, random_y)
        self.tilt(random_angle)
