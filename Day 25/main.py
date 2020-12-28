import pandas

dist = {}
count = []
FurColor = []
data = pandas.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

Fur_color = data['Primary Fur Color'].to_list()
furcolor = set(Fur_color)
for row in furcolor:
    FurColor.append(row)
    count.append(Fur_color.count(row))
dist['Fur Color'] = FurColor
dist['Count'] = count

print(dist)



new_data = pandas.DataFrame(dist)
# print(new_data)
new_data.to_csv('new_data.csv')