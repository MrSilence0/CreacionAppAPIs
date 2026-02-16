# services/streaming_api.py
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Pega aquí lo que obtengas del dashboard de Spotify
CLIENT_ID = "client_id_de_tu_aplicacion_spotify"
CLIENT_SECRET = "client_secret_de_tu_aplicacion_spotify"

def get_spotify_track(query):
    auth_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(auth_manager=auth_manager)
    
    # Buscamos la canción
    results = sp.search(q=query, limit=1, type='track')
    if results['tracks']['items']:
        return results['tracks']['items'][0]['id']
    return None