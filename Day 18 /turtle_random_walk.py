import turtle as tim
import random



t = tim.Turtle()
s = tim.Screen()

tim.colormode(255)
angle = [0, 90, 180, 270]
run = 0
t.speed(10)
t.pensize(10)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)

    return random_color

while run <= 200:
    colormod = (random_color())
    turn = random.choice(angle)
    t.color(random_color())

    t.forward(20)
    t.setheading(turn)

    run += 1

s.exitonclick()