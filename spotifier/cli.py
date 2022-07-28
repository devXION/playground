import click
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


@click.command()
@click.password_option('--cid', prompt='your cid', hide_input=False, confirmation_prompt=False)
@click.password_option('--secret', prompt='your secret', hide_input=False, confirmation_prompt=False)
@click.password_option('--playlink', prompt='playlist link', required=True,hide_input=False, confirmation_prompt=False )
@click.option('--stat', type=click.Choice(['track name', 'artist name', 'album']), prompt='')
def cli(cid, secret, playlink, stat):
    click.echo(f'credentials have been entered')
    client = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    sp = spotipy.Spotify(client_credentials_manager=client)
    playlist_URI = playlink.split("/")[-1].split("?")[0]
    for track in sp.playlist_tracks(playlist_URI)["items"]:
        if stat == 'track name':
            print(track["track"]["name"])
        if stat == 'artist name':
            print(track["track"]["artists"][0]["name"])
        if stat == 'album':
            print(track["track"]["album"]["name"])
