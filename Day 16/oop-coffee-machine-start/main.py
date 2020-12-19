## Coffee Machine Documentation Link: https://docs.google.com/document/d/e/2PACX-1vTragRHILyj76AvVgpWeOlEaLBXoxPM_43SdEyffIKtOgarj42SoSAsK6LwLAdHQs2qFLGthRZds6ok/pub


from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Machine_is_on = True


while Machine_is_on:

    drink = input("What do you like? (Cappuccino/Latte/Espresso): ")


    if drink == 'report':
        coffeeMaker = CoffeeMaker()
        print(coffeeMaker.report())
    elif drink == 'off':
        Machine_is_on = False
    else:
        coffeeMaker= CoffeeMaker()
        print(CoffeeMaker.is_resource_sufficient(drink))

        print("Work")
