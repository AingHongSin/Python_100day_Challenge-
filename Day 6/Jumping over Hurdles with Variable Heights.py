## This code for run in this 
## Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json


def turn_right():
    for t in range(3):
        turn_left()

def jump():
    turn_left()
    move()
    while wall_on_right():
        move()
    if right_is_clear():
        turn_right()
        move()
        turn_left()
    while front_is_clear():
        move()
    if wall_in_front():
        turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()