# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = weight/(height ** 2)

if BMI < 1.85:
  print(f"Your BMI is {round(BMI), 2}, you are underweight.")
elif 1.85 <= BMI < 25:
  print(f"Your BMI is {round(BMI), 2}, you have a normal weight.")
elif 25 <= BMI > 30:
  print(f"Your BMI is {round(BMI, 2)}, you are slightly weight")
elif 30 <= BMI > 35 :
  print(f"Your BMI is {round(BMI, 2)}, you are obese ")
else :
  print(f"Your BMI is {round(BMI, 2)}, you are clinically obese")

