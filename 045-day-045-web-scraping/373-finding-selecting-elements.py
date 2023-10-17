from bs4 import BeautifulSoup

with open(file="./website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.p)
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# Only first

print(soup.find_all(name="p"))
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>
# <p><em>Founder of <strong><a href="https://www.appbrewery.co/">The App Brewery</a></strong>.</em></p>, <p>I am an iOS and Web Developer. I ❤️ coffee and motorcycles.</p>

all_anchor_tags = soup.find_all(name="a")
for tag in all_anchor_tags:
    print(tag.string)  # print(tag.getText()) same
    # The App Brewery
    # My Hobbies
    # Contact Me

    print(tag.get("href"))
    # https://www.appbrewery.co/
    # https://angelabauer.github.io/cv/hobbies.html
    # https://angelabauer.github.io/cv/contact-me.html

print(soup.find_all(name="h1", id="name"))
# <h1 id="name">Angela Yu</h1>

print(soup.find_all(name="h3", class_="heading"))  # Class reserved. class_
# [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]

print(soup.select_one(selector="p a"))
# <a href="https://www.appbrewery.co/">The App Brewery</a>

print(soup.select(selector=".heading"))  # Class of heading
# [<h3 class="heading">Books and Teaching</h3>, <h3 class="heading">Other Pages</h3>]
