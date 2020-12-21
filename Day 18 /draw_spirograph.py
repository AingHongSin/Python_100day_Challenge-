import turtle as tl
import random

t = tl.Turtle()

tl.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


run = 0
t.speed('fastest')
for angle in range(0, 360, 10):
    t.color(random_color())
    t.setheading(angle)
    t.circle(100)


s = tl.Screen()
s.exitonclick()


