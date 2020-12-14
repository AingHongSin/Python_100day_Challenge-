############### Blackjack Project #####################
from replit import clear
import random
from art import logo

gameStart = False


Start_Game = input("Do you want to play the blackjack game? Type 'y' for start or type 'n' for exit: ")

if Start_Game == 'y':
    gameStart = True

First_Round = True
next_Round = False
ComputerTurn = False
UserTurn = False
nextRoundCount = 0


Your_CardList = []
Computer_CardList = []


def FirstCard():  
    print("Card Processing...")
    for chose in range(2):
        Your_CardList.append(random.choice(cardList))
        Computer_CardList.append(random.choice(cardList))
    
    

def nextCard():
    for card in range(1):
        Your_CardList.append(random.choice(cardList))

    Computer_Turn()
    
    if sum(Your_CardList) > 23:
        Over = sum(Your_CardList) % 23 
        UserTotal = Over 
        
    if sum(Computer_CardList) > 23:
        
        over = sum(Computer_CardList) % 23
        ComputerTotal = over
    

def Computer_Turn():
    ComputerTotal = sum(Computer_CardList)
    UserTotal = sum(Your_CardList)
    if ComputerTotal < UserTotal:
        for card in range(1):
            Computer_CardList.append(random.choice(cardList))

        

def FinalDisplay():
    if sum(Your_CardList) > 23 or sum(Computer_CardList) > 23:
        if sum(Your_CardList) > 23:
            Over = sum(Your_CardList) % 23 
            UserTotal = Over 
            
        if sum(Computer_CardList) > 23:
            over = sum(Computer_CardList) % 23
            ComputerTotal = over
    UserTotal = sum(Your_CardList)
    ComputerTotal = sum(Computer_CardList)


    print(f"Your final hand {Your_CardList}, final score: {UserTotal}")
    print(f"Computer final hand {Computer_CardList}, final score: {ComputerTotal}")
    
    if ComputerTotal < UserTotal:
        print("Opponen went over. You Win!")
    elif ComputerTotal > UserTotal:
        print("Opponen went over. You Lose!")
    else:
        print("Opponen went over. You Draw!")


while gameStart :
    
    cardList = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    if First_Round:
        clear()
        print(logo)
        # Function
        FirstCard()
        First_Round = False

    UserTotal = sum(Your_CardList)
    ComputerTotal = sum(Computer_CardList)

        
    if nextRoundCount < 3:

        
        print(f"Your Card: {Your_CardList}, currernt score: {UserTotal}")
        print(f"Computer first card: {Computer_CardList[0]}")
        another_Card = input("Type 'y' for another card and type 'n' for pass: ")
        

    else:
        FinalDisplay()
        gameStart = False


    if another_Card == 'y':
        nextRoundCount += 1
        nextCard()
        
    elif another_Card == 'n':
        Computer_Turn()
        FinalDisplay()
        gameStart = False
        
        
