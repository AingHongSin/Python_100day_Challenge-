# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
NameTogether = name1.lower() + name2.lower()

T = NameTogether.count("t")
R = NameTogether.count("r")
U = NameTogether.count("u")
E = NameTogether.count("e")

FirstNum = str(T + R + U + E)

L = NameTogether.count("l")
O = NameTogether.count("o")
V = NameTogether.count("v")
E1 = NameTogether.count("e")

SecondNum = str(L + O + V + E1)

Total = int(FirstNum + SecondNum)

if Total < 10 or Total > 90:
  print(f"Your score is {Total}, you go together like coke and menthos")
elif 40 < Total < 50 :
  print(f"Your score is {Total}, your are alright")
else:
  print(f"Your score is {Total}")