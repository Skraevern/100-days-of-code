import csv
import pandas

with open("./weather_data.csv") as file:
    data = csv.reader(file)

    temperatures = []
    for row in data:
        print(row)
        # ['day', 'temp', 'condition']
        # ['Monday', '12', 'Sunny']
        # ['Tuesday', '14', 'Rain']
        # ['Wednesday', '15', 'Rain']
        # ['Thursday', '14', 'Cloudy']
        # ['Friday', '21', 'Sunny']
        # ['Saturday', '22', 'Sunny']
        # ['Sunday', '24', 'Sunny']
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)  # [12, 14, 15, 14, 21, 22, 24]


csv_data = pandas.read_csv("./weather_data.csv")
print(csv_data)
#          day  temp condition
# 0     Monday    12     Sunny
# 1    Tuesday    14      Rain
# 2  Wednesday    15      Rain
# 3   Thursday    14    Cloudy
# 4     Friday    21     Sunny
# 5   Saturday    22     Sunny
# 6     Sunday    24     Sunny
