import click
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

print('Welcome to spotifier ver 1.0, This project will help you find Spotify song'
      'suggestions! Please do the following below:')


@click.command()
@click.option(
    "--cid",
    # prompt="Enter your cid",
    # hide_input=False,
    # confirmation_prompt=False,
    help='CID can be found at Spotify Dashboard'
)
@click.option(
    "--secret",
    # prompt="Enter your secret",
    # hide_input=False,
    # confirmation_prompt=False,
    help='Secret can be found at Spotify Dashboard'
)
def cli(cid, secret):
    sp = spotify_login(cid, secret)
    click.echo("This command will guide you through finding your songs recommendation.")
    seeds_artists = []
    seeds_tracks = []
    seeds_genres = []

    if click.confirm("Would you like to define artist seeds?"):
        click.echo("""\
        You can specify an artist in following forms:
          - A artist name (Metalica)
          - A artist URL (Example here)
          - A artist Spotify ID (EXAMPLE HERE)"""
        )

        artist = click.prompt("Search for an artist (or leave blank to continue)", default="", type=str)

        while artist:
            result = get_artist(sp, artist)
            seeds_artists.append(result)
            artist = click.prompt("Search for an artist", default="", type=str)

    if click.confirm("Would you like to define track seeds?"):
        click.echo("""\
        You can specify an artist in following forms:
          - A track name (Careless whisper)
          - A track URL (Example here)
          - A track Spotify ID (EXAMPLE HERE)"""
        )

        track = click.prompt("Search for an track (or leave blank to continue)", default="", type=str)

        while track:
            result = get_track(sp, track)
            seeds_tracks.append(result)
            track = click.prompt("Search for a track", default="", type=str)

    if click.confirm("Would you like to define genre seeds?"):
        available_genres = sp.recommendation_genre_seeds()["genres"]
        genres_numered = [f"[{i}] {x}" for i, x in enumerate(available_genres)]
        click.echo(f"Available genres:\n{genres_numered}")

        genre = click.prompt("Enter genre # to add:", default="", type=str)

        while genre != "":
            seeds_genres.append(available_genres[int(genre)])
            genre = click.prompt("Enter genre # to add:", default="", type=str)

    click.echo("DEBUG INFO")
    click.echo("Seeds artists:")
    click.echo(seeds_artists)
    click.echo("Seeds tracks:")
    click.echo(seeds_tracks)
    click.echo("Seeds genres:")
    click.echo(seeds_genres)
    click.echo()
    recommendations = get_recommendations(sp, seeds_artists, seeds_tracks, seeds_genres)
    print("DO SOMETHING WITH RECOMMENDATIONS")


def is_url(url):
    return True


def spotify_login(cid, secret):
    client = SpotifyClientCredentials(client_id=cid, client_secret=secret)
    return spotipy.Spotify(client_credentials_manager=client)


def get_track(spotify, track):
    print("IMPLEMENT GET TRACK HERE!!!!")
    return track


def get_artist(spotify, artist):
    print("IMPLEMENT GET ARTIST HERE!!!!")
    return artist


def get_recommendations(spotify, seeds_artists, seeds_tracks, seeds_genres):
    print("Call get_recommendations with collected seeds here!!!")
    return ["IMPLEMENT THIS SHIT"]
