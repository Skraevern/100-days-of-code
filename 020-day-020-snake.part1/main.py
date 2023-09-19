from turtle import Turtle, Screen
from snake import Snake
import random
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(key="w", fun=snake.turn_north)
screen.onkey(key="s", fun=snake.turn_south)
screen.onkey(key="a", fun=snake.turn_west)
screen.onkey(key="d", fun=snake.turn_east)


game_over = False
while game_over == False:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # if (
    #     (segment_list[0].xcor() > 280)
    #     or (segment_list[0].xcor() < -300)
    #     or (segment_list[0].ycor() > 280)
    #     or (segment_list[0].ycor() < -300)
    # ):
    #     print("Over!")
    #     game_over = True


screen.exitonclick()
