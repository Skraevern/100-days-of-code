import turtle
import random

screen = turtle.Screen()
screen.colormode(255)

jimmy = turtle.Turtle()
jimmy.pensize(10)
jimmy.speed(10)

direction_list = [0, 90, 180, 270]

for i in range(200):
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    jimmy.pencolor((r, g, b))

    jimmy.forward(20)
    jimmy.setheading(random.choice(direction_list))

screen.exitonclick()
