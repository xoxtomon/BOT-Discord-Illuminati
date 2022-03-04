import os
from datetime import datetime
import requests
import json
import random

my_secret = os.environ['lyrics']
base_url = 'https://api.musixmatch.com/ws/1.1/'
anuel_AA_id = 28849527

def get_quote():
  #random_track = 
  """response = requests.get(
    base_url + 'artist.search?q_artist=Anuel-A-A&page_size=5&apikey='+my_secret
  )"""
  response = requests.get(
    f'{base_url}track.search?f_artist_id={anuel_AA_id}&page_size=100&page=1&s_track_rating=desc&apikey={my_secret}'
  )

  response_serialized = response.json()

  if response_serialized["message"]["header"]["status_code"] != 200:
    return False
  
  all_tracks = response_serialized['message']['body']['track_list']
  num_of_tracks = len(all_tracks)

  rand_song_pos = random.randint(1,num_of_tracks)
  rand_song_common = all_tracks[rand_song_pos]['track']
  rand_song_id = rand_song_common['track_id']
  rand_song_name = rand_song_common['track_name']

  rand_song_snippet = requests.get(
    f"{base_url}track.snippet.get?track_id={rand_song_id}&apikey={my_secret}"
  )
  snippet_body = rand_song_snippet.json()["message"]["body"]["snippet"]["snippet_body"]

  return (snippet_body, rand_song_name)


def calc_breakup():
  breakup = datetime(2021, 7, 2, 0, 0, 0)
  today = datetime.now()

  elapsed = today - breakup

  return(elapsed.days)
