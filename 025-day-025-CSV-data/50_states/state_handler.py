from turtle import Turtle


class StateWriter(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.penup()
        self.speed(1)

    def write_state(self, state, x, y):
        self.setheading(self.towards(x, y))
        self.goto(x, y)
        self.write(state)
        self.goto(0, 0)
