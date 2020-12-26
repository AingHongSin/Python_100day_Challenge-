import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

car_list = []

player = Player()
score = Scoreboard()
car = CarManager()

screen.listen()
screen.onkey(player.move, "Up")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.Car_Generate()
    car.driving()
    if player.ycor() > 280:
        score.Indcreasing_Level()
        player.start_location()
        car.car_Speedup()

    for m_car in car.all_car:
        if m_car.distance(player) < 20:
            game_is_on = False
            score.game_Over()



screen.exitonclick()
