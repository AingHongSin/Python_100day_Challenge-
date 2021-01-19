import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "ecadb538c66c4feab8e19103c2ef668f"

CLIENT_SECRET = "d852bd882481498abbd1d73899445889"


# date_input = input("Which year do you want to travel to? Type date in this format YYYY-MM-DD:")
#
# response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date_input}")
# contact = response.text
# soup = BeautifulSoup(contact, 'html.parser')
#
# all_title_music_Scraping_code = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')
# all_music_title = [music.getText() for music in all_title_music_Scraping_code]
# print(all_music_title)

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]