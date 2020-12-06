import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

mainList = [rock, paper, scissors]

User = int(input("What do you choose? Type 0 for rock, 1 for paper, 2 for scissors. "))

if 0<= User <=2:
  
  print("You Choose", mainList[User])

  Machin = random.randint(0, 2)
  print(f"Computer Choose: {mainList[Machin]}")

  if User == 0 and Machin == 1:
    print("You Lose!")
  elif User == 0 and Machin == 2:
    print("You Win!")

  elif User == 1 and Machin == 0:
    print("You Win!")
  elif User == 1 and Machin == 2:
    print("You Lose!")

  elif User == 2 and Machin == 0:
    print("You Lose!")
  elif User == 2 and Machin == 1:
    print("You Win!")

  elif User == Machin:
    print("It's draw! Please Try Again")
else:
  print("Your number doesn't have in the list")


