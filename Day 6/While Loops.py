## This code for run in this 
## Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json


def turn_right():
    for t in range(3):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left() 
        
        
step = 6
while step > 0:
    jump()
    if at_goal():
        step = 0
    step -= 1


## Module 2
def turn_right():
    for t in range(3):
        turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left() 

while not at_goal():
    jump()
