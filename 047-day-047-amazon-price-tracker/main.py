import requests
from bs4 import BeautifulSoup
import os
import smtplib

URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"

headers = {
    "Accept-Language": "nb-NO,nb;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
}

# --- Scraping
website = requests.get(f"{URL}", headers=headers)
with open("./page", "wb+") as file:
    file.write(website.content)

with open("./page", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
price = soup.find(name="span", class_="a-offscreen")
price = float(price.string.replace("$", ""))
print(price)

# --- email alert


gmail = "kristian.skreosen.test@gmail.com"  # smtp.gmail.com
gmail_password = ""  # app password
yahoo = "kristianskreosen.test@yahoo.com"  # smtp.mail.yahoo.com

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=gmail, password=gmail_password)
    connection.sendmail(
        from_addr=gmail,
        to_addrs=yahoo,
        msg=f"Subject:Rice Cooker Price\n\nPrice of rice cooker is now {price}",
    )
