from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

CLIENT_ID = os.getenv("SPOTIFY_CLIENTID")
CLIENT_SECRET = os.getenv("SPOTIFY_CLIENTSECRET")

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/91.0.4472.124 Safari/537.36"
}

url = f"https://www.billboard.com/charts/hot-100/{date}/"

response = requests.get(url=url, headers=headers)
billboard_website = response.text

soup = BeautifulSoup(billboard_website, "html.parser")

top_100_songs = soup.select("li ul li h3.c-title.a-no-trucate")

top_100_songs_title = [song.getText().strip() for song in top_100_songs]

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri="http://example.com",
                                               scope="playlist-modify-private",
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]

year = date.split("-")[0]
top_100_songs_uri = []

for song in top_100_songs_title:

    query = f"track:{song} year:{year}"
    results = sp.search(q=query)

    try:
        uri = results["tracks"]["items"][0]["uri"]
        top_100_songs_uri.append(uri)

    except KeyError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

top_100_songs_uri = [song.split(":")[2] for song in top_100_songs_uri]

playlist = sp.user_playlist_create(user=user_id,
                                   name=f"{date} Billboard 100",
                                   public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=top_100_songs_uri)
