#!/usr/bin/env python
# coding: utf-8

# # Spotify - Spotipy
# 

# In[ ]:


# Install Spotipy
get_ipython().system('pip install spotipy')


# In[ ]:


# Import and Set Up Spotipy
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = 'XXXXXXXXXX' # Insert your client id
client_secret = 'XXXXXXXXXX' # Insert your client secret id here

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


# In[ ]:


# Get artist

# Bruce Springsteen
#artist_uri = 'spotify:artist:3eqjTLE0HfPfh78zjh6TqT'

# Kim Larsen
artist_uri = 'spotify:artist:2ZQifdPOptKHxTaYTLh0BC'


# In[ ]:


# List albums
results = sp.artist_albums(artist_uri, album_type='album')

albums = results['items']
while results['next']:
    results = sp.next(results)
    albums.extend(results['items'])

for album in albums:
    print(album['name'])


# In[ ]:


# Top 10 tracks
results = sp.artist_top_tracks(artist_uri)

for track in results['tracks']:
    print(track['name'])


# In[ ]:


# 100 New releases
results = sp.new_releases()

while results:
    albums = results['albums']
    for i, item in enumerate(albums['items']):
        print(albums['offset'] + i, item['name'])

    if albums['next']:
        results = sp.next(albums)
    else:
        results = None


# In[ ]:




