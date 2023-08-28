from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json

load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization" : "Basic " + auth_base64,
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization" : "Bearer " + token}

def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    headers = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"
    
    query_url = url + query
    result = get(query_url, headers=headers)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists")
        return None
    return json_result[0]

def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?country=US"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]
    return json_result

def get_playlist_items(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    headers = get_auth_header(token)
    result = get(url, headers=headers)
    json_result = json.loads(result.content)["tracks"]["items"]
    return json_result

token = get_token() 
result = search_for_artist(token, "Drake")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

playlist_id = "4Gkbj4A2Xke8mT8B5MKb4e?si=90d30b6a1c854115"
playlist = get_playlist_items(token, playlist_id)

artist_song_dict = {}

for track in playlist:
    if track['track']['artists'][0]['name'] in artist_song_dict:
        artist_song_dict[track['track']['artists'][0]['name']].append(track['track']['name'])
    else:
        artist_song_dict[track['track']['artists'][0]['name']] = [track['track']['name']]
print(artist_song_dict)

total_values = 0

for value in artist_song_dict.values():
    if isinstance(value, list):
        total_values += len(value)
    else:
        total_values += 1

print(total_values)