"""
Módulo de excepciones personalizadas para la gestión de artistas

Este módulo contiene el error CancionYaExiste para manejar los casos en los que se intenta
anyadir una canción ya existente a la lista de canciones d eun artista.

Clases:
 -
"""

class CancionYaExiste(Exception):
    """
    Excepción personalizada para indicar que una canción ya existe.

    Atributos:
    --------------
    cancion: str
        Nombre de la canción que se quería eliminar

    artista: str
        Nombre del artista que se intentó modificar

    Metodos:
    --------------
    __init__(self, cancion : str, artista : str) -> None:
        Inicializa la excepción con el nombre del artista afectado y el nombre de la
        canción ya existente.
    """

    def __init__(self, cancion : str, artista : str) -> None:
        """
        Inicializa la excepción con un mensaje que incluye la canción que se intentó añadir
        y el artista al que se le intentó anyadir la canción.

        Parámetros:
        --------------------
        cancion: str
            Nombre de la canción que se intenta anyadir.

        artista: str
            Nombre del artista al que se intentó anyadir la cancion.
        """

        super().__init__(
            f'La canción {cancion} ya se encuentra en la lista de canciones del artista {artista}')