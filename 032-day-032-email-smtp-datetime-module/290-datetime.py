import datetime as dt

now = dt.datetime.now()
print(now)  # 22023-10-05 18:19:57.065218

print(now.year)  # 2023

print(now.month)  # 10

print(now.day)  # 5

print(now.hour)  # 18

print(now.minute)  # 19

print(now.second)  # 57

print(now.microsecond)  # 65218

print(now.weekday())  # 3 # fourth day of week. Start at 0

date_of_birth = dt.datetime(year=1988, month=7, day=17)
print(date_of_birth)  # 1988-07-17 00:00:00
