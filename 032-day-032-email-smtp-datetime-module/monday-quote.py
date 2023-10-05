import smtplib
import datetime as dt
import random

gmail = "kristian.skreosen.test@gmail.com"  # smtp.gmail.com
gmail_password = ""  # app password

now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 3:
    with open(file="quotes.txt") as file:
        all_quotes = file.readlines()

    quote_of_the_day = random.choice(all_quotes)
    print(quote_of_the_day)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=gmail_password)
        connection.sendmail(
            from_addr=gmail,
            to_addrs=gmail,
            msg=f"Subject:Monday Quote!\n\n{quote_of_the_day}",
        )
