import requests
import json

endpoint_url = 'https://api.spotify.com/v1/recommendations?'
access_token = "bsk134kakalkdf245"

#FILTERS
limit = 10 #number of songs
market = "AU" #country
seed_genres = "pop" #genres
target_danceability = 0.2
seed_artists = '06HL4z0CvFAxyc27GXpf02?si=_0xxqWK1RMm-QYK6TwApQg'

#QUERY FOR SONGS
query = f'{endpoint_url}limit={limit}&market={market}&seed_artists={seed_artists}&target_danceability={target_danceability}'

response = requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})

json_response = response.json()
for i,j in enumerate(json_response['tracks']):
            uris.append(j['uri'])
            print(f"{i+1}) \"{j['name']}\" by {j['artists'][0]['name']}")

response_genres =requests.get("https://api.spotify.com/v1/recommendations/available-genre-seeds",
               headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {access_token}"})
print(response_genres.json())