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

import csv

def cargar_festivales_desde_csv():
    festivales.clear()
    try:
        with open('informacion_festivales.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for row in lector:
                nombre, fecha, lugar, aforo, coste = row[:5]
                fest = Festival(nombre, fecha, lugar, aforo, coste)
                festivales.append(fest)
    except FileNotFoundError:
        print("Archivo de festivales no encontrado.")

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

cargar_festivales_desde_csv()

while True:
    opcion = ''
    opciones = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

    while opcion not in opciones:
        # Pueden haber más o menos opciones esto es un ejemplo y primera idea
        print('1. Registrar usuario')
        print('2. Iniciar sesión')
        print('3. Eliminar usuario')
        print('4. Crear festival')
        print('5. Eliminar festival')
        print('6. Modificar festival')
        print('7. Mostrar festivales')
        print('8. Mostrar información de un festival')
        print('9. Mostrar datos de un servicio')
        print('10. Mostrar datos de un trabajador')
        print('11. Mostrar datos de un artista')# Aquí hacemos tambien que te muestre lo de la api que está en la clase artista
        # podemos añadir tambien que muestre los artistas disponibles
        print('12. Mostrar datos de un atendiente')
        print('13. Terminar')
        opcion = input('Introduce una de las opciones (por número): ')


    if opcion == '1':
        usuario = input('Elige un nombre de usuario: ')
        password = input('Elige una contraseña: ')
        r = requests.post(f'{URL}/signup?user={usuario}&password={password}')
        if r.status_code == 200:
            print(f'Usuario {usuario} creado correctamente')
        else:
            print(f'Error al crear usuario: {r.status_code} - {r.text}')

    elif opcion == '2':
        usuario = input('Usuario: ')
        password = input('Password: ')
        r = requests.get(f'{URL}/signin?user={usuario}&password={password}')
        if r.status_code == 200:
            token = r.text
            print('Inicio de sesión correcto')
        else:
            print('Error al iniciar sesión:', r.text)

    elif opcion == '3':
        usuario = input('Introduce el nombre de usuario a eliminar: ')
        password = input('Introduce la contraseña del usuario: ')
        r = requests.delete(f'{URL}/signout?user={usuario}&password={password}')
        if r.status_code == 200:
            print(f'Usuario {usuario} eliminado correctamente')
        else:
            print(f'Error al eliminar usuario: {r.status_code} - {r.text}')

    elif opcion == '4':

        nombre_fest = input('Introduce el nombre del festival a crear: ')
        fecha_fest = input('Introduce la fecha del festival a crear: ')
        lugar_fest = input('Introduce el lugar del festival: ')
        aforo_fest = input('Introduce el aforo del festival a crear: ')
        while not aforo_fest.isdigit():
            print('Por favor, introduzca un número entero')
            aforo_fest = input('Introduce el aforo del festival a crear: ')
        aforo_fest = int(aforo_fest)
        coste_fest = ''
        while True:
            try:
                coste_fest = float(input('Introduce el coste del festival (en €): '))
                break
            except ValueError:
                print('Por favor, introduzca un número válido')
        r = requests.post(f'{URL}/data?nombre={nombre_fest}&fecha={fecha_fest}&lugar={lugar_fest}&aforo={aforo_fest}&coste={coste_fest}', headers={'Authorization': f'Bearer {token}'})
        print(r.text + ' (' + str(r.status_code) + ')')

        if r.status_code == 200:
            nuevo_festival = Festival(nombre_fest, fecha_fest, lugar_fest, aforo_fest, coste_fest)
            festivales.append(nuevo_festival)


    elif opcion == '5':
        if not festivales:
            print("No hay festivales disponibles. Carga o crea alguno primero.")
        else:
            print('Elige un festival para eliminar:')
            festival_a_eliminar = seleccionar_festival()
            r = requests.delete(f'{URL}/data?festival={festival_a_eliminar.nombre}', headers={'Authorization': f'Bearer {token}'})
            print(r.text + ' (' + str(r.status_code) + ')')
            if r.status_code == 200:
                festivales.remove(festival_a_eliminar)

    elif opcion == '6':
        if len(festivales) == 0:
            print('No hay festivales')
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

    elif opcion == '7':
        r = requests.get(f'{URL}/data_nombres')
        if r.status_code == 200:
            nombres = r.text.strip("[]").replace("'", "").split(", ")
            print('Festivales registrados:')
            for nombre in nombres:
                print(f"- {nombre}")
        else:
            print(f'Error al obtener festivales: {r.status_code} - {r.text}')

    elif opcion == '8':
        festival = seleccionar_festival()
        print(festival)
    elif opcion == '9':
        festival = seleccionar_festival()
        servicio = seleccionar_servicio_de_festival(festival)
        print(servicio)
    elif opcion == '10':
        festival = seleccionar_festival()
        servicio = seleccionar_servicio_de_festival(festival)
        trabajador = seleccionar_trabajador_de_servicio(servicio)
        print(trabajador)
    elif opcion == '11':


        pass
    elif opcion == '12':
        r = requests.get(f'{URL}/data/publico')
        pass
    elif opcion == '13':
        print('Cerrando programa)')
        break