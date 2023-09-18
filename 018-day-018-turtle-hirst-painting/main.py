from colors import color_list
import turtle
import random


def draw(cwidth, cheight, hdots, vdots):
    start_width = 0 - cwidth
    start_height = 0 - cheight
    total_width = cwidth * 2
    total_height = cheight * 2
    jump = total_height / hdots

    jimmy.goto(start_width, start_height)
    for i in range(hdots):
        for i in range(vdots):
            jimmy.dot(10, random.choice(color_list))
            jimmy.forward(total_width / vdots)
            jimmy.dot(10, random.choice(color_list))
        start_height += jump
        jimmy.goto(start_width, start_height)


screen = turtle.Screen()
screen.setup(1500, 800)
screen.colormode(255)

jimmy = turtle.Turtle()
jimmy.speed(0)
jimmy.penup()
jimmy.hideturtle()

draw(cwidth=500, cheight=300, hdots=40, vdots=60)

screen.exitonclick()
