from menu import MENU, resources


Local_resources = resources
Money = 0



def check(items, coffee):
    g = True
    while g:
        for r in MENU[coffee]['ingredients']:
            if r != items:
                Local_resources[r] += MENU[coffee]['ingredients'][r]
            else:
                g = False
            



def coffee_Mechin_Processing(coffee):
    global Local_resources
    global Money

    Total_Coin = 0
    coin_Type = ['quarters', 'dimes', 'nickles', 'pennies']
    coin_Price = ['0.25', '0.1', '0.05', '0.01']
    Ingrediants = []

    
    for items in MENU[coffee]['ingredients']:
        if Local_resources[items] - MENU[coffee]['ingredients'][items] < 0:
            print(f"Sorry not enough {items}")
            check(items, coffee)
            main()
        elif Local_resources[items] - MENU[coffee]['ingredients'][items] >= 0:
            # print(f"{items} : {MENU[coffee]['ingredients'][items]}")
            Ingrediants.append(MENU[coffee]['ingredients'][items])
            Local_resources[items] -= MENU[coffee]['ingredients'][items]
    
    for coin in range(4):
        InPrice = float(input(f"How manny {coin_Type[coin]}: "))

        Total_Coin += InPrice * float(coin_Price[coin])
    
    if Total_Coin < MENU[coffee]['cost']:
        for items in MENU[coffee]['ingredients']:
            Local_resources[items] += MENU[coffee]['ingredients'][items]



    
    Money += MENU[coffee]['cost']
    



    if Total_Coin < MENU[coffee]['cost']:
        print(f"Here is coffee your {coffee} ☕ Enjoy!")
    elif Total_Coin > MENU[coffee]['cost']:
        print(f"Here is {round(Total_Coin - MENU[coffee]['cost'], 2)} in change.")
        print(f"Here is coffee your {coffee} ☕ Enjoy!")
    elif Total_Coin < MENU[coffee]['cost']:
        print("Sorry that's not enough money. Money refuned.")



def main():
    Processing = True
    

    while Processing:

        coffee = input("\tWhat whould you like? (espresso/latte/cappuccino) ").lower()

        if coffee == 'report':
            for item in Local_resources:
                print(f"{item} : {resources[item]}")
            print(f"Money: ${Money}")
        else:
            coffee_Mechin_Processing(coffee)
            

        # Processing = False

main()