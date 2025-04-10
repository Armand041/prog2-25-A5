import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from artista_no_encontrado_error import ArtistaNoEncontrado
from typing import List


class InformacionArtista:
    """
    Clase InformacionArtista
        Se conecta a la API de spotify mediante la biblioteca spotipy para recabar informacion
        de artistas.

    Atributos:
    ------------
    Clase:
        artistas: dict
            Base de datos donde se guardarán los ID de spotify de cada artista siendo el nombre de este
            (usando el que aparece en spotify) como clave.
        spotify: object
            Objeto que conecta, via credenciales propias, con spotify para recuperar información
    Instancia:
        artista: str
            Nombre del artista que se buscará en el diccionario artistas
        id: str
            ID del artista que se ha buscado
        uri: str
            uri del artista que se ha buscado, derivada de id

    Metodos:
    ------------
        __init__(self, artista: str) -> None:
            Constructor del objeto
        albumes(self) -> list[dict]:
            Devolverá una lista de los álbumes publicados por el artista, junto links a estos.
        canciones_top(self) -> list[dict]:
            Devolverá una lista de las 10 canciones más populares del artista, junto links a estas
        link_artista(self) -> str
            Devolverá el link a la página de spotify del artista
    """

    ##### HAY QUE HACER QUE EL DICCIONARIO SE CREE A PARTIR DE UN CSV #####
    __artistas = {'Cosmo Sheldrake': '6hV6oxGLeLFw17DGjIPkYD'}
    __spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials('13806cf7187b4de487777fe679d594e8','c338bbe63d1345e98770e217ab055b61'))

    def __init__(self, artista: str) -> None:
        """
        Metodo constructor

        Parámetros:
        -------------
        artista: str
            Nombre de spotify del artista a buscar en el diccionario artistas
            Si no se encuentra eleva el error ArtistaNoEncontrado

        Otros atributos creados en el constructor:
        -------------------------------------------
        id: str
            Es la ID de spotify del artista que hemos buscado. Se recoge del diccionario
            artistas que funciona como una base de datos local
        uri: str
            String general que sumado a la id del artista nos permitirá acceder al contenido
            de ese artista.
        """
        if artista not in type(self).__artistas:
            raise ArtistaNoEncontrado(artista)
        else:
            self.__artista = artista
            self.__id = type(self).__artistas[self.__artista]
            self.__uri = f'spotify:artist:{self.__id}'

    def albumes(self) -> List[dict]:
        """
        Metodo que obtiene los álbumes del artista
        """

        # Extraemos los albumes del objeto de clase spotify
        resultados = type(self).__spotify.artist_albums(self.__uri, album_type='album')
        albumes = resultados['items']

        # Ampliamos albumes para contener todos los albumes si el artista cumple la condicion next
        while resultados['next']:
            print(resultados)
            print(resultados['next'])
            resultados = type(self).__spotify.next(resultados)
            albumes.extend(resultados['items'])

        # Creamos la lista que devolveremos en forma de lista de diccionarios
        result_album = []
        for album in albumes:
            result_album.append({'Album': album['name'], 'Link': album['external_urls']['spotify']})
        return result_album

    def canciones_top(self) -> list[dict]:
        """
        Metodo para obtener las 10 canciones más populares del artista
        """
        # Extraemos los datos a usar
        resultados = type(self).__spotify.artist_top_tracks(self.__uri)

        # Creamos la lista que devolveremos en forma de lista de diccionarios
        canciones = []
        for cancion in resultados['tracks']:
            canciones.append({'Track': cancion['name'], 'Link': cancion['external_urls']['spotify']})
        return canciones

    def link_artista(self) -> str:
        """
        Metodo para proporcionar el link a la página de spotify del artista
        """
        # Extraemos los datos del artista
        resultado = type(self).__spotify.artist(self.__id)

        return resultado['external_urls']['spotify']