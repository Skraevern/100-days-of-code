from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_starting_pos()
        self.setheading(90)
        self.x_cor = 0
        self.y_cor = 0

    def update_coordinates(self):
        self.x_cor = self.xcor()
        self.y_cor = self.ycor()

    def move_up(self):
        self.update_coordinates()
        self.goto(self.x_cor, self.y_cor + MOVE_DISTANCE)

    def move_down(self):
        self.update_coordinates()
        self.goto(self.x_cor, self.y_cor - MOVE_DISTANCE)

    def move_left(self):
        self.update_coordinates()
        self.goto(self.x_cor - MOVE_DISTANCE, self.y_cor)

    def move_right(self):
        self.update_coordinates()
        self.goto(self.x_cor + MOVE_DISTANCE, self.y_cor)

    def reset_starting_pos(self):
        self.goto(STARTING_POSITION)
