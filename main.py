"""
Programa principal.

Ejecuta un bucle para el usuario en el que este puede elegir entre distintas opciones
para manejar los distintos festivales y personas que trabajan en ellos y acuden a ellos.

Permite que estos datos se guarden en ficheros para que tengan permanencia.
"""

import requests
from festival import Festival
from publico import Publico
from Personal.artista import Artista
from Personal.persona import Persona
from Personal.staff import Staff
from servicio import EntradasSeguridad, SonidoLuces, Merch, Tattoo, Bebida, Comida
URL = 'http://127.0.0.1:5000/'
festivales = []
URL = 'http://127.0.0.1:5000/'

def seleccionar_festival():
    opc_festival = ''
    opciones_validas = [str(i + 1) for i in range(len(festivales))]

    while opc_festival not in opciones_validas:
        for i, festival in enumerate(festivales):
            print(f"{i + 1}. {festival.nombre}")
        opc_festival = input('Selecciona un festival (por número): ')

    return festivales[int(opc_festival) - 1]


def seleccionar_servicio_de_festival(festival):
    opc_servicio = ''
    opciones_validas = [str(i + 1) for i in range(len(festival.servicios))]

    while opc_servicio not in opciones_validas:
        for i, servicio in enumerate(festival.servicios):
            print(f"{i + 1}. {servicio.nombre}")
        opc_servicio = input('Selecciona un servicio (por número): ')

    return festival.servicios[int(opc_servicio) - 1]


def seleccionar_trabajador_de_servicio(servicio):
    opc_trabajador = ''
    opciones_validas = [str(i + 1) for i in range(len(servicio.trabajadores))]

    while opc_trabajador not in opciones_validas:
        for i, trabajador in enumerate(servicio.trabajadores):
            print(f"{i + 1}. {trabajador.nombre} ({trabajador.dni})")
        opc_trabajador = input('Selecciona un trabajador (por número): ')

    return servicio.trabajadores[int(opc_trabajador) - 1]

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
        if not aforo_fest.isdigit():
            print('Por favor, introduzca un número entero')
            aforo_fest = int(input('\nIntroduce el aforo del festival a crear: '))
        coste_fest = ''
        while type(coste_fest) != float:
            try:
                coste_fest = float(input('Introduce el coste del festival (en €): '))
            except TypeError:
                print('Por favor, introduzca un número')

        r = requests.post(f'{URL}/data?nombre={nombre_fest}&fecha={fecha_fest}&lugar={lugar_fest}&aforo={aforo_fest}&coste={coste_fest}')
        print(r.text + ' (' + str(r.status_code)+ ')')

    elif opcion == '2':
        print('Elige un festival para eliminar')
        festival_a_eliminar = seleccionar_festival()

        r = requests.delete(f'{URL}/data?festival={festival_a_eliminar}')
        print(r.text + ' (' + str(r.status_code)+ ')')

    elif opcion == '3':
        if len(festivales) == 0:
            print('No hay festivales disponibles')
        else:
            festival = seleccionar_festival()
            opcion_servicio=''
            opciones_mod=['1','2']
            while opcion_servicio not in opciones_mod:
                print('1. Añadir servicio: ')
                print('2. Añadir artista: ')
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

                r = requests.put(f'{URL}/data?nombre={festival}&servicio={nombre}')
                print(f'{r.text} ({r.status_code})')

            elif opcion_servicio == '2':
                servicio_introducir_trabjador = seleccionar_servicio_de_festival(festival)

                fecha_nacimiento = input('Introduce tu fecha de nacimiento: ')
                dni = input('Introduce tu dni: ')
                nombre = input('Introduce tu nombre: ')
                apellido1 = input('Introduce tu primer apellido: ')
                apellido2 = input('Introduce tu segundo apellido: ')
                sueldo = float(input('Introduce el sueldo: '))

                trabajador = Staff(fecha_nacimiento, dni, nombre, apellido1, sueldo, servicio_introducir_trabjador.horario, '' , apellido2)
                servicio_introducir_trabjador.contratar_trabajador(trabajador)
                r = requests.put(f'{URL}/data?nombre={festival}&artista={nombre}')
                print(f'{r.text} ({r.status_code})')


    elif opcion == '4':
        if len(festivales) == 0:
            print('No hay festivales disponibles para añadir asistentes')
        else:
            print('Selecciona un festival para añadir al asistente:')
            festival = seleccionar_festival()

            print('\nCrear nuevo usuario:')
            nombre = input('Nombre: ')
            apellido1 = input('Primer apellido: ')
            fecha_nacimiento = input('Fecha de nacimiento (dd/mm/aaaa): ')
            dni = input('DNI: ')
            tipo_entrada = input('Tipo de entrada (General/VIP/...): ')
            dinero_actual = ''
            while True:
                try:
                    dinero_actual = float(input('Dinero disponible (€): '))
                    break
                except ValueError:
                    print('Por favor, introduce un número válido para el dinero (float)')

            nuevo_usuario = Publico(fecha_nacimiento, dni, nombre, apellido1, tipo_entrada, dinero_actual)

            festival.anyadir_persona(nuevo_usuario)
            print('Nuevo asistente añadido al festival')
    elif opcion == '5':
        usuario = str(input('Usuario: '))
        password = str(input('Password: '))
        r = requests.get(f'{URL}/signin?user={usuario}&password={password}')

        pass
    elif opcion == '6':
        for festival in festivales:
            print(f"{festival}\n")
    elif opcion == '7':
        festival = seleccionar_festival()
        print(festival)
    elif opcion == '8':
        festival = seleccionar_festival()
        servicio = seleccionar_servicio_de_festival(festival)
        print(servicio)
    elif opcion == '9':
        festival = seleccionar_festival()
        servicio = seleccionar_servicio_de_festival(festival)
        trabajador = seleccionar_trabajador_de_servicio(servicio)
        print(trabajador)
    elif opcion == '10':


        pass
    elif opcion == '11':
        r = requests.get(f'{URL}/data/publico')
        pass
    elif opcion == '12':
        print('Cerrando programa)')
        break
