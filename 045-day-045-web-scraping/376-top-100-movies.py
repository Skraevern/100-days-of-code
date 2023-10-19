import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


website = requests.get(URL)
with open("./top-100.html", "wb+") as file:
    file.write(website.content)


with open(file="./top-100.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

titles = soup.find_all(name="h3", class_="title")
titles = titles[::-1]

for title in titles:
    try:
        with open(file="top-100.txt", mode="a") as file:
            file.write(f"\n{title.string}")
    except FileNotFoundError:
        with open(file="top-100.txt", mode="w") as file:
            file.write(title.string)
