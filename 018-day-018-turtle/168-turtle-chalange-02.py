import turtle

jimmy = turtle.Turtle()

for i in range(15):
    jimmy.forward(10)
    jimmy.penup()
    jimmy.forward(10)
    jimmy.pendown()


screen = turtle.Screen()
screen.exitonclick()
