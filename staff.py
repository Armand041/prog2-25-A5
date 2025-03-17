# from persona import Persona

class Staff(Persona):
    """
    Clase Staff
        Comprende a todos los trabajadores del festival, desde artistas hasta vendedores en pustos.

    Atributos:
    -------------
    edad: int
            Edad del trabajador
        nombre: str
            Nombre del trabajador
        dni: str
            Dni del trabajador
        sueldo: float
            Sueldo por hora del trabajador
        horario: str
            Horario en el que trabaja el empleado
        puesto_trabajo: object
            Objeto de tipo servicio en el que el empleado trabaja. Cada empleado solamente podrá estar
            relacionado con un solo puesto de trabajo.

    Metodos:
    -------------
    __init__(self, edad : int, nombre: str, dni: str, sueldo: float, horario: str ) -> None:
        Constructor del objeto, llamará a la clase Persona para sus atributos comunes.

    actualizar_sueldo(self, nuevo_sueldo: float) -> None :
        Reemplaza el sueldo actual del trabajador por nuevo_sueldo.

    cambiar_horario(self, nuevo_horario: str) -> None :
        Reemplaza el horario del trabajador por nuevo_horario.
    """

    def __init__(self, edad : int, nombre: str, dni: str, sueldo: float, horario: str, puesto_trabajo: object ) -> None :
        """
        Metodo constructor

        Parámetros:
        -----------------
        edad: int
            Edad del trabajador
        nombre: str
            Nombre del trabajador
        dni: str
            Dni del trabajador
        sueldo: float
            Sueldo por hora del trabajador
        horario: str
            Horario en el que trabaja el empleado, debe ser hora_inicio-hora_fin, por ejemplo: 9:00-5:00
        puesto_trabajo: object
            objeto de tipo servicio en el que el empleado trabaja
        """
        super().__init__(edad, nombre, dni)
        self.__sueldo=sueldo
        self.__horario=horario
        self.__puesto_trabajo=puesto_trabajo

    def actualizar_sueldo(self, nuevo_sueldo: float) -> None :
        """
        Metodo que reemplaza el sueldo del trabajador por uno nuevo

        Parámetros:
        --------------
        nuevo_sueldo: float
            Valor nuevo del sueldo del empleado
        """
        self.__sueldo=nuevo_sueldo

    def cambiar_horario(self, nuevo_horario: str) -> None :
        """
        Metodo que reemplaza el horario de un trabajador

        Parámetros:
        ---------------
        nuevo_horario: str
            Horario nuevo que recibirá el empleado
        """
        self.__horario=nuevo_horario

    def cambiar_puesto(self, nuevo_puesto: str) -> None :
        """
        Metodo que reemplaza el puesto de trabajo de un trabajador

        Parámetros:
        ---------------
        nuevo_puesto: str
            Puesto de trabajo nuevo que recibirá el empleado
        """
        self.__puesto_trabajo=nuevo_puesto