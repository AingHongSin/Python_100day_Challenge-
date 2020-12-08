# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
Height_of_Total = 0
NumberStudent = 0
for t in student_heights:
  Height_of_Total += t
  NumberStudent += 1

print(f"Average: {Height_of_Total/NumberStudent}")
