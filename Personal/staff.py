from Personal.persona import Persona

class Staff(Persona):
    """
    Clase Staff
        Comprende a todos los trabajadores del festival, desde artistas hasta vendedores en pustos.

    Atributos:
    -------------
        fecha_nacimiento: str
            Fecha de nacimiento del trabajador
        dni: str
            Dni del trabajador
        nombre: str
            Nombre del trabajador
        apellido1: str
            Primer apellido del trabajador
        apellido2: str
            Segundo apellido (si tiene) del trabajador
        sueldo: float
            Sueldo por hora del trabajador
        horario: str
            Horario en el que trabaja el empleado
        puesto_trabajo: object
            Objeto de tipo servicio en el que el empleado trabaja. Cada empleado solamente podrá estar
            relacionado con un solo puesto de trabajo.

    Metodos:
    -------------
    __init__(self, fecha_nacimiento : str, nombre: str, dni: str, sueldo: float, horario: str ) -> None:
        Constructor del objeto, llamará a la clase Persona para sus atributos comunes.

    actualizar_sueldo(self, nuevo_sueldo: float) -> None :
        Reemplaza el sueldo actual del trabajador por nuevo_sueldo.

    cambiar_horario(self, nuevo_horario: str) -> None :
        Reemplaza el horario del trabajador por nuevo_horario.
    """

    def __init__(self, fecha_nacimiento : str, dni: str, nombre: str, apellido1: str, sueldo: float, horario: str, puesto_trabajo: str, apellido2: str = None ) -> None :
        """
        Metodo constructor

        Parámetros:
        -----------------
        fecha_nacimiento: str
            Fecha de nacimiento del trabajador en formato dd/mm/aaaa
        dni: str
            Dni del trabajador. Forma primaria de identificacion
        nombre: str
            Nombre del trabajador
        apellido1: str
            Primer apellido del trabajador
        apellido2: str
            Segundo apellido (si tiene) del trabajador. Si carece de él será None
        sueldo: float
            Sueldo por hora del trabajador
        horario: str
            Horario en el que trabaja el empleado, debe ser hora_inicio-hora_fin, por ejemplo: 9:00-5:00
        puesto_trabajo: object
            objeto de tipo servicio en el que el empleado trabaja
        """
        super().__init__(fecha_nacimiento, dni, nombre, apellido1, apellido2)
        self._sueldo=sueldo
        self._horario=horario
        self._puesto_trabajo=puesto_trabajo

    def actualizar_sueldo(self, nuevo_sueldo: float) -> None :
        """
        Metodo que reemplaza el sueldo del trabajador por uno nuevo

        Parámetros:
        --------------
        nuevo_sueldo: float
            Valor nuevo del sueldo del empleado
        """
        if type(nuevo_sueldo)==float:
            self._sueldo=nuevo_sueldo
        else:
            print('Sueldo no válido, prueba con un número entero')

    def cambiar_horario(self, nuevo_horario: str) -> None :
        """
        Metodo que reemplaza el horario de un trabajador

        Parámetros:
        ---------------
        nuevo_horario: str
            Horario nuevo que recibirá el empleado
        """
        if type(nuevo_horario)==str:
            self._horario=nuevo_horario
        else:
            print('Horario no válido')

    def cambiar_puesto(self, nuevo_puesto: str) -> None :
        """
        Metodo que reemplaza el puesto de trabajo de un trabajador

        Parámetros:
        ---------------
        nuevo_puesto: str
            Puesto de trabajo nuevo que recibirá el empleado
        """
        self._puesto_trabajo=nuevo_puesto

    def __str__(self):
        return f'{super().__str__()}, Trabaja en: {self._puesto_trabajo}, Sueldo: {self._sueldo}, Horario del servicio: {self._horario}'
