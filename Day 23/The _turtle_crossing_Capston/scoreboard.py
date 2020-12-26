from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        self.current_Level = 0

        self.penup()
        self.hideturtle()

        self.Display_ScoreBoad()

    def Display_ScoreBoad(self):
        self.clear()
        self.goto(-290,270)
        self.write(f"Level: {self.current_Level}", False, font = FONT)

    def Indcreasing_Level(self):
        self.current_Level += 1
        self.Display_ScoreBoad()

    def game_Over(self):
        self.goto(-65,0)
        self.write("GAME OVER",False, font = FONT)
