import spotipy
from spotipy.oauth2 import SpotifyOAuth
from secret import client_id, client_secret, redirect_uri, weely_playlist_id, all_playlist_id

# set scope
scope = 'playlist-modify-private'

# authenticate
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope))

# get songs from Discover Weekly
results = sp.playlist_items(
    playlist_id=weely_playlist_id)

# add song uris to a list
to_add = []
for item in (results['items']):
    track = item['track']
    to_add.append(track['uri'])

# add to custom playlist
sp.playlist_add_items(playlist_id=all_playlist_id, items=to_add)
