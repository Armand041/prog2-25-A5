class Persona:
    """
    Clase Persona
        Cubre lo básico de cualquier persona.
        Clase madre de todas las demás clases que son consideradas personas

    Atributos
    -----------------
    fecha_nacimiento: str
        Fecha de nacimiento de la persona.
    dni: str
        Documento Nacional Identificador de la persona.
    nombre: str
        Nombre de la persona
    apellido1: str
        Primer apellido de la persona
    apellido2: str
        Segundo apellido (si tiene) de la persona.

    Metodos:
    -------------
    __init__(self, fecha_nacimiento : str, dni: str, nombre: str, apellido1: str, apellido2: str ) -> None:
        Constructor del objeto.
    """

    def __init__(self, fecha_nacimiento: str, dni: str,nombre: str, apellido1: str,apellido2: str = None) -> None:
        """
        Metodo constructor

        Parámetros:
        -----------------
        fecha_nacimiento: str
            Fecha de nacimiento de la persona en formato dd/mm/aaaa
        dni: str
            Dni de la persona. Forma primaria de identificación
        nombre: str
            Nombre de la persona
        apellido1: str
            Primer apellido de la persona
        apellido2: str
            Segundo apellido (si tiene) de la persona. Si carece de él será None
        """
        self.__fecha_nacimiento = fecha_nacimiento
        self._nombre = nombre
        self.__apellido1 = apellido1
        self.__apellido2 = apellido2
        self.__dni = dni

    @property
    def dni(self):
        return self.__dni