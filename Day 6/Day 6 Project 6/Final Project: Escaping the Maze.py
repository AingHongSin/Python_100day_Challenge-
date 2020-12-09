## This code for run in this 
## Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Maze&url=worlds%2Ftutorial_en%2Fmaze1.json

## My Module
def turn_right():
    for t in range(3):
        turn_left()
        
def turn_back():
    for t in range(2):
        turn_left()

while not at_goal():
    while wall_on_right() and front_is_clear():
        move()
    while right_is_clear():
        turn_right()
        if not at_goal():
            move()
    if not at_goal():
        if front_is_clear():
            move()
        elif wall_in_front() and wall_on_right():
            turn_left()
    else:
        at_goal()     



# Sulution from Professor:

def turn_right():
    for t in range(3):
        turn_left()
        
def turn_back():
    for t in range(2):
        turn_left()

while front_is_clear():
    move()
turn_left()

while not at_goal():
    if right_is_clear():
        turn_right()
    elif fron_is_clear():
        move()
    else:
    turn_left()