from bs4 import BeautifulSoup

with open(file="./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")
