# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

Amount = len(names)
randomPeople = random.randint(0,Amount - 1)

print(f"{names[randomPeople]}, is goint go buy meals today!")

