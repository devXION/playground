import click
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


@click.command()
@click.option('--cid', prompt='your cid')
@click.option('--secret', prompt='your secret')
def credits(cid, secret):
    click.echo(f'credentials have been entered')
    client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    playlist_link = 'https://open.spotify.com/playlist/2M2ERqBl2vRKEV1Hc23Poc?si=0535071291624040'
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
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
        print(track_name)

if __name__ == '__main__':
    credits()