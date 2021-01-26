import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secret import client_id, client_secret, redirect_uri, weely_playlist_id, all_playlist_id

scope = 'playlist-read-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

results = sp.playlist_items(
    playlist_id=weely_playlist_id)
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['name'], " - ", track['artists'][0]['name'])
