from Personal.persona import Persona
from servicio import Servicio

class Publico(Persona):
    '''
    Clase usada para representar al público que asistirá a cada festival

    Atributos
    ---------
    fecha_nacimiento: str
        Fecha de nacimiento de la persona del público en formato dd/mm/aaaa
    dni: str
        Documento Nacional de Identidad de la persona del público
    nombre: str
        Nombre de la persona del público
    apellido1: str
        Primer apellido de la persona
    apellido2: str
        Segundo apellido (si tiene) de la persona
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

    ver_saldo(self)-> float
        Devuelve el dinero actual del usuario

    actualizar_tipo_entrada(self, nuevo_tipo_entrada: str)->None
        Cambia el tipo de entrada que tiene la persona

    comprar_servicio(self, servicio: Servicio, producto: str) -> str:
        Permite comprar un producto de un servicio del festival

    __str__(self)-> str
        Devuelve una representación en cadena de texto del objeto
    '''

    def __init__(self, fecha_nacimiento: str, dni: str, nombre: str, apellido1: str, tipo_entrada: str, dinero_actual: float, apellido2: str = None) -> None:
        '''
        Método constructor

        Parámetros
        ----------
        fecha_nacimiento: int
            Fecha de nacimiento de la persona del público en formato dd/mm/aaaa
        dni: str
            Documento Nacional de Identidad de la persona del público
        nombre: str
            Nombre de la persona del público
        apellido1: str
            Primer apellido de la persona
        apellido2: str
            Segundo apellido (si tiene) de la persona
        tipo_entrada: str
            Tipo de entrada que se desea comprar
        dinero_actual: float
            Dinero disponible de cada persona del público

        '''
        super().__init__(fecha_nacimiento, dni, nombre, apellido1, apellido2)
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

    def ver_saldo(self) -> float:
        """
        Método que devuelve el dinero actual 
        """
        return self.__dinero_actual

    def actualizar_tipo_entrada(self, nuevo_tipo_entrada: str) -> None:
        """
        Método que cambia el tipo de entrada que tiene la persona

        Parámetros:
        ----------
        nuevo_tipo_entrada: str
            Nuevo tipo de entrada
        """
        self.__tipo_entrada = nuevo_tipo_entrada

    def comprar_servicio(self, servicio: Servicio, producto: str) -> str:
        '''
        Método que permite comprar un producto de un servicio del festival

        Parámetros:
        -----------
        servicio: Servicio
            Servicio del que se quiere comprar el producto
        producto: str
            Nombre del producto a comprar
        '''
        productos_inf = servicio.obtener_informacion()

        if isinstance(productos_inf, dict):
            if producto in productos_inf:
                precio = productos_inf[producto]

                if self.__dinero_actual >= precio:
                    self.__dinero_actual -= precio
                    return f"Producto '{producto}' comprado por {precio}€. Dinero restante: {self.__dinero_actual}€"
                else:
                    return f"No dispone de saldo suficiente"
            else:
                return f"Producto no disponible en el servicio"
        else:
            return f"este servicio no ofrece productos"

    def __str__(self)-> str:
        '''
        Devuelve una representación en cadena de texto del objeto
        '''
        return f" {self._nombre} tiene una entrada {self.__tipo_entrada} y dispone de {self.__dinero_actual}€"
