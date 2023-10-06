import requests
import datetime
import time
import smtplib

API_SUN = "https://api.sunrise-sunset.org/json"
API_ISS = "http://api.open-notify.org/iss-now.json"
SILJAN_LAT = 59.276020
SILJAN_LNG = 9.713000
ISS_ORBIT_MIN = 93

gmail = "kristian.skreosen.test@gmail.com"  # smtp.gmail.com
gmail_password = ""  # app password

while True:
    # --- Sunset Sunrise --- #
    parameters = {"lat": SILJAN_LAT, "lng": SILJAN_LNG, "formatted": 0}

    sun_response = requests.get(url=API_SUN, params=parameters)
    sun_response.raise_for_status()
    sun_data = sun_response.json()

    sunset_hour = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])
    sunrise_hour = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])

    # --- ISS --- #
    iss_response = requests.get(url=API_ISS)
    iss_response.raise_for_status()
    iss_data = iss_response.json()

    iss_lat = float(iss_data["iss_position"]["latitude"])
    iss_lng = float(iss_data["iss_position"]["longitude"])

    # --- Notifier --- #
    now = datetime.datetime.now()
    if now.hour > sunrise_hour or now.hour < sunrise_hour:  # Between sunset and sunrise
        if (
            ((SILJAN_LNG - 20) < iss_lng)  # West of Siljan
            and ((SILJAN_LNG + 20) > iss_lng)  # East of Siljan
            and (iss_lat > (SILJAN_LAT - 20))  # Long enough to North
        ):
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(user=gmail, password=gmail_password)
                connection.sendmail(
                    from_addr=gmail,
                    to_addrs=gmail,
                    msg=f"Subject:ISS overhead!\n\nLook up! ISS is at latitude:{iss_lat} longitude {iss_lng}",
                )
                time.sleep((ISS_ORBIT_MIN * 60) / 4)

    else:
        time.sleep(60)
