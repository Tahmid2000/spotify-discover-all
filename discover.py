import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secret import client_id, client_secret, redirect_uri, weely_playlist_id, all_playlist_id

""" scope = 'playlist-read-private' """
scope = 'playlist-modify-private'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

results = sp.playlist_items(
    playlist_id=weely_playlist_id)
to_add = []
for item in (results['items']):
    track = item['track']
    to_add.append(track['uri'])
sp.playlist_add_items(playlist_id=all_playlist_id, items=to_add)
