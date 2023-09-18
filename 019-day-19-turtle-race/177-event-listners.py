from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards)

screen.exitonclick()


# Function in function. higher order function
def add(n1, n2):
    return n1 + n2


def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(2, 5, add))  # 7
