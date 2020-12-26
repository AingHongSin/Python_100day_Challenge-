from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('turtle')
        self.penup()
        self.start_location()

    def start_location(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)


    def move(self):
        # new_x = self.xcor() + 10
        self.forward(MOVE_DISTANCE)


