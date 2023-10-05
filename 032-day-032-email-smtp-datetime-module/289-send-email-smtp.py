import smtplib

gmail = "kristian.skreosen.test@gmail.com"  # smtp.gmail.com
gmail_password = ""
yahoo = "kristianskreosen.test@yahoo.com"  # smtp.mail.yahoo.com

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=gmail, password=gmail_password)
    connection.sendmail(
        from_addr=gmail,
        to_addrs=yahoo,
        msg="Subject:Hello World!\n\nHello World with subject",
    )
