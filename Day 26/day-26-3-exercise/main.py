with open('file1.txt', mode = 'r') as file1:
    data1 = file1.readlines()

with open('file2.txt', mode = 'r') as file2:
    data2 = file2.readlines()


result = [int(sameNum) for sameNum in data1 if sameNum in data2]

# Write your code above 👆

print(result)


