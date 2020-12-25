from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

s = Screen()
s.setup(800,600)
s.bgcolor('black')
s.title("PONG")
s.tracer(0)

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

s.listen()
s.onkey(r_paddle.go_up, 'Up')
s.onkey(r_paddle.go_down, 'Down')
s.onkey(l_paddle.go_up, 'w')
s.onkey(l_paddle.go_down, 's')

game_is_on = True

while game_is_on:

    time.sleep(ball.ball_speed)
    s.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bound_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bound_x()

    elif ball.xcor() > 340:
        ball.ball_reset()
        scoreboard.l_point()
        scoreboard.display_score()

    elif ball.xcor() < -340:
        ball.ball_reset()
        scoreboard.r_point()
        scoreboard.display_score()


s.exitonclick()