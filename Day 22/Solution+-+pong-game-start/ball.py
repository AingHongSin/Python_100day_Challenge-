from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.shape('circle')
        self.color('white')
        self.shapesize(1,1)
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.ball_speed = 0.1

    def move(self):
        self.speed(self.ball_speed)
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bound_y(self):
        self.y_move *= -1

    def bound_x(self):
        self.x_move *= -1
        self.ball_speed *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.bound_x()
        self.ball_speed = 0.1
