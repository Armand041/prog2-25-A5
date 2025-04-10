"""
Programa principal.

Ejecuta un bucle para el usuario en el que este puede elegir entre distintas opciones
para manejar los distintos festivales y personas que trabajan en ellos y acuden a ellos.

Permite que estos datos se guarden en ficheros para que tengan permanencia.
"""

from festival import Festival
from publico import Público
from Personal.artista import Artista
from Personal.persona import Persona
from Personal.staff import Staff

while True:
    opcion = ''
    opciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']

    while opcion not in opciones:
        # Pueden haber más o menos opciones esto es un ejemplo y primera idea
        print('1. Crear festival')
        print('2. Eliminar festival')
        print('3. Modificar festival')
        print('4. Crear usuario')
        print('5. Iniciar sesión')
        print('6. Mostrar festivales')
        print('7. Mostrar información de un festival')
        print('8. Mostrar datos de un servicio')
        print('9. Mostrar datos de un trabajador')
        print('10. Mostrar datos de un artista')# Aquí hacemos tambien que te muestre lo de la api que está en la clase artista
        # podemos añadir tambien que muestre los artistas disponibles
        print('11. Mostrar datos de un atendiente')
        print('12. Terminar')
        opcion = input('Introduce una de las opciones (por número): ')

    if opcion == '1':
        nombre_fest = input('Introduce el nombre del festival a crear: ')
        fecha_fest = input('Introduce la fecha del festival a crear: ')
        aforo_fest = input('Introduce el aforo del festival a crear: ')
        if aforo_fest.isdigit():
            print('Por favor, introduzca un número entero')
            aforo_fest = input('\nIntroduce el aforo del festival a crear: ')
        coste_fest = ''
        while type(coste_fest) != float:
            try:
                coste_fest = float(input('Introduce el coste del festival (en €): '))
            except TypeError:
                print('Por favor, introduzca un número')
        # el resto


    elif opcion == '2':
        pass
    elif opcion == '3':
        opc_mod=''
        opciones_mod=['1','2','3','4','5','6','7','8']
        while opc_mod not in opciones_mod:
            print('1. Añadir servicio: ')
            print('2. Eliminar servicio: ')
            print('3. Añadir trabajador: ')
            print('4. Eliminar trabajador: ')
            print('5. Añadir artista: ')
            print('6. Eliminar artista: ')
            print('7. Añadir atendiente: ')
            print('8. Eliminar atendiente: ') # etc
    elif opcion == '4':
        pass
    elif opcion == '5':
        pass
    elif opcion == '6':
        pass
    elif opcion == '7':
        pass
    elif opcion == '8':
        pass
    elif opcion == '9':
        pass
    elif opcion == '10':
        pass
    elif opcion == '11':
        pass
    elif opcion == '12':
        print('Cerrando programa)')
        break
