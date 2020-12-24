from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape('circle')
        self.penup()
        self.speed('fastest')
        self.shapesize(0.5,0.5)
        self.color('blue')
        self.refrash()

    def refrash(self):
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
