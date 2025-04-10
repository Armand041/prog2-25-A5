from staff import Staff
from spotify_api import InformacionArtista



class Artista(Staff):
    """
    Clase Artista
        Trabajadores del festival que actúan en el escenario

    Atributos:
    -------------
        fecha_nacimiento: str
            Fecha de nacimiento del artista
        dni: str
            Dni del arista
        nombre: str
            Nombre del arista
        apellido1: str
            Primer apellido del artista
        apellido2: str
            Segundo apellido del artista
        sueldo: float
            Sueldo por hora del arista
        horario: str
            Horario en el que trabaja el arista
        puesto_trabajo: object
            Puesto de trabajo del artista (en este caso será Cantante, esa es su ocupación)
        canciones_populares: List[dict]
            Canciones más populares del artista y links a estas

    Metodos:
    -------------
    __init__(self, fecha_nacimiento: str, dni: str, nombre: str, sueldo: float, horario: str, apellido2: str = None) -> None:
        Constructor del objeto, llamará a la clase Staff para sus atributos comunes.

    mostrar_canciones_populares(self) -> None:
        Metodo que muestra las canciones populares de un artista y sus links a spotify.

    mostrar_albumes(self) -> None:
        Metodo que muestra los álbumes de un artista y sus links a spotify.

    mostrar_link_artista(self):
        Metodo que muestra el link que lleva a la página principal del artista en spotify.

    __str__(self) -> str:
        Metodo que muestra una cadena de texto con los principales datos de un artista.
    """

    def __init__(self, fecha_nacimiento: str, dni: str, nombre: str, sueldo: float, horario: str, apellido2: str = None) -> None:
        """
        Metodo constructor

        Parámetros:
        -----------------
        fecha_nacimiento: str
            Fecha de nacimiento del artista en el formato dd/mm/aaaa
        dni: str
            Dni del artista. Forma principal de identificación
        nombre: str
            Nombre del artista
        apellido2: str
            Segundo apellido (si tiene) del artista. Si carece de él será None
        sueldo: float
            Sueldo por hora del artista
        horario: str
            Horario en el que trabaja el artista, debe ser hora_inicio-hora_fin, por ejemplo: 9:00-5:00


        """
        puesto_trabajo = 'Cantante'
        apellido1 = ''

        super().__init__(fecha_nacimiento, dni, nombre, apellido1, sueldo, horario, puesto_trabajo, apellido2)

        self.__canciones_populares = InformacionArtista(self._nombre).canciones_top()

    def mostrar_canciones_populares(self) -> None:
        """
        Méetodo que muestra todas las canciones populares de un artista y sus respectivos links
        a spotify.
        """
        for cancion in self.__canciones_populares:
            print(f'Canción: {cancion['Track']}, Link a la canción -> {cancion['Link']}')

    def mostrar_albumes(self) -> None:
        """
        Metodo que obtiene los albumes de un artista mediante el uso de la API de spotify
        y muestra sus álbumes y sus respectivos links a spotify
        """
        albumes = InformacionArtista(self._nombre).albumes()
        for album in albumes:
            print(f'Álbum: {album['Album']}, Link al álbum -> {album['Link']}')

    def mostrar_link_artista(self):
        """
        Metodo que muestra por pantalla un link a la pagina de spotify del artista

        """
        link = InformacionArtista(self._nombre).link_artista()
        print(f'Página principal del artista en spotify -> {link}')

    def __str__(self) -> str:
        """
        Metodo que muestra los datos principales de un artista
        ----------------------
        :returns str
            Devuelve una cadena d etexto con los datos principales del artista.
        """
        return f'{self._nombre} es un {self._puesto_trabajo}, \nCobra {self._sueldo}€ la hora, y su horario es {self._horario}.'




