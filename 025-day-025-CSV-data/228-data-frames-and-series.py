import pandas

data = pandas.read_csv("./weather_data.csv")
print(type(data))  # <class 'pandas.core.frame.DataFrame'>
print(type(data["temp"]))  # <class 'pandas.core.series.Series'>

data_dict = data.to_dict()
print(data_dict)
# {'day': {0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'}, 'temp': {0: 12, 1: 14, 2: 15, 3: 14, 4: 21, 5: 22, 6: 24}, 'condition': {0: 'Sunny', 1: 'Rain', 2: 'Rain', 3: 'Cloudy', 4: 'Sunny', 5: 'Sunny', 6: 'Sunny'}}

temp_list = data["temp"].to_list()
print(temp_list)  # [12, 14, 15, 14, 21, 22, 24]

average_temp = 0
for temp in temp_list:
    average_temp += temp
average_temp /= len(temp_list)
print(average_temp)  # 17.4285714228571427

average_temp = sum(temp_list) / len(temp_list)
print(average_temp)  # 17.4285714228571427

average_temp = data["temp"].mean()
print(average_temp)  # 17.4285714228571427

max_temp = data["temp"].max()
print(max_temp)  # 24

# get data n columns
print(data["condition"])
print(data.condition)
# 0     Sunny
# 1      Rain
# 2      Rain
# 3    Cloudy
# 4     Sunny
# 5     Sunny
# 6     Sunny
# Name: condition, dtype: object

# get data in rows
row = data[data.day == "Monday"]
print(row)
#       day  temp condition
# 0  Monday    12     Sunny

row = data[data.condition == "Sunny"]
print(row)
#       day  temp condition
# 0    Monday    12     Sunny
# 4    Friday    21     Sunny
# 5  Saturday    22     Sunny
# 6    Sunday    24     Sunny

row = data[data.temp == data.temp.max()]
print(row)
#       day  temp condition
# 6  Sunday    24     Sunny

monday = data[data.day == "Monday"]
print(monday.condition)
# 0    Sunny

monday_temp_fahr = (monday.temp * 1.8) + 32
print(monday_temp_fahr)
# 0    53.6

# Create dataframe from scratch
student_dict = {"students": ["Amy", "James", "Angela"], "score": [76, 56, 65]}
student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
#   students  score
# 0      Amy     76
# 1    James     56
# 2   Angela     65

student_data_frame.to_csv("./student_data_frame.csv")
