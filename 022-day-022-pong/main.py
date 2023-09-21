from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

NORTH_WALL = 280
SOUTH_WALL = -280

game_over = False

screen = Screen()
screen = Screen()
screen.colormode(255)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle((-370, 0))
computer_paddle = Paddle((360, 0))

ball = Ball()

screen.listen()
screen.onkey(key="w", fun=player_paddle.move_up)
screen.onkey(key="Up", fun=player_paddle.move_up)
screen.onkey(key="s", fun=player_paddle.move_down)
screen.onkey(key="Down", fun=player_paddle.move_down)


while game_over == False:
    screen.update()
    ball.move()
    # computer_paddle.move_up()


screen.exitonclick()
