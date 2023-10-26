import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

FORM = "https://docs.google.com/forms/d/e/1FAIpQLSfXDSU2nctGXYA54x5OFpl2RFQklaAZCG8ctvgHFmi7BUDkKQ/viewform?usp=sf_link"
ZILLOW = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"


headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.zillow.com",
    "Referer": "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22isMapVisible%22%3Afalse%2C%22mapBounds%22%3A%7B%22west%22%3A-122.62078322363281%2C%22east%22%3A-122.24587477636719%2C%22south%22%3A37.676990660829674%2C%22north%22%3A37.873461716438335%7D%2C%22mapZoom%22%3A11%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22price%22%3A%7B%22min%22%3Anull%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3Anull%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%2C%22max%22%3Anull%7D%7D%2C%22isListVisible%22%3Atrue%7D",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36",
}


# --- bf4 --- #
response = requests.get(f"{ZILLOW}", headers=headers)
with open("./website.html", "wb+") as file:
    file.write(response.content)

with open("./website.html", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

prices = []
links = []
adresses = []

for price in soup.find_all("span", attrs={"data-test": "property-card-price"}):
    prices.append(price.text)

for link in soup.find_all("a", attrs={"data-test": "property-card-link"}):
    if link.get("href")[0] == "/":
        links.append(f'https://www.zillow.com{link.get("href")}')
    else:
        links.append(link.get("href"))
links = list(dict.fromkeys(links))

for adress in soup.find_all("address", attrs={"data-test": "property-card-addr"}):
    adresses.append(adress.text)


# --- Selenium --- #

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(FORM)

for i in range(0, len(prices)):
    try:
        another_form = driver.find_element(
            By.XPATH, value="/html/body/div[1]/div[2]/div[1]/div/div[4]/a"
        )
        another_form.click()
    except:
        pass
    finally:
        address_input = driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        price_input = driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        link_input = driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input',
        )
        send_btn = driver.find_element(
            By.XPATH,
            value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span',
        )

        address_input.send_keys(adresses[i])
        price_input.send_keys(prices[i])
        link_input.send_keys(links[i])
        send_btn.click()

driver.quit()
