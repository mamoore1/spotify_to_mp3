# This file will hold the code that accesses the Spotify API and downloads the details of a given playlist

import requests

# As we are only looking to access playlists, and not user information, we only need the "Client Credentials" access flow
# Client ID and secret
CLIENT_ID = 'e4a8106fe976462a8e5138e5e6929716'
CLIENT_SECRET = 'e161215016dc458982a54fe5f13aa972'

# Authorisation url
AUTH_URL = 'https://accounts.spotify.com/api/token'

# Base URL of all Spotify API endpoints
BASE_URL = 'https://api.spotify.com/v1/'

# Post request to get a user access token
auth_response = requests.post(AUTH_URL,
                              {
                                  'grant_type': 'client_credentials',
                                  'client_id': CLIENT_ID,
                                  'client_secret': CLIENT_SECRET,
                              })

auth_response_data = auth_response.json()

access_token = auth_response_data['access_token']

headers = {
    'Authorization': f'Bearer {access_token}'
}

test_playlist = '3O6Sut8kEvi2k4XNuGjTXb'
payload = {'fields': 'tracks.items(track(name,artists(name)))'}

# Pull all song names and artists from a given playlist
songs = requests.get(BASE_URL + 'playlists/' + test_playlist,
                     headers=headers,
                     params=payload)

song_data = songs.json()

# Accessing the track names and artists
song_name_artist = song_data['tracks']['items']

# Turning the list of song data into a list of dictionaries with the format [artist_name: '', song_name: '']
# Initialise a list to hold artist and song data
artist_song_list = []
# Iterate through the list of track data
for track in song_name_artist:
    # Initialise a dictionary to hold the song and artist names
    artist_song_dict = {}
    # For each track, access the dictionary value containing the artist and song information
    artist_song_info = track['track']
    # Access the dictionary value holding the artist's name
    artist_name = artist_song_info['artists'][0]['name']
    # Add the artist's name to the dictionary
    artist_song_dict['artist_name'] = artist_name
    # Access the dictionary value holding the song name
    song_name = artist_song_info['name']
    # Add the song name to the dictionary
    artist_song_dict['song_name'] = song_name
    # Append the dictionary to the list
    artist_song_list.append(artist_song_dict)

print(artist_song_list)