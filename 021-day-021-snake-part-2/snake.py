from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0


class Snake:
    def __init__(self) -> None:
        """Creates a three segment snake"""
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

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
        self.head.forward(MOVE_DISTANCE)

    def turn_north(self):
        if self.head.heading() != SOUTH:
            self.head.setheading(NORTH)

    def turn_south(self):
        if self.head.heading() != NORTH:
            self.head.setheading(SOUTH)

    def turn_west(self):
        if self.head.heading() != EAST:
            self.head.setheading(WEST)

    def turn_east(self):
        if self.head.heading() != WEST:
            self.head.setheading(EAST)

    def grow_snake(self):
        self.last_segment_pos = self.segment_list[-1].pos()
        self.segment = Turtle("square")
        self.segment.penup()
        self.segment.color("white")
        self.segment.goto(self.last_segment_pos)
        self.segment_list.append(self.segment)
