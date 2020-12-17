from art import logo, vs
from game_data import data
from replit import clear
import random

answerBool = True
next_round = False
distC = []
score = 0
    
while answerBool:
    
    clear()
    print(logo)
    if next_round:
        print(f"You'r right! Current score: {score} ")
        distA = distC[-1]
    else:
        distA = random.choice(data)
        

    print(f"Compare A: {distA['name']}, {distA['description']}, from {distA['country']} ")

    print(vs)

    distB = random.choice(data)
    distC = [distB]

    if distB != distA:

        print(f"Again B: {distB['name']}, {distB['description']}, from {distB['country']} ")

        UserAnswer = input("Who has more follower? Typr 'A' or 'B': ").lower()
      

        if distA['follower_count'] > distB['follower_count']:
            correct_answer = 'a'
            print("A Win")
        else:
            correct_answer = 'b'
            print("B Win")
        if UserAnswer == correct_answer:
            score += 1
            next_round = True
        else:
            if UserAnswer != correct_answer:
                clear()
                print(logo)
                print(f"Sorry that's wrong. Fianl score: {score}")
                answerBool = False
