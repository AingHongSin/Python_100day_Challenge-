from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
clear()
print(logo)

Bidder = {}

Start = True
while Start:

    Name = input("What is your name?\n")
    Bird = int(input("What is your bird?\n$"))
    More = input('Are there any bidder? Type "yes" for "no" \n').lower()

    Bidder[Name] = Bird
    


    if More == "no":
        Start = False
    clear()

def Calculate():
    Value = 0
    for people in Bidder:
        if Bidder[people] > Value:
            Value = Bidder[people]
    for Winner, heightest_bidder in Bidder.items():
        if Value == heightest_bidder:
            print(f"The winner is {Winner} a bird of ${Value}")
Calculate()
        
