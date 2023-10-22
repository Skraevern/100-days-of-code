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

# --- Scraping
website = requests.get(f"{URL}{user_input}")
with open("./billboard-hot-100", "wb+") as file:
    file.write(website.content)

with open("./billboard-hot-100", "r") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

songs = soup.find_all(name="h3", id="title-of-a-story", class_="u-line-height-125")
song_titles = [title.getText().strip("\n\t") for title in songs]
artists = soup.find_all(name="span", class_="u-max-width-330")
artist_names = [name.getText().strip("\n\t") for name in artists]
song_and_artist = dict(zip(song_titles, artist_names))

print(song_and_artist)

# --- Spotify Authentication
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


# --- Search Spotify for song by title and artist
song_uris = []
for song, artist in song_and_artist.items():
    try:
        result = sp.search(q=f"track:{song} artist: {artist}", type="track")
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        pass

print(f"Number of songs found: {len(song_uris)}")

# Create new private playlist in Spotify
playlist = sp.user_playlist_create(
    user=user_id,
    name=f"{user_input} Billboard 100",
    public=False,
)
sp.playlist_add_items(playlist_id=["id"], items=song_uris)
print(f"New playlist '{user_input} Billboard 100' succsessfully created on Spotify")
