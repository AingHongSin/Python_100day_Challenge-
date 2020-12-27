from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

        with open('data.txt', mode = 'r') as file:
            H_S = file.read()
        file.close()
        self.heightest_score = int(H_S)
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} Height Score: {self.heightest_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.heightest_score:
            self.heightest_score = self.score
            with open('data.txt', mode = 'w') as file:
                file.write(f"{self.heightest_score}")
            # file.close()
        self.score = 0

        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
