from turtle import Screen
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

score = 0
snake = Snake()
food = Food()

screen.listen()
screen.onkey(key="w", fun=snake.turn_north)
screen.onkey(key="s", fun=snake.turn_south)
screen.onkey(key="a", fun=snake.turn_west)
screen.onkey(key="d", fun=snake.turn_east)
screen.onkey(key="Up", fun=snake.turn_north)
screen.onkey(key="Down", fun=snake.turn_south)
screen.onkey(key="Left", fun=snake.turn_west)
screen.onkey(key="Right", fun=snake.turn_east)


game_over = False
while game_over == False:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.hideturtle()
        food = Food()
        score += 1
        snake.grow_snake()

screen.exitonclick()
