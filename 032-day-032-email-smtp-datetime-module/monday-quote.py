import smtplib
import datetime as dt
import random
import os

gmail = "kristian.skreosen.test@gmail.com"  # smtp.gmail.com
gmail_password = os.environ.get("PYTHON_MAIL_PASSWORD")  # app password

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open(file="quotes.txt") as file:
        all_quotes = file.readlines()

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=gmail, password=gmail_password)
        connection.sendmail(
            from_addr=gmail,
            to_addrs=gmail,
            msg=f"Subject:Monday Quote!\n\n{random.choice(all_quotes)}",
        )
