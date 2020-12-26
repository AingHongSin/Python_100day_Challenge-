from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):

        self.all_car = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def Car_Generate(self):
        random_Change = random.randint(1,6)
        if random_Change == 1:
            new_car = Turtle()
            new_car.shape('square')
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            new_car.goto(300, y_cor)
            new_car.setheading(180)

            self.all_car.append(new_car)

    def driving(self):
        for car in self.all_car:
            car.forward(self.carSpeed)

    def car_Speedup(self):
        self.carSpeed += MOVE_INCREMENT




