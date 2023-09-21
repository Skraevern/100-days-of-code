from turtle import Screen
from snake import Snake
from food import Food
from score_board import ScoreBoard
import time

NORTH_WALL = 300
SOUTH_WALL = -280
WEST_WALL = -300
EAST_WALL = 280

screen = Screen()
screen.colormode(255)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

score = 0
snake = Snake()
food = Food()
score_board = ScoreBoard()

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

    # Detect collision with wall
    if (
        (snake.head.ycor() > NORTH_WALL)
        or (snake.head.ycor() < SOUTH_WALL)
        or (snake.head.xcor() < WEST_WALL)
        or (snake.head.xcor() > EAST_WALL)
    ):
        score_board.game_over()
        game_over = True

    # Detect collision with tail
    for segment in snake.segment_list[1:]:
        if snake.head.distance(segment) < 10:
            score_board.game_over()
            game_over = True

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.grow_snake()


screen.exitonclick()
