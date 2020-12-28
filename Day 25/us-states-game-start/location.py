from turtle import Turtle

class State_Location(Turtle):

    def __init__(self):
        super().__init__()

        self.hideturtle()
        self.penup()
        self.score = 0


    def show_location_and_state(self, state_name, location):
        self.goto(location)
        self.write(state_name)

    def displa_Score(self):
        return self.score

    def increasing_score(self):
        self.score += 1

