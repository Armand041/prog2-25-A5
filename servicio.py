from abc import ABC, abstractmethod

from Personal.staff import Staff


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
        self.trabajadores = trabajadores


    def contratar_trabajador(self, trabajador):
        """
        Método que añade trabajadores a la lista Trabajadores si queremos contratar a alguien
        """
        trabajador.cambiar_puesto(self.nombre)

        self.trabajadores.append(trabajador)

 #   def despedir_trabajadores(self, trabajador):
    def despedir_trabajadores(self, dni_trabajador: str):

        """
        Método que elimina los trabajadores de la lista Trabajadores en el caso en el que queramos despedir a alguien
        """

        for trabajador in self.trabajadores:
            if trabajador.dni == dni_trabajador:
                trabajador.cambiar_puesto("")
                self.trabajadores.remove(trabajador)
                print(f"El trabajador con DNI {dni_trabajador} ha sido despedido.")
                return
        print(f"No se encontró al trabajador con el DNI {dni_trabajador}.")

    @abstractmethod
    def obtener_informacion(self):
        pass

    def __str__(self):
        informacion = f'Horario: {self.horario}, Alquiler: {self.alquiler}, Lugar: {self.lugar}, Trabajadores: '
        for trabajador in self.trabajadores:
            informacion += f'{trabajador}\n'

        return informacion


class Comida(Servicio):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        super().__init__(nombre, horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        menu_comida = {'Hamburguesa ': 12, 'Perrito caliente': 8, '1 porción de pizza grande': 5, 'Patatas fritas': 5, 'Churros': 7, 'Helado': 3, 'Fruta con chocolate': 6}
        return f'Este puesto de comida ofrece: {menu_comida}'


class Bebida(Servicio):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        super().__init__(nombre, horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        bebidas_sin_alcohol = {'Fanta Naranja': 2.5, 'Fanta limon': 2.5, 'Cocacola': 2.7, 'Agua': 3}
        bebidas_con_alcohol = {'Mojito': 8, 'Cubata': 10, 'Tinto': 5, 'Cerveza': 4}
        return f'Este puesto de bebidas ofrece bebidas con alcohol: {bebidas_con_alcohol} y sin alcohol: {bebidas_sin_alcohol}'

class Tattoo(Servicio):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        super().__init__(nombre, horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        tattoo = {'Pequeño': 50, 'Mediano': 120, 'Grande': 300, 'Muy grande': 750}
        return f'Este puesto de tatuajes ofrece los siguientes precios dependiendo del tamaño: {tattoo}'

class Merch(Servicio):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        super().__init__(nombre, horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        merch = {'Camiseta': 25, 'Sudaderas': 40, 'Taza': 10, 'Pulsera': 5, 'Termo': 20}
        return f'Este puesto de merchandising ofrece: {merch}'

class SonidoLuces(Servicio):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        super().__init__(nombre, horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        return 'Este puesto no ofrece ningún prodcuto al público si no que consta de una serie de trabajadores que gestionan las luces y el sonido empleado en el festival controlandoq que todo funcione correctamente'

class EntradasSeguridad(Servicio):
    def __init__(self, nombre: str, horario: str, alquiler: float, lugar: str, trabajadores: list[Staff]):
        super().__init__(nombre, horario, alquiler, lugar, trabajadores)

    def obtener_informacion(self):
        return 'Este puesto no ofrece ningún prodcuto al público si no que una serie de trabajadores se encargan de controlar las entradas del recinto'
