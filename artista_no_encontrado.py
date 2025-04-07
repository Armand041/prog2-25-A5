"""
Módulo de excepciones personalizadas para la gestión de artistas

Este módulo contiene el error CancionNoEncontrada para manejar los casos en los que no se encuentra
una canción del artista al intentar eliminarla.

Clases:
 CancionNoEncontrada: Excepción personalizada para canciones no encontradas
"""

class ArtistaNoEncontrado(Exception):
    """
    Excepción personalizada para indicar que una canción no existe.

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
        canción no encontrada.
    """

    def __init__(self, artista : str) -> None:
        """
        Inicializa la excepción con un mensaje que incluye la canción que se intentó eliminar
        y el artista del que se intentó eliminar la canción.

        Parámetros:
        --------------------
        cancion: str
            Nombre de la canción que se intenta eliminar

        artista: str
            Nombre del artista del que se intentó eliminar la canción
        """

        super().__init__(
            f'El artista {artista} no se encuentra en la base de datos local')