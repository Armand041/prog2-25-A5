"""
Módulo de excepciones personalizadas para la gestión de artistas

Este módulo contiene el error ArtistaNoEncontrado para manejar los casos en los que no se encuentra
al artista en la base de datos local.

Clases:
 ArtistaNoEncontrado: Excepción personalizada para artistas no encontrados
"""

class ArtistaNoEncontrado(Exception):
    """
    Excepción personalizada para indicar que el artista no se ha encontrado en la base de datos local.

    Atributos:
    --------------
    artista: str
        Nombre del artista que se intentó buscar

    Metodos:
    --------------
    __init__(self, artista : str) -> None:
        Inicializa la excepción con el nombre del artista no encontrado
    """

    def __init__(self, artista : str) -> None:
        """
        Inicializa la excepción con un mensaje que incluye al artista que se intentó encontrar.

        Parámetros:
        --------------------
        artista: str
            Nombre del artista del que se intentó encontrar en la base de datos local.
        """

        super().__init__(
            f'El artista {artista} no se encuentra en la base de datos local')