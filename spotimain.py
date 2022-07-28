import click
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


@click.command()
@click.password_option('--cid', prompt='your cid', hide_input=False, confirmation_prompt=False)
@click.password_option('--secret', prompt='your secret', hide_input=False, confirmation_prompt=False)
@click.password_option('--playlink', prompt='playlist link', required=True,hide_input=False, confirmation_prompt=False )
@click.option('--stat', type=click.Choice(['track name', 'artist name', 'album']), prompt='')
def credits(cid, secret, playlink, stat):
    click.echo(f'credentials have been entered')
    client = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client)
    playlist_URI = playlink.split("/")[-1].split("?")[0]
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        [x["track"]["uri"] for x in sp.playlist_tracks(playlist_URI)["items"]]
        track_name = track["track"]["name"]
        artist_name = track["track"]["artists"][0]["name"]
        album = track["track"]["album"]["name"]
        if stat == 'track name':
            print(track_name)
        if stat == 'artist name':
            print(artist_name)
        if stat == 'album':
            print(album)



if __name__ == '__main__':
    credits()
