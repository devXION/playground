import spotipy

from spotipy.oauth2 import SpotifyClientCredentials


cid = '4a109a342a864e30b2f1e8295668c6e1'
secret = '740d2e2bb4ee4b3792204b956a5f6748'
client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
playlist_link = 'https://open.spotify.com/playlist/2M2ERqBl2vRKEV1Hc23Poc?si=0535071291624040'playlist_URI = playlist_link.split("/")[-1].split("?")[0]
track_uris = [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]

for track in sp.playlist_tracks(playlist_URI)["items"]:
    track_uri = track["track"]["uri"]
    track_name = track["track"]["name"]
    artist_uri = track["track"]["artists"][0]["uri"]
    artist_info = sp.artist(artist_uri)
    artist_name = track["track"]["artists"][0]["name"]
    artist_pop = artist_info["popularity"]
    artist_genres = artist_info["genres"]
    album = track["track"]["album"]["name"]
    track_pop = track["track"]["popularity"]
    print(track_name,'[', album, ']')
