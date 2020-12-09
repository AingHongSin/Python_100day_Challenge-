## This code for run in this 
## Link: https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json


                
                def turn_right():
                    for t in range(3):
                        turn_left()
                        
                for t in range(6):
                    move()
                    turn_left()
                    move()
                    turn_right()
                    move()
                    turn_right()
                    move()
                    turn_left() 