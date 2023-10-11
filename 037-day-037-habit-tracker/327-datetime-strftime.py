import datetime

today = datetime.datetime.now()
# https://www.w3schools.com/python/gloss_python_date_format_codes.asp
print(today)  # 2023-10-11 10:41:46.536006
print(today.strftime("%Y%m%d"))  # 20231011

day = datetime.datetime(year=2023, month=7, day=17)
print(day)  # 2023-07-17 00:00:00
