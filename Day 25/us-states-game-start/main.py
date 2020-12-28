from turtle import Screen, Turtle
from location import State_Location
import pandas


screen = Screen()
turtle = Turtle()
display = State_Location()

screen.title('US-States_games')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
game_start = True
data = pandas.read_csv('50_states.csv')

guess_state = []
all_state = data.state.to_list()
missing_state = []

while len(guess_state) < 50:
    answer_state = screen.textinput(title = f"{len(guess_state)}/50 States Correct", prompt = "What's another state name?").title()
    print(answer_state)
    if answer_state == 'Exit':
        for state in all_state:
            if state not in guess_state:
                missing_state.append(state)
        new_date = pandas.DataFrame(missing_state)
        new_date.to_csv('state_to_learn.csv')
        break
    if answer_state in data.state.to_list():
        if answer_state not in guess_state:
            guess_state.append(answer_state)
            location = data[data.state == answer_state]
            print(f"x = {location.x}, y = {location.y} ")
            coor = (int(location.x), int(location.y))
            print(coor)
            display.show_location_and_state(location.state.item(), coor)
            display.increasing_score()




