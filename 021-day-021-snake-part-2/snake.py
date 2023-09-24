from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
NORTH = 90
SOUTH = 270
WEST = 180
EAST = 0
SNAKE_Color = (255, 16, 240)


class Snake:
    def __init__(self) -> None:
        """Creates a three segment snake"""
        self.segment_list = []
        self.create_snake()
        self.head = self.segment_list[0]

    def create_snake(self):
        for i in range(3):
            self.grow_snake()
            self.segment_list[i].goto(STARTING_POSITIONS[i])

    def move(self):
        """Moves snake forward"""
        for i in range(len(self.segment_list) - 1, 0, -1):
            new_x = self.segment_list[i - 1].xcor()
            new_y = self.segment_list[i - 1].ycor()
            self.segment_list[i].goto(new_x, new_y)
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
        segment = Turtle("square")
        segment.penup()
        segment.color(255, 16, 240)
        if self.segment_list:
            segment.goto(self.segment_list[-1].pos())
        self.segment_list.append(segment)

    def reset(self):
        for segments in self.segment_list:
            segments.goto(1000, 1000)  # Moves them off screen
        self.segment_list.clear()
        self.create_snake()
        self.head = self.segment_list[0]
