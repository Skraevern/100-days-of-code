import turtle
import random


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    random_tuple = (r, g, b)
    return random_tuple


def draw(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        jimmy.pencolor((random_color()))
        jimmy.circle(100)
        current_heading = jimmy.heading()
        jimmy.setheading(current_heading + size_of_gap)


screen = turtle.Screen()
screen.colormode(255)

jimmy = turtle.Turtle()
jimmy.speed(0)


draw(1)
screen.exitonclick()
