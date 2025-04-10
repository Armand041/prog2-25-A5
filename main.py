"""
Programa principal.

Ejecuta un bucle para el usuario en el que este puede elegir entre distintas opciones
para manejar los distintos festivales y personas que trabajan en ellos y acuden a ellos.

Permite que estos datos se guarden en ficheros para que tengan permanencia.
"""

from festival import Festival
from publico import Publico
from Personal.artista import Artista
from Personal.persona import Persona
from Personal.staff import Staff
from servicio import EntradasSeguridad, SonidoLuces, Merch, Tattoo, Bebida, Comida

festivales = []

def seleccionar_festival():
    opc_festival = ''
    opciones_validas = [str(i + 1) for i in range(len(festivales))]

    while opc_festival not in opciones_validas:
        for i, festival in enumerate(festivales):
            print(f"{i + 1}. {festival.nombre}")
            opc_festival = input('Selecciona un festival (por número): ')

    return festivales[int(opc_festival) - 1]


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
        lugar_fest = input('Introduce el lugar del festival: ')
        aforo_fest = input('Introduce el aforo del festival a crear: ')
        if aforo_fest.isdigit():
            print('Por favor, introduzca un número entero')
            aforo_fest = input('\nIntroduce el aforo del festival a crear: ')
        coste_fest = ''
        permisos_fest = []
        while type(coste_fest) != float:
            try:
                coste_fest = float(input('Introduce el coste del festival (en €): '))
            except TypeError:
                print('Por favor, introduzca un núsmero')
        while True:
            permiso = input('Introduce un permiso para el festival (no escribas nada para terminar): ')
            if permiso == '':
                break
            permisos.append(permiso)
        festival_nuevo = Festival(nombre_fest, fecha_fest, lugar_fest, aforo_fest, coste_fest, permisos_fest)
        festivales.append(festival_nuevo)
        print('Nuevo festival creado')

    elif opcion == '2':
        pass
    elif opcion == '3':
        if len(festivales) == 0:
            print('No hay festivales disponibles')
        else:
            festival = seleccionar_festival()
            opcion_servicio=''
            opciones_mod=['1','2','3','4','5','6','7','8']
            while opcion_servicio not in opciones_mod:
                print('1. Añadir servicio: ')
                print('2. Eliminar servicio: ')
                print('3. Añadir trabajador: ')
                print('4. Eliminar trabajador: ')
                print('5. Añadir artista: ')
                print('6. Eliminar artista: ')
                print('7. Añadir atendiente: ')
                print('8. Eliminar atendiente: ')
                opcion_servicio = input('Introduce una de las opciones (por número): ')

            if opcion_servicio == '1':
                opcion_puesto = ''
                opciones_puestos = ['1', '2', '3', '4', '5', '6']
                while opcion_puesto not in opciones_puestos:
                    print('1. Puesto de Comida')
                    print('2. Puesto de Bebidas')
                    print('3. Puesto de de Tatuajes')
                    print('4. Puesto de Merchandising')
                    print('5. Servicio de Luces y Sonido')
                    print('6. Servicio de Seguridad de las entradas')
                    opcion_puesto = input('Introduce una de las opciones (por número): ')

                nombre = input('Introduce el nombre del servicio: ')
                horario = input('Introduce el horario del servicio: ')
                alquiler = float(input('Introduce el costo del alquiler del servicio: '))
                lugar  = input('Introduce el lugar donde se encuentra el puesto: ')

                if opcion_puesto == '1':
                    comida1 = Comida(nombre, horario, alquiler, lugar, [])
                    festival.anyadir_servicio(comida1)

                elif opcion_puesto == '2':
                    bebida1 = Bebida(nombre, horario, alquiler, lugar, [])
                    festival.anyadir_servicio(bebida1)

                elif opcion_puesto == '3':
                    tattoo1 = Tattoo(nombre, horario, alquiler, lugar, [])
                    festival.anyadir_servicio(tattoo1)

                elif opcion_puesto == '4':
                    merch1 = Merch(nombre, horario, alquiler, lugar, [])
                    festival.anyadir_servicio(merch1)

                elif opcion_puesto == '5':
                    sonidoLuces1 = SonidoLuces(nombre, horario, alquiler, lugar, [])
                    festival.anyadir_servicio(sonidoLuces1)

                elif opcion_puesto == '6':
                    entradasSeguridad1 = EntradasSeguridad(nombre, horario, alquiler, lugar, [])
                    festival.anyadir_servicio(entradasSeguridad1)

            if opcion_servicio == '3':
                fecha_nacimiento = input('Introduce tu fecha de nacimiento: ')
                dni = input('Introduce tu dni: ')
                nombre = input('Introduce tu nombre: ')
                apellido1 = input('Introduce tu primer apellido: ')
                apellido2 = input('Introduce tu segundo apellido: ')



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
