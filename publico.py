# from persona import Persona

class Público(Persona):
    '''
    Clase usada para representar al público que asistirá a cada festival

    Atributos
    ---------
    edad: int
        Edad que tiene la persona del público
    nombre: str
        Nombre de la persona del público
    dni: str
        Documento Nacional de Identidad de la persona del público
    tipo_entrada: str
        Tipo de entrada que se desea comprar
    dinero_actual: float
        Dinero disponible de cada persona del público

    Métodos
    -------
    __init__(self, edad: int, nombre: str, dni: str, tipo_entrada: str, dinero_actual: float)-> None:
        Es el constructor del objeto

    comprar_entrada(self, precio: float)-> str:
        Permite comprar una entrada

    devolver_entrada(self, precio)-> str:
        Devuelve una entrada y el dinero correspondiente al comprador de esta
    '''

    def __init__(self, edad: int, nombre: str, dni: str, tipo_entrada: str, dinero_actual: float) -> None:
        '''
        Método constructor

        Parámetros
        ----------
        edad: int
            Edad que tiene la persona del público
        nombre: str
            Nombre de la persona del público
        dni: str
            Documento Nacional de Identidad de la persona del público
        tipo_entrada: str
            Tipo de entrada que se desea comprar
        dinero_actual: float
            Dinero disponible de cada persona del público

        '''
        super().__init__(edad, nombre, dni)
        self.__tipo_entrada = tipo_entrada
        self.__dinero_actual = dinero_actual

    def comprar_entrada(self, precio: float) -> str:
        '''
       Método que permite comprar una entrada

       Parámetros
       ----------
       precio: float
           Dinero que cuesta la entrada
       '''

    if self.__dinero_actual >= precio:
        self.__dinero_actual -= precio
        return f"Entrada comprada. Aún dispone de: {self.__dinero_actual}€"
    else:
        return f"No dispone de saldo suficiente"

    def devolver_entrada(self, precio) -> str:
        '''
        Método que permite devolver una entrada y recuperar el dinero

        Parámetros
        ----------
        precio: float
            Dinero que se le devolvería al comprador
        '''
        self.__dinero_actual += precio
        return f"Entrada devuelta. Dispone de: {self.__dinero_actual}€"
