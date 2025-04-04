from staff import Staff
from typing import List
from cancion_no_encontrada_error import CancionNoEncontrada
from cancion_ya_existe_error import CancionYaExiste

class Artista(Staff):
    """
    Clase Artista
        Trabajadores del festival que actúan en el escenario

    Atributos:
    -------------
    edad: int
            Edad del arista
        nombre: str
            Nombre del arista
        dni: str
            Dni del arista
        sueldo: float
            Sueldo por hora del arista
        horario: str
            Horario en el que trabaja el arista
        canciones_populares: List[str]
            Canciones más populares del artista

    Metodos:
    -------------
    __init__(self, edad : int, nombre: str, dni: str, sueldo: float, horario: str ) -> None:
        Constructor del objeto, llamará a la clase Staff para sus atributos comunes.

    anyadir_cancion(self, nueva_cancion: str) -> None :
        Añade una canción a la lista de canciones populares del artista.

    eliminar_cancion(self, cancion: str) -> None :
        Elimina una de las canciones de la lista de canciones populares del artista.
    """

    def __init__(self, edad: int, nombre: str, dni: str, sueldo: float, horario: str, canciones_populares: List[str]) -> None:
        """
        Metodo constructor

        Parámetros:
        -----------------
        edad: int
            Edad del artista
        nombre: str
            Nombre del artista
        dni: str
            Dni del artista
        sueldo: float
            Sueldo por hora del artista
        horario: str
            Horario en el que trabaja el artista, debe ser hora_inicio-hora_fin, por ejemplo: 9:00-5:00
        canciones_populares: List[str]
            Lista con las canciones populares del artista
        """
        super().__init__(edad, nombre, dni, sueldo, horario)
        self.__canciones_populares=canciones_populares


    def anyadir_cancion(self, nueva_cancion: str) -> None :
        """
        Añade una canción a la lista de canciones populares del artista si esta no pertenece a la lista

        Parámetros:
        --------------
        nueva_cancion: str
            Canción que se desea añadir a la lista de canciones populares
        """
        if nueva_cancion not in self.__canciones_populares:
            self.__canciones_populares.append(nueva_cancion)
        else:
            raise CancionYaExiste(nueva_cancion, self.nombre)

    def eliminar_cancion(self, cancion: str) -> None :
        """
        Elimina una de las canciones de la lista de canciones populares del artista solo si esta se encuentra en la lista,
        si no está elevará un error.

        Parámetros:
        --------------
        cancion: str
            Canción que se desea eliminar de la lista de canciones populares
        """
        if cancion in self.__canciones_populares:
            self.__canciones_populares.remove(cancion)
        else:
            raise CancionNoEncontrada(cancion, self.nombre)