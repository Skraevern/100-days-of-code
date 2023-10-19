import requests
from bs4 import BeautifulSoup

URL = "https://news.ycombinator.com/show"

response = requests.get(URL)
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
print(soup.find(name="a", class_="storylink"))
