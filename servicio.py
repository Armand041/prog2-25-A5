from abc import ABC, abstractmethod

from Personal.staff import Staff
#from Personal.staff import Staf


"""
Clase Servicio: incluye todos los servicios que ofrece el festival desde puestos de comida hasta puestos de merch

Sus atributos son los que salen en el método del constructor      
"""

class Servicio(ABC):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        """
        Metodo constructor

        Parámetros:
        -----------------
        nombre: str
            Es el nombre del puesto en el que trabaja cada lista de staff
         horario: str
            Horario de cada de puesto
        Alquiler: float
            Alquiler que paga cada puesto para estar en el festival
        Lugar dentro del recinto: str
            Ubicación de cada puesto en el festival
        Trabajadores: list
            Lista de staff que nos dice los trabajadores que trabajan en cada puesto con sus datos
        """
        self.nombre = nombre
        self.horario = horario
        self.alquiler = alquiler
        self.lugar = lugar
        # TODO: Cuando juntemos la clase Staff, utilizarla aqui
        self.trabajadores = trabajadores

    def contratar_trabajador(self, trabajador):
        """
        Método que añade trabajadores a la lista Trabjadores si queremos contratar a alguien
        """
        trabajador.cambiar_puesto(self.nombre)

        self.trabajadores.append(trabajador)

    def despedir_trabajadores(self, trabajador):
        """
        Método que elimina los trabajadrores de la lista Trabajadores en el caso en el que queramos despedir a alguien
        """
        for trabajador in self.trabajadores:
            if trabajador.dni == dni_trabajador:
                trabajador.cambiar_puesto("")  # Se vacía el puesto de trabajo
                self.trabajadores.remove(trabajador)  # Elimina al trabajador de la lista
                print(f"El trabajador con DNI {dni_trabajador} ha sido despedido y su puesto ha sido eliminado.")
                return  # Terminamos la función después de despedir al trabajador

            # Si no se encuentra el trabajador con ese DNI
        print(f"No se encontró al trabajador con el DNI {dni_trabajador}.")



    @abstractmethod
    def obtener_informacion(self):
        pass

    def __str__(self):
        return f'Horario: {self.horario}, Alquiler: {self.alquiler}, Lugar: {self.lugar}, Trabajadores: {self.trabajadores}'


class Comida(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str]):
        super().__init__(horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        menu_comida = {'Hamburguesa ': 12, 'Perrito caliente': 8, '1 porción de pizza grande': 5, 'Patatas fritas': 5, 'Churros': 7, 'Helado': 3, 'Fruta con chocolate': 6}
        return f'Este puesto de comida ofrece: {menu_comida}'


class Bebida(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str]):
        super().__init__(horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        bebidas_sin_alcohol = {}
        bebidas_con_alcohol = {}
        return f'Este puesto de bebidas ofrece bebidas con alcohol: {bebidas_con_alcohol} y sin alcohol: {bebidas_sin_alcohol}'

class Tatto(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str]):
        super().__init__(horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        tatto = {'Pequeño': 50, 'Mediano': 120, 'Grande': 300, 'Muy grande': 750}
        return f'Este puesto de tatuajes ofrece los siguientes precios dependiendo del tamaño: {tatto}'

class Merch(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str]):
        super().__init__(horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        merch = {'Camiseta': 25, 'Sudaderas': 40, 'Taza': 10, 'Pulsera': 5, 'Termo': 20}
        return f'Este puesto de merchandising ofrece: {merch}'

class SonidoLuces(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str]):
        super().__init__(horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        return 'Este puesto no ofrece ningún prodcuto al público si no que consta de una serie de trabajadores que gestionan las luces y el sonido empleado en el festival controlandoq que todo funcione correctamente'

class EntradasSeguridad(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str]):
        super().__init__(horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        return 'Este puesto no ofrece ningún prodcuto al público si no que una serie de trabajadores se encargan de controlar las entradas del recinto'


pepe = Staff('03-03-2000', '334535', )
servicio1 = Comida('horario', 4,5, 'lugar', )