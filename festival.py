"""
Clase festival.
Podrá crear y eliminar festivales, a la vez que añadir, modificar o eliminar información
respecto a estos.


ATRIBUTOS
--------
nombre: Nombre del festival
fecha: Fecha de realización del festival
lugar: Lugar donde transcurre el festival
aforo: Aforo máximo permitido
coste: Coste total del festival
permisos: Lista de los permisos legales que tiene el festival
aforo_libre: Aforo disponible actualmente
asistentes: Lista con los asistentes al festival
servicios: Lista de servicios que ofrece el festival
MÉTODOS
-------
anyadir_permisos(): Añade permisos al festival

"""""

from typing import List




class Festival:



    def __init__(self, nombre: str, fecha: str, lugar: str, aforo: int, coste: float, permisos: List[str]):
        self._nombre = nombre
        self._fecha = fecha
        self._lugar = lugar
        self.__aforo = aforo
        self.__coste = coste
        self.__permisos = permisos
        self.__aforo_libre = aforo
        self.asistentes = []
        self.servicios = []


    def anyadir_persona(self, persona: object):
        """
        
        Añadimos una nueva persona del público al festival
        Parametros
        ---------
        persona: Un objeto de la clase Publico
        
        Retorna: None en caso de haber aforo libre

        """
        if self.__aforo_libre >0:
            self.__aforo_libre -=1
            self.asistentes.append(persona)
        else:
            return f'No hay aforo libre'



    def anyadir_permisos(self, nuevo_permiso: str) -> None:
        """
        Añadir nuevos permisos al festival
        Parametros
        ---------
        nuevo_permiso: permiso que se va a añadir a los actuales

        Retorna: None
        """
        self.__permisos += nuevo_permiso

    def anyadir_servicio(self, servicio: object) -> None:
        """
        Añade un nuevo servicio a la lista servicio

        """
        self.servicios.append(servicio)

    def __str__(self):
        return f'Nombre: {self._nombre}, Fecha: {self._fecha}, Lugar: {self._lugar}'

    def mostrar_publico(self):
        """
        Muestra el público que asiste al festival

        """
        return f'Asistentes del Festival {self.__class__.__name__}: {self.asistentes}'

    def mostrar_servicios(self):
        """
        Muestra el público que asiste al festival

        """
        return f' Servicios del Festival {self.__class__.__name__}: {self.servicios}'