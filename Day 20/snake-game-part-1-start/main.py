from turtle import Turtle, Screen
from snake import Snake
import time


s = Screen()
s.setup(600,600)
s.bgcolor('black')
s.title("my snake game")
s.tracer()

snake = Snake()
s.listen()

s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


start = True
while start:
    s.update()
    # time.sleep(0.1)
    snake.move()










s.exitonclick()