import turtle as tl
import random

s = tl.Screen()
s.setup(500,400)
resing_start = False
color = ['orange', 'red', 'blue', 'green', 'lime', 'brown']
user_input = s.textinput(title="Make your bet", prompt = "Whitch turtle will win the race? Enter color: ")
turtle_list = []
sp = 0
for turtle in range(6):
    t = tl.Turtle(shape='turtle')
    t.penup()
    t.color(color[turtle])
    t.goto(-230, -125 + sp)
    sp += 50
    turtle_list.append(t)


if user_input:
    resing_start = True

while resing_start:
    for turtle in turtle_list:
        if turtle.xcor() > 230:
            resing_start = False
            if turtle.pencolor == user_input:
                print(f"You won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You won! The {turtle.pencolor()} turtle is the winner!")

        else:
            random_destain = random.randint(0, 10)
            turtle.forward(random_destain)



s.exitonclick()