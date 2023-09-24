import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

WIDTH = 600
HEIGHT = 600
LEFT_WALL = WIDTH * -1 / 2 - 10

score_board = ScoreBoard(WIDTH, HEIGHT)

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)

player = Player()
car_list = []
for i in range(40):
    car = CarManager()
    car_list.append(car)


screen.listen()
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)
screen.onkey(key="Left", fun=player.move_left)
screen.onkey(key="Right", fun=player.move_right)


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in car_list:
        car.move()
        if car.xcor() < LEFT_WALL:
            car.random_xcor()
    if player.ycor() > HEIGHT / 2:
        player.reset_starting_pos()
        for car in car_list:
            car.increase_speed()
        score_board.increase_score()
