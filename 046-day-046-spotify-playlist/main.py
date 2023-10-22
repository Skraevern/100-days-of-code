import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# user_input = input(
#     "What your do you want to travel to? Type the date in this format YYYY-MM-DD: "
# )

URL = "https://www.billboard.com/charts/hot-100/"
user_input = "1988-07-17"
CLIENT_ID = os.environ.get("SPOTIPY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIPY_CLIENT_SECRET")
# print(CLIENT_ID)
# print(CLIENT_SECRET)


website = requests.get(f"{URL}{user_input}")
with open("./billboard-hot-100", "wb+") as file:
    file.write(website.content)

with open("./billboard-hot-100", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

lists = soup.find_all(name="li", class_="o-chart-results-list__item")
songs = []
for i in lists:
    if i.find(name="h3") != None:
        h3 = i.find(name="h3")
        song = h3.string.strip()
        songs.append(song)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt",
        username="skraevern",
    )
)
user_id = sp.current_user()["id"]
