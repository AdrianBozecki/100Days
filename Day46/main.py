from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

list_of_uris = []
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=CLIENT_ID,
        client_secret=SECRET_ID,
        show_dialog=True,
        cache_path="token.txt"
    )
)

user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
year=date.split("-")[0]

response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
soup = BeautifulSoup(response.text, "html.parser")


list_of_all_songs = [a.select("h3")[0].getText().replace("\t", "").replace("\n", "")
                     for a
                     in soup.find_all("div", class_="o-chart-results-list-row-container")]


for song in list_of_all_songs:
    result = sp.search(q=f"track:{song} year:{date}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        list_of_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't appear on Spotify. Skipped")


playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)

sp.playlist_add_items(playlist_id=playlist["id"], items=list_of_uris)