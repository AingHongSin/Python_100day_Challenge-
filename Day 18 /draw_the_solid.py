from turtle import Turtle, Screen
import random

t = Turtle()
s = Screen()
color = ['blue', 'green', 'red', 'cyan', 'magenta', 'yellow', 'lime', 'brown']
for angle in range(3, 11):
    t.color(random.choice(color))
    for r in range(angle):

        t.forward(100)
        t.right(360/angle)



s.exitonclick()