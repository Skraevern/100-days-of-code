from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_right():
    tim.right(10)


def turn_left():
    tim.left(10)


def clear():
    tim.home()
    tim.clear()


screen.listen()
screen.onkey(fun=move_forwards, key="w")
screen.onkey(fun=move_backwards, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key="c")

screen.exitonclick()


# Function in function. higher order function
def add(n1, n2):
    return n1 + n2


def calculator(n1, n2, func):
    return func(n1, n2)


print(calculator(2, 5, add))  # 7
