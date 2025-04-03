from abc import ABC, abstractmethod

"""
Clase Servicio: incluye todos los servicios que ofrece el festival

Atributos:
    horario: str
         Horario de cada de puesto
    Alquiler: float
        Alquiler que paga cada puesto para estar en el festival
    Lugar dentro del recinto: str
        Ubicación de cada puesto en el festival
    Trabajadores: list
        Lista de los trabajadores de cada puesto
"""


# Si fuese una clase abtracta, podriamos hacer un metodo mas general sobre el servicio que ofrece cada puesto Y precio, horario??
# Dejamos los metodos de despedir y contrtar sin ser abstractos

class Servicio(ABC):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str], productos: dict[str, float]):
        self.horario = horario
        self.alquiler = alquiler
        self.lugar = lugar
        # TODO: Cuando juntemos la clase Staff, utilizarla aqui
        self.trabajadores = trabajadores
        self.productos = productos

    def contratar_trabajador(self, trabajador):
        """
        Método que añade trabajadores a la lista Trabjadores si queremos contratar a alguien
        """
        self.trabajadores.append(trabajador)

    def despedir_trabajadores(self, trabajador):
        """
        Método que elimina los trabajadrores de la lista Trabajadores en el caso en el que queramos despedir a alguien
        """
        if trabajador in self.trabajadores:
            self.trabajadores.remove(trabajador)
        return self.trabajadores

    @abstractmethod
    def obtener_informacion(self):
        pass

    def __str__(self):
        return f'Horario: {self.horario}, Alquiler: {self.alquiler}, Lugar: {self.lugar}, Trabajadores: {self.trabajadores}'


class T_Comida(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str], productos: dict[str, float]):
        super().__init__(horario, alquiler, lugar, trabajadores, productos)

    # No se que queremos de cad clase pero hice este de ejemplo

    def preparar_pedido(self, pedido):
        precio = 0
        for elemento in pedido:
            if elemento in self.productos:
                precio += self.productos[elemento]
            else:
                print('Ese producto no está a la venta')
        return precio

    # Si lo hiciese como una clase abstracta haría esto pero con el precio incluido, un diccionario objeto : precio

    def obtener_informacion(self):
        return 'Es un puesto de comida que ofrece: Patatas, Bocadillos, Perritos'


class T_Bebida(Servicio):
    def __init__(self, horario: str, alquiler: float, lugar: str, trabajadores: list[str], productos: dict[str, float]):
        super().__init__(horario, alquiler, lugar, trabajadores, productos)

    def obtener_informacion(self):
        return 'Es un puesto de bebidas que ofrece: Agua, Cerveza, Refrescos'

# class T_Tatto(Servicio):


# class T_Merch(Servicio):


# class T_Sonido(Servicio):


# class T_Entradas_Seguridad(Servicio):
