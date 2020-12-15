################ Guess the number #################

import random
from art import logo, WinGame

print(logo)

print("Wellcom to the Number Guessing Game.")
print("I'll tkink the number from 1 to 100.")
print("And than u guess what is that number.")
Type_of_Game = input("Choice the deffically. Type 'hard' for or 'easy' : ").lower()

HardGameBool = False
GuessingCound = 0
FirstGame = True
Finish = False

if Type_of_Game == "hard":
    GuessingCound = 5
    HardGameBool = True
elif Type_of_Game == "easy":
    GuessingCound = 10

Answer = random.randint(1,100)
print(f"Pssst, the correct answer is {Answer}")

while GuessingCound > 0:

    if not Finish:
        print(f"you have {GuessingCound} attemp for guess the number.")
        Gussing_Num = int(input("Make a guess: "))
        GuessingCound -= 1

    
    
    if Gussing_Num != Answer:
        if Gussing_Num < Answer:
            print("Too low.")
        elif Gussing_Num > Answer:
            print("Too heigh.")
        print("Guess again.")
        if GuessingCound == 0:
            print("You've run out of guesses, you lose.")
    elif Gussing_Num == Answer:
        print(WinGame)
        print(f"You got it. The answer was {Answer}")
        Finish = True
        GuessingCound = 0
