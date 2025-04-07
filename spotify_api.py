import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from artista_no_encontrado import ArtistaNoEncontrado


class InformacionArtista:
    __artistas = {'Cosmo Sheldrake': '6hV6oxGLeLFw17DGjIPkYD'}
    __spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials('13806cf7187b4de487777fe679d594e8','c338bbe63d1345e98770e217ab055b61'))

    def __init__(self, artista):
        if artista not in type(self).__artistas:
            raise ArtistaNoEncontrado(artista)
        else:
            self.__artista = artista
            self.__id = type(self).__artistas[self.__artista]
            self.__uri = f'spotify:artist:{self.__id}'

    def albumes(self):
        resultados = type(self).__spotify.artist_albums(self.__uri, album_type='album')
        albumes = resultados['items']
        while resultados['next']:
            resultados = type(self).__spotify.next(resultados)
            albumes.extend(resultados['items'])

        for i, album in enumerate(albumes):
            print(f"Album {i+1}: {album['name']}")
            print(f"Link: {album['external_urls']['spotify']}\n")

    def canciones_top(self):
        resultados = type(self).__spotify.artist_top_tracks(self.__uri)

        canciones = []
        for cancion in resultados['tracks']:
            canciones.append({'Track': cancion['name'], 'Link': cancion['external_urls']['spotify']})
        return canciones

cosmo = InformacionArtista('Cosmo Sheldrake')
cosmo.albumes()
print(cosmo.canciones_top())