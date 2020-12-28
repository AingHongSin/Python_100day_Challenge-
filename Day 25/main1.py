# data = []
#
# with open("weather_data.csv", mode = 'r') as file:
#     for d in file.readlines():
#         data.append(d.split(',')[1])
#
# data.remove('temp')
# print(data)

# import csv
#
# with open('weather_data.csv', mode = 'r') as file:
#     data = csv.reader(file)
#     temp = []
#     for row in data:
#         print(row[1])
#         if row[1] !='temp':
#             temp.append(int(row[1]))
#     print(temp )


import pandas

data = pandas.read_csv('weather_data.csv')
# print(type(data))
# print(type(data['temp']))
#
# data_dist = data.to_dict()
# print(data_dist)
#
# temperature_list = data['temp'].to_list()
# print(temperature_list)
# print(f"average {sum(temperature_list)/len(temperature_list)}")
# print(data['temp'].mean())
# print('mix: ', data['temp'].max())

# get data in column

# print(data['condition'])
# print(data.condition)

# get data in row
# print(data[data.day == 'Monday'])


# print(data[data.temp == data['temp '].max()])

monday = data[data.day == 'Monday']
print(monday.temp)


print("F = ", (monday.temp * 9/5) + 32)