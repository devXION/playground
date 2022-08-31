import pprint

import click
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from spotipy.oauth2 import SpotifyOAuth

print('Welcome to spotifier ver 1.0, This project will help you find Spotify song'
      'suggestions! Please do the following below:')


@click.command()
@click.option(
    "--cid",
    prompt="Enter your cid",
    hide_input=False,
    confirmation_prompt=False,
    envvar="SPOTIFY_CID",
    help='CID can be found at Spotify Dashboard'
)
@click.option(
    "--secret",
    prompt="Enter your secret",
    hide_input=False,
    confirmation_prompt=False,
    envvar="SPOTIFY_SECRET",
    help='Secret can be found at Spotify Dashboard'
)
def cli(cid, secret):
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=cid,
                                                   client_secret=secret,
                                                   redirect_uri='http://example.com/callback/',
                                                   scope='playlist-read-private,playlist-modify-public'))

    click.echo("This command will guide you through finding your songs recommendation.")
    seeds_artists = []
    seeds_tracks = []
    seeds_genres = []

    if click.confirm("Search for an artist?"):
        click.echo('Search artists name: ')



        artist = click.prompt("(or leave blank to continue)", default="", type=str)

        while artist:
            result = get_artist(sp, artist)
            for i in result['artists']['items']:
                seeds_artists.append(i['id'])
                artist = click.prompt("Search for an artist", default="", type=str)
                break

    if click.confirm("Would you like to search for a song?"):
        click.echo('search by name of the song: ')

        track = click.prompt("(or leave blank to continue)", default="", type=str)

        while track:
            result = get_track(sp, track)
            for i in result['tracks']['items']:
                seeds_tracks.append(i['id'])
                track = click.prompt("Search for a track", default="", type=str)
                break

    if click.confirm("Would you like to define genre?"):
        available_genres = sp.recommendation_genre_seeds()["genres"]
        genres_numered = [f"[{i}] {x}" for i, x in enumerate(available_genres)]
        click.echo(f"Available genres:")
        for entry in genres_numered:
            click.echo(f"{entry}")

        genre = click.prompt("Enter genre # to add:", default="", type=str)

        while genre != "":
            seeds_genres.append(available_genres[int(genre)])
            genre = click.prompt("Enter genre # to add:", default="", type=str)

    click.echo("DEBUG INFO")
    click.echo("Artists ID:")
    click.echo(seeds_artists)
    click.echo("Tracks ID:")
    click.echo(seeds_tracks)
    click.echo("Genres defined:")
    click.echo(seeds_genres)
    click.echo()
    get_recommendations(sp, a=seeds_artists, b=seeds_tracks, c=seeds_genres)


def get_track(spotify, track):
    results = spotify.search(q='track:' + track, type='track')
    for i in results['tracks']['items']:
        print((i['name']))
    return results


def get_artist(spotify, artist):
    results = spotify.search(q='artist:' + artist, type='artist')
    for i in results['artists']['items']:
        print(i['name'])

    return results


def get_recommendations(sp, a , b, c):

  recommendation = sp.recommendations(seed_artists=a,seed_tracks=b,
                            seed_genres=c, limit=100)

  songs=[]
  print('Recommended songs are listed below:')
  for i in recommendation['tracks']:
      print(f"[Song]: {i['name']} [Artist]: {i['album']['artists'][0]['name']}")
      songs.append(i['id'])
  if click.confirm('Would you like to add these songs to newly created playlist?'):
      click.prompt('what is your spotify nickname: ')
      nickname = sp.me()['id']
      playlist = sp.user_playlist_create(user=nickname, name='RECOMMENDATIONS')['id']
      sp.playlist_add_items(playlist_id=playlist,items=songs)




     


    


cli()
