from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


s = Screen()
s.setup(600,600)
s.bgcolor('black')
s.title("my snake game")
s.tracer()

snake = Snake()
s.listen()
f = Food()
sb = Scoreboard()

s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")


start = True
while start:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(f) < 15:
        f.refrash()
        snake.extant()
        sb.increase_the_score()


    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() <= -280 or snake.head.ycor() >= 280:
        start = False
        sb.game_over()


    for sagment in snake.sagment_List[0:]:
        if snake.head.distance(sagment) < 10:
            start = False
            sb.game_over()







s.exitonclick()