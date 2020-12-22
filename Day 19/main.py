import turtle as tl

t = tl.Turtle()
s = tl.Screen()

def move_forward():
    t.forward(10)

def move_backward():
    t.backward(10)

def turn_left():
    t.lt(10)

def turn_right():
    t.rt(10)

def clear_fun():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

s.listen()
s.onkey(key = "w", fun = move_forward)
s.onkey(key = "s", fun = move_backward)
s.onkey(key = "a", fun = turn_left)
s.onkey(key = "d", fun = turn_right)
s.onkey(key = "c", fun = clear_fun)

s.exitonclick()