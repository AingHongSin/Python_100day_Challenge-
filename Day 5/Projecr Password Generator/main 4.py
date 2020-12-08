#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# letterList = []
# numList = []
# symbleList = []

# for l in range(0, nr_letters):
#   ran_letter = random.randint(0, len(letters) - 1)
#   letterList.append(letters[ran_letter])

# for s in range(0, nr_symbols):
#   ran_symbole = random.randint(0, len(symbols) - 1)
#   symbleList.append(symbols[ran_symbole])

# for n in range(0, nr_numbers):
#   ran_number = random.randint(0, len(numbers) - 1)
#   numList.append(numbers[ran_number])

# Passlist = [letterList + symbleList + numList]
# r = Passlist[0][0]
# for i in range(1, len(Passlist[0])):
#   r += str(Passlist[0][i])
# print("Password: ", r)

# Pass = ""
# for char in range(0, nr_letters):
#   Pass += random.choice(letters)
# for char in range(0, nr_symbols):
#   Pass += random.choice(symbols)
# for char in range(0, nr_numbers):
#   Pass += random.choice(numbers)

# print("Password : ", Pass)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

PassList = []
for char in range(1, nr_letters + 1):
  PassList.append(random.choice(letters))
for char in range(1, nr_symbols + 1):
  PassList.append(random.choice(symbols))
for char in range(1, nr_numbers + 1):
  PassList.append(random.choice(numbers))

print(PassList)
random.shuffle(PassList)
Password = ""
for char in PassList:
  Password += char
print("Your Password is : " ,Password)