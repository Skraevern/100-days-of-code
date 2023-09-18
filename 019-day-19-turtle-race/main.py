from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race. Enter a color: "
)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-100, -60, -20, 20, 60, 100]
all_turtles = []

for i in range(0, len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-240, y=y_position[i])
    all_turtles.append(turtle)

if user_bet:
    is_is_race_on = True

while is_is_race_on:
    for i in range(0, len(all_turtles)):
        if all_turtles[i].xcor() > 210:
            winner = all_turtles[i].pencolor()
            if winner == user_bet:
                print(f"Congratulations. {winner} won!")
            else:
                print(f"Sorry. {winner} won...")
            is_is_race_on = False

        random_dist = random.randint(0, 10)
        all_turtles[i].forward(random_dist)


screen.exitonclick()
