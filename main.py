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
    json_result = json.loads(result.content)["tracks"]["items"][0]["track"]["name"]#["album"]["artists"][0]["name"]
    return json_result

token = get_token() 
result = search_for_artist(token, "Drake")
artist_id = result["id"]
songs = get_songs_by_artist(token, artist_id)

playlist_id = "7tX0z34vWjjcpOj1IFlS3w?si=82d938eca9ac40fb"

print(get_playlist_items(token, playlist_id))

#for idx, song in enumerate(songs):
#    print(f"{idx + 1}. {song['name']}")

[{'added_at': '2023-08-13T15:09:15Z', 'added_by': {'external_urls': {'spotify': 'https://open.spotify.com/user/31mdf2d3qnqfxpfijdu76bh4pea4'}, 'href': 'https://api.spotify.com/v1/users/31mdf2d3qnqfxpfijdu76bh4pea4', 'id': '31mdf2d3qnqfxpfijdu76bh4pea4', 'type': 'user', 'uri': 'spotify:user:31mdf2d3qnqfxpfijdu76bh4pea4'}, 'is_local': False, 'primary_color': None, 'track': {'album': {'album_type': 'single', 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6Ip8FS7vWT1uKkJSweANQK'}, 'href': 'https://api.spotify.com/v1/artists/6Ip8FS7vWT1uKkJSweANQK', 'id': '6Ip8FS7vWT1uKkJSweANQK', 'name': 'Dave', 'type': 'artist', 'uri': 'spotify:artist:6Ip8FS7vWT1uKkJSweANQK'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5H4yInM5zmHqpKIoMNAx4r'}, 'href': 'https://api.spotify.com/v1/artists/5H4yInM5zmHqpKIoMNAx4r', 'id': '5H4yInM5zmHqpKIoMNAx4r', 'name': 'Central Cee', 'type': 'artist', 'uri': 'spotify:artist:5H4yInM5zmHqpKIoMNAx4r'}], 'available_markets': ['AD', 'AE', 'AG', 'AL', 'AM', 'AO', 'AR', 'AT', 'AU', 'AZ', 'BA', 'BB', 'BD', 'BE', 'BF', 'BG', 'BH', 'BI', 'BJ', 'BN', 'BO', 'BR', 'BS', 'BT', 'BW', 'BZ', 'CA', 'CD', 'CG', 'CH', 'CI', 'CL', 'CM', 'CO', 'CR', 'CV', 'CW', 'CY', 'CZ', 'DE', 'DJ', 'DK', 'DM', 'DO', 'DZ', 'EC', 'EE', 'EG', 'ES', 'ET', 'FI', 'FJ', 'FM', 'FR', 'GA', 'GB', 'GD', 'GE', 'GH', 'GM', 'GN', 'GQ', 'GR', 'GT', 'GW', 'GY', 'HK', 'HN', 'HR', 'HT', 'HU', 'ID', 'IE', 'IL', 'IN', 'IQ', 'IS', 'IT', 'JM', 'JO', 'JP', 'KE', 'KG', 'KH', 'KI', 'KM', 'KN', 'KR', 'KW', 'KZ', 'LA', 'LB', 'LC', 'LI', 'LK', 'LR', 'LS', 'LT', 'LU', 'LV', 'LY', 'MA', 'MC', 'MD', 'ME', 'MG', 'MH', 'MK', 'ML', 'MN', 'MO', 'MR', 'MT', 'MU', 'MV', 'MW', 'MX', 'MY', 'MZ', 'NA', 'NE', 'NG', 'NI', 'NL', 'NO', 'NP', 'NR', 'NZ', 'OM', 'PA', 'PE', 'PG', 'PH', 'PK', 'PL', 'PS', 'PT', 'PW', 'PY', 'QA', 'RO', 'RS', 'RW', 'SA', 'SB', 'SC', 'SE', 'SG', 'SI', 'SK', 'SL', 'SM', 'SN', 'SR', 'ST', 'SV', 'SZ', 'TD', 'TG', 'TH', 'TJ', 'TL', 'TN', 'TO', 'TR', 'TT', 'TV', 'TW', 'TZ', 'UA', 'UG', 'US', 'UY', 'UZ', 'VC', 'VE', 'VN', 'VU', 'WS', 'XK', 'ZA', 'ZM', 'ZW'], 'external_urls': {'spotify': 'https://open.spotify.com/album/5l0QlaI3wdZpE7ggoO5Rwg'}, 'href': 'https://api.spotify.com/v1/albums/5l0QlaI3wdZpE7ggoO5Rwg', 'id': '5l0QlaI3wdZpE7ggoO5Rwg', 'images': [{'height': 640, 'url': 'https://i.scdn.co/image/ab67616d0000b273e3a09a9ae3f1fa102c110e60', 'width': 640}, {'height': 300, 'url': 'https://i.scdn.co/image/ab67616d00001e02e3a09a9ae3f1fa102c110e60', 'width': 300}, {'height': 64, 'url': 'https://i.scdn.co/image/ab67616d00004851e3a09a9ae3f1fa102c110e60', 'width': 64}], 'name': 'Sprinter', 'release_date': '2023-06-01', 'release_date_precision': 'day', 'total_tracks': 1, 'type': 'album', 'uri': 'spotify:album:5l0QlaI3wdZpE7ggoO5Rwg'}, 'artists': [{'external_urls': {'spotify': 'https://open.spotify.com/artist/6Ip8FS7vWT1uKkJSweANQK'}, 'href': 'https://api.spotify.com/v1/artists/6Ip8FS7vWT1uKkJSweANQK', 'id': '6Ip8FS7vWT1uKkJSweANQK', 'name': 'Dave', 'type': 'artist', 'uri': 'spotify:artist:6Ip8FS7vWT1uKkJSweANQK'}, {'external_urls': {'spotify': 'https://open.spotify.com/artist/5H4yInM5zmHqpKIoMNAx4r'}, 'href': 'https://api.spotify.com/v1/artists/5H4yInM5zmHqpKIoMNAx4r', 'id': '5H4yInM5zmHqpKIoMNAx4r', 'name': 'Central Cee', 'type': 'artist', 'uri': 'spotify:artist:5H4yInM5zmHqpKIoMNAx4r'}], 'available_markets': ['AR', 'AU', 'AT', 'BE', 'BO', 'BR', 'BG', 'CA', 'CL', 'CO', 'CR', 'CY', 'CZ', 'DK', 'DO', 'DE', 'EC', 'EE', 'SV', 'FI', 'FR', 'GR', 'GT', 'HN', 'HK', 'HU', 'IS', 'IE', 'IT', 'LV', 'LT', 'LU', 'MY', 'MT', 'MX', 'NL', 'NZ', 'NI', 'NO', 'PA', 'PY', 'PE', 'PH', 'PL', 'PT', 'SG', 'SK', 'ES', 'SE', 'CH', 'TW', 'TR', 'UY', 'US', 'GB', 'AD', 'LI', 'MC', 'ID', 'JP', 'TH', 'VN', 'RO', 'IL', 'ZA', 'SA', 'AE', 'BH', 'QA', 'OM', 'KW', 'EG', 'MA', 'DZ', 'TN', 'LB', 'JO', 'PS', 'IN', 'KZ', 'MD', 'UA', 'AL', 'BA', 'HR', 'ME', 'MK', 'RS', 'SI', 'KR', 'BD', 'PK', 'LK', 'GH', 'KE', 'NG', 'TZ', 'UG', 'AG', 'AM', 'BS', 'BB', 'BZ', 'BT', 'BW', 'BF', 'CV', 'CW', 'DM', 'FJ', 'GM', 'GE', 'GD', 'GW', 'GY', 'HT', 'JM', 'KI', 'LS', 'LR', 'MW', 'MV', 'ML', 'MH', 'FM', 'NA', 'NR', 'NE', 'PW', 'PG', 'WS', 'SM', 'ST', 'SN', 'SC', 'SL', 'SB', 'KN', 'LC', 'VC', 'SR', 'TL', 'TO', 'TT', 'TV', 'VU', 'AZ', 'BN', 'BI', 'KH', 'CM', 'TD', 'KM', 'GQ', 'SZ', 'GA', 'GN', 'KG', 'LA', 'MO', 'MR', 'MN', 'NP', 'RW', 'TG', 'UZ', 'ZW', 'BJ', 'MG', 'MU', 'MZ', 'AO', 'CI', 'DJ', 'ZM', 'CD', 'CG', 'IQ', 'LY', 'TJ', 'VE', 'ET', 'XK'], 'disc_number': 1, 'duration_ms': 229133, 'episode': False, 'explicit': True, 'external_ids': {'isrc': 'GBUM72305159'}, 'external_urls': {'spotify': 'https://open.spotify.com/track/2FDTHlrBguDzQkp7PVj16Q'}, 'href': 'https://api.spotify.com/v1/tracks/2FDTHlrBguDzQkp7PVj16Q', 'id': '2FDTHlrBguDzQkp7PVj16Q', 'is_local': False, 'name': 'Sprinter', 'popularity': 96, 'preview_url': None, 'track': True, 'track_number': 1, 'type': 'track', 'uri': 'spotify:track:2FDTHlrBguDzQkp7PVj16Q'}, 'video_thumbnail': {'url': None}}]
