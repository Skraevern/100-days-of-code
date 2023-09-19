from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self) -> None:
        """Creates a three segment snake"""
        self.segment_list = []
        self.create_snake()

    def create_snake(self):
        for i in range(3):
            self.segment = Turtle("square")
            self.segment.penup()
            self.segment.color("white")
            self.segment.goto(STARTING_POSITIONS[i])
            self.segment_list.append(self.segment)

    def move(self):
        """Moves snake forward"""
        for i in range(len(self.segment_list) - 1, 0, -1):
            self.new_x = self.segment_list[i - 1].xcor()
            self.new_y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(self.new_x, self.new_y)
        self.segment_list[0].forward(MOVE_DISTANCE)

    def turn_north(self):
        self.segment_list[0].setheading(90)

    def turn_south(self):
        self.segment_list[0].setheading(270)

    def turn_west(self):
        self.segment_list[0].setheading(180)

    def turn_east(self):
        self.segment_list[0].setheading(0)
