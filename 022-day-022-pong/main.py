from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

NORTH_WALL = 280
SOUTH_WALL = -280
EAST_WALL = 380
WEST_WALL = -380
DIFFICULTY_LIST = [0, 50, 100, 150, 200]  # hard - easy

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
screen.onkey(key="Up", fun=computer_paddle.move_up)
screen.onkey(key="s", fun=player_paddle.move_down)
screen.onkey(key="Down", fun=computer_paddle.move_down)


while game_over == False:
    time.sleep(0.05)
    screen.update()
    ball.move()
    computer_paddle.computer_move(ball.ycor(), ball.xcor(), DIFFICULTY_LIST[4])

    # Detect collision with wall
    if (ball.ycor() > NORTH_WALL) or (ball.ycor() < SOUTH_WALL):
        ball.bounce_wall()

    # Detect collision with paddle
    if (ball.distance(computer_paddle) < 50 and ball.xcor() > 340) or (
        ball.distance(player_paddle) < 50 and ball.xcor() < -350
    ):
        ball.bounce_paddle()

    # Detect collision with back walls
    if (ball.xcor() > EAST_WALL) or (ball.xcor() < WEST_WALL):
        ball.bounce_paddle()


screen.exitonclick()
