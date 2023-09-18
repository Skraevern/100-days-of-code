import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

jimmy = turtle.Turtle()

sides = 3

while sides != 10:
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    jimmy.pencolor((r, g, b))

    for i in range(sides):
        angle = 360 / sides
        jimmy.forward(100)
        jimmy.right(angle)
    sides += 1


screen.exitonclick()
