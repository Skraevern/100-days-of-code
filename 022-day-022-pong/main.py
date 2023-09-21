from turtle import Screen
from paddle import Paddle
import time

game_over = False

screen = Screen()
screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle()
player_paddle.goto(-370, 0)
computer_paddle = Paddle()
computer_paddle.goto(360, 0)

screen.listen()
screen.onkey(key="w", fun=player_paddle.move_up)
screen.onkey(key="s", fun=player_paddle.move_down)


while game_over == False:
    screen.update()
    time.sleep(0.1)
    # computer_paddle.move_up()


screen.exitonclick()
