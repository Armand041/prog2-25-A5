from staff import Staff
from spotify_api import InformacionArtista
from artista_no_encontrado_error import ArtistaNoEncontrado
from cancion_no_encontrada_error import CancionNoEncontrada
from cancion_ya_existe_error import CancionYaExiste

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
            Puesto de trabajo del artista
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
        apellido1: str
            Primer apellido del artista
        apellido2: str
            Segundo apellido (si tiene) del artista. Si carece de él será None
        sueldo: float
            Sueldo por hora del artista
        horario: str
            Horario en el que trabaja el artista, debe ser hora_inicio-hora_fin, por ejemplo: 9:00-5:00
        puesto_trabajo: object
            Puesto de trabajo del artista es ser artista, por lo que tomará siempre el objeto Artista.
        canciones_populares: List[str]
            Lista con las canciones populares del artista
        """
        puesto_trabajo = type(self)
        apellido1 = None
        super().__init__(fecha_nacimiento, dni, nombre, sueldo, horario, puesto_trabajo, apellido1, apellido2)

        try:
            self.__informacion = InformacionArtista(nombre)
        except ArtistaNoEncontrado:
            print(f"El artista {nombre} no se encuentra en la base de datos. \nRevise ortografía y asegurese de colocar el nombre que aparece en Spotify en el parámetro 'nombre'")
        else:
            top10 = self.__informacion.canciones_top()
            canciones_populares = []
            for cancion in top10:
                canciones_populares.append(cancion['Track'])
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
            raise CancionYaExiste(nueva_cancion, self._nombre)

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
            raise CancionNoEncontrada(cancion, self._nombre)


coso = Artista('a', 'b', 'Coso Sheldrake', 13.5, 'c')
print('ERROR')

cosmo = Artista('a', 'b', 'Cosmo Sheldrake', 13.5, 'c')
print('\nTodo Cahchi')