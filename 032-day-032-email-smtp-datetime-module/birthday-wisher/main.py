##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib

now = dt.datetime.now()
gmail = "kristian.skreosen.test@gmail.com"  # smtp.gmail.com
gmail_password = ""  # app password
letter_list = []

for i in range(1, 4):
    with open(f"./letter_templates/letter_{i}.txt", "r") as file:
        letter = file.read()
        letter_list.append(letter)

with open("./birthdays.csv", "r") as file:
    data = pandas.read_csv(file)
    birthday_list = data.to_dict(orient="records")

for i in range(len(birthday_list)):
    if (birthday_list[i]["month"] == now.month) and (
        birthday_list[i]["day"] == now.day
    ):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=gmail, password=gmail_password)
            connection.sendmail(
                from_addr=gmail,
                to_addrs=gmail,
                msg=f'Subject:Happy B Day!\n\n{random.choice(letter_list).replace("[NAME]", birthday_list[i]["name"])}',
            )
