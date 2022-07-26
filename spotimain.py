import click
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


@click.command()
@click.option('--cid', prompt='your cid')
@click.option('--secret', prompt='your secret')
@click.option('--playlink', prompt='playlist link')
@click.option('--stat', prompt='stat to display')
def credits(cid, secret, playlink,stat):
    click.echo(f'credentials have been entered')
    client = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client)
    playlist_link = playlink
    playlist_URI = playlist_link.split("/")[-1].split("?")[0]
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        album = track["track"]["album"]["name"]
        if stat == 'track name':
            print(track_name)
        if stat == 'artistname':
            print(artist_name)
        if stat == 'album':
            print(album)









if __name__ == '__main__':
    credits()
