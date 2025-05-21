from flask import Flask, request
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt)
import hashlib
from festival import Festival
from publico import Publico
from Personal.artista import Artista
from Personal.persona import Persona
from Personal.staff import Staff
import csv
import ast # para pasar str de listas a lista y manejarlo
from almacenamiento_artista import anadir_artista, eliminar_artista

app = Flask(__name__)
app.config['JWT_SECRET_KEY']='$ecret0 dE_verdAd*'
jwt = JWTManager(app)

@app.route('/signup', methods=['POST'])
def signup():
    """
    Registra un nuevo usuario y guarda sus credenciales en un archivo CSV.

    Obtiene el nombre de usuario y la contraseña desde los argumentos de la petición
    (request.args). Verifica si el usuario ya existe en el archivo usuarios.csv.
    Si no existe, calcula el hash de la contraseña y lo guarda junto al nombre de usuario.
    Si el archivo no existe, se devuelve un error indicando que no se encontró el archivo de usuarios.

    Returns
    -------
     Un par (respuesta, código de estado):
        - 200 si el usuario fue creado correctamente.
        - 409 si el usuario ya existe.
        - 404 si el archivo `usuarios.csv` no se encuentra.
    """
    datos=[]
    new_user = request.args.get('user', '')
    try:
        with open('usuarios.csv', 'r') as usuarios:
            reader = csv.reader(usuarios, delimiter=',')
            for user in reader:
                datos.append(user)
                if new_user == user[0]:
                    return f'El usuario {new_user} ya existe', 409

            password = request.args.get('password', '')
            hashed = hashlib.sha256(password.encode()).hexdigest()
            datos.append([new_user, hashed])
            writer = open('usuarios.csv', 'w')
            user_writer = csv.writer(writer, delimiter=',')
            user_writer.writerows(datos)
            writer.close()
            return f'Ususario {new_user} añadido correctamente', 200
    except FileNotFoundError:
        return 'No existe el documento usuarios.csv', 404

@app.route('/signin', methods=['GET'])
def signin():
    """
    Autentica a un usuario y genera un token JWT.

    Obtiene el nombre de usuario y la contraseña desde los argumentos de la petición
    (request.args). Verifica si el usuario existe en el archivo usuarios.csv y si
    la contraseña  también coincide. Si la autenticación es exitosa, se genera y se
    devuelve un token JWT con el código de estado 200. Si las credenciales son incorrectas,
    devuelve un mensaje de error con código de estado 401. Si el archivo no existe,
    se devuelve un error con código de estado 404.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Token JWT y código 200 si las credenciales son válidas.
        - Mensaje de error y código 401 si las credenciales son incorrectas.
        - Mensaje de error y código 404 si el archivo usuarios.csv no se encuentra.
    """
    user = request.args.get('user', '')
    password = request.args.get('password', '')
    hashed = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open('usuarios.csv', 'r') as usuarios:
            reader = csv.reader(usuarios, delimiter=',')
            for usuario in reader:
                if user == usuario[0] and hashed == usuario[1]:
                    return create_access_token(identity=user), 200
            return 'Usuario o contraseña incorrectos', 401
    except FileNotFoundError:
        return 'No existe el documento usuarios.csv', 404

# Eliminar usuario, no cerrar sesión
@app.route('/signout', methods=['DELETE'])
def signout():
    """
    Elimina un usuario del sistema.

    Obtiene el nombre de usuario y la contraseña desde los argumentos de la petición
    (request.args). Verifica si el usuario existe en el archivo usuarios.csv y si
    la contraseña coincide. Si el usuario es encontrado y autenticado, este se elimina.
    Si el archivo no existe, o si el usuario no es encontrado o la contraseña no es
    correcta, se devuelve un mensaje de error con código de estado 404.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje de éxito y código 200 si el usuario fue eliminado correctamente.
        - Mensaje de error y código 404 si el usuario no se encuentra o la contraseña es incorrecta.
        - Mensaje de error y código 404 si el archivo usuarios.csv no se encuentra.
    """
    datos_nuevos=[]
    user_found=False
    user = request.args.get('user', '')
    password = request.args.get('password', '')
    hashed = hashlib.sha256(password.encode()).hexdigest()
    try:
        with open('usuarios.csv', 'r') as usuarios:
            reader = csv.reader(usuarios, delimiter=',')
            for usuario in reader:
                if user == usuario[0] and hashed == usuario[1]:
                    user_found=True
                else:
                    datos_nuevos.append(usuario)
        if not user_found:
            return f'El usuario {user} no fue encontrado. Tal vez la contraseña no era la correcta, vuelva a intentarlo.', 404
    except FileNotFoundError:
        return 'No existe el documento usuarios.csv', 404
    with open('usuarios.csv', 'w') as usuarios:
        writer= csv.writer(usuarios, delimiter=',')
        writer.writerows(datos_nuevos)
        return f'El usuario {user} fue eliminado correctamente', 200

@app.route('/data', methods=['GET'])
def get_datos_festival():
    """
   Obtiene la información detallada de un festival específico.

    Lee el nombre del festival desde los argumentos de la petición (request.args)
    y lo busca en el archivo informacion_festivales.csv. Si encuentra el festival,
    devuelve un mensaje con su información. Si no encuentra el festival o
    si el archivono existe, devuelve un mensaje de error.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje con los detalles del festival y código 200 si se encuentra.
        - Mensaje de error y código 404 si el festival no fue encontrado.
        - Mensaje de error y código 404 si el archivo informacion_festivales.csv no se encuentra.
    """
    festival = request.args.get('festival', '')
    try:
        with open('informacion_festivales.csv', 'r') as festivales:
            reader= csv.reader(festivales, delimiter=',')
            for row in reader:
                if festival==row[0]:
                    return f'El festival {row[0]} se celebrará en la fecha {row[1]} en {row[2]}. \nEl aforo total es {row[3]}, solo quedan {row[5]} huecos. Costará {row[4]}€ en total. Sus servicios son: {row[7]} y los cantantes invitados son {row[8]}', 200
            return f'El festival {festival} no fue encontrado', 404
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404

# se pasan todos los datos por la url
@app.route('/data', methods=['POST'])
@jwt_required()
def crear_festival():
    """
    Crea un nuevo festival y lo guarda en el archivo informacion_festivales.csv.

    Esta función requiere autenticación JWT. Obtiene todos los datos del festival
    desde los argumentos de la petición (request.args): nombre, fecha, lugar,
    aforo y coste. Verifica si el festival ya existe en el archivo y, si no
    existe, lo añade.  Si el archivo no existe, se devuelve un error.

   Returns
    --------
        Un par (respuesta, código de estado):
        - Mensaje de éxito y código 200 si el festival fue creado correctamente.
        - Mensaje de error y código 409 si el festival ya existe.
        - Mensaje de error y código 404 si el archivo `informacion_festivales.csv` no se encuentra.
    """
    datos=[]
    nombre = request.args.get('nombre', '')
    fecha = request.args.get('fecha', '')
    lugar = request.args.get('lugar', '')
    aforo = request.args.get('aforo', '')
    coste = request.args.get('coste', '')
    try:
        with open('informacion_festivales.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for festival in reader:
                datos.append(festival)
                if nombre == festival[0]:
                    return f'El festival {nombre} ya existe', 409
    except FileNotFoundError:
        return 'No existe el documento con los festivales', 404
    datos.append([nombre,fecha,lugar,aforo,coste,aforo])
    with open('informacion_festivales.csv', 'w') as info:
        writer = csv.writer(info, delimiter=',')
        writer.writerows(datos)
        return f'Festival {nombre} añadido correctamente', 200

@app.route('/data', methods=['PUT'])
@jwt_required()
def modificar_festival():
    """
    Modifica los datos de un festival existente.

    Esta función requiere autenticación JWT. Recibe los parámetros desde los argumentos
    de la petición (request.args) y actualiza los campos correspondientes del festival.
    También utiliza un archivo auxiliar (inf_festivales_aux.csv) para reescribir la
    información de forma segura.

    Se modifica la fecha, el lugar, el aforo, el coste, los atendientes,
    los servicios y artistas invitados.

    """
    nombre = request.args.get('nombre', '')
    servicio = request.args.get('servicio', '')
    artista = request.args.get('artista', '')
    atendiente = request.args.get('atendiente', '')
    fecha = request.args.get('fecha', '')
    aforo = request.args.get('aforo', '')
    coste = request.args.get('coste', '')
    lugar = request.args.get('lugar', '')


    with open('informacion_festivales.csv', 'r') as csv_file, open('inf_festivales_aux.csv', 'w') as aux_file:
        reader = csv.reader(csv_file)
        writer = csv.writer(aux_file)

        for row in reader:
            if row[0] == nombre:
                fila = [nombre]
                if fecha != '':
                    fila.append(fecha)
                else:
                    fila.append(row[1])
                if lugar != '':
                    fila.append(lugar)
                else:
                    fila.append(row[2])
                if aforo != '':
                    fila.append(aforo)
                else:
                    fila.append(row[3])
                if coste != '':
                    fila.append(coste)
                else:
                    fila.append(row[4])
                if aforo != '':
                    fila.append(aforo - (row[3]-row[5]))
                else:
                    fila.append(row[5])
                if atendiente != '':
                    nuevos_atendientes = row[6]
                    for letter in atendiente:
                        nuevos_atendientes.insert(-2,letter)
                    fila.append(nuevos_atendientes)
                else:
                    fila.append(row[6])
                if servicio != '':
                    nuevos_servicios = row[7]
                    for letter in servicio:
                        nuevos_servicios.insert(-2,letter)
                    fila.append(nuevos_servicios)
                else:
                    fila.append(row[7])
                if artista != '':
                    nuevo_artista = row[8]
                    for letter in artista:
                        nuevo_artista.insert(-2,letter)
                    fila.append(nuevo_artista)
                else:
                    fila.append(row[8])
                writer.writerows(fila)
            else:
                writer.writerow(row)
        with open('informacion_festivales.csv', 'w') as csv_file, open('inf_festivales_aux.csv', 'r') as aux_file:
            reader = csv.reader(aux_file)
            writer = csv.writer(csv_file)
            for row in reader:
                writer.writerow(row)

@app.route('/data', methods=['DELETE'])
@jwt_required()
def eliminar_festival():
    """
    Elimina un festival del archivo informacion_festivales.csv.

   Esta función requiere autenticación JWT. El nombre del festival a eliminar
    se recibe como parámetro desde los argumentos de la petición (request.args).
    Si el festival existe en el archivo informacion_festivales.csv, lo elimina, y si
    el festival no se encuentra, devuelve un error. En caso de que no exista el archivo
    CSV, también se devuelve un mensaje de error

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje de éxito y código 200 si el festival fue eliminado correctamente.
        - Mensaje de error y código 404 si el festival no fue encontrado o si el archivo no existe.
    """
    datos_nuevos=[]
    festi_found=False
    festival = request.args.get('festival', '')
    try:
        with open('informacion_festivales.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if festival == row[0]:
                    festi_found=True
                else:
                    datos_nuevos.append(row)
        if not festi_found:
            return f'El festival {festival} no fue encontrado.', 404
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404
    with open('informacion_festivales.csv', 'w') as info:
        writer= csv.writer(info, delimiter=',')
        writer.writerows(datos_nuevos)
        return f'El festival {festival} fue eliminado correctamente', 200

#Notar que devuelve una lista
@app.route('/data_nombres', methods=['GET'])
def mostrar_festivales():
    """
    Obtiene una lista con los nombres de todos los festivales registrados.

    Lee el archivo informacion_festivales.csv y extrae únicamente los nombres de los
    festivales. Devuelve una lista de nombres en formato JSON junto con el código de
    estado 200. En caso de que el archivo no exista, devuelve un mensaje de error.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Se devuelve una lista con los festivales y código 200 si se ejecutó correctamente.
        - Mensaje de error y código 404 si no se encuentra el archivo.
    """
    nombres_festi = []
    contador = 0
    try:
        with open('informacion_festivales.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if contador == 0:
                    contador += 1
                else:
                    nombres_festi.append(row[0])
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404
    return nombres_festi, 200

@app.route('/data/artistas', methods=['GET'])
def datos_artista():
    """
    Obtiene los datos de un artista específico y de todos (si artista == '')

    Recibe el nombre del artista como parámetro desde los argumentos
    de la petición (request.args) y crea un objeto Artista con ese nombre. Este objeto se
    instancia con valores por defecto para los demás atributos.

    Returns
    -------
        Un par (datos del artista, código de estado 200 si todo ha salido correctamente, 404 si no encuentra al artista).
    """
    artista = request.args.get('artista', '')

    # Todos los artistas
    if artista == '':
        with open('artistas_disponibles.csv', 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            return 'Artista --- Link\n'+'\n'.join([f'{row['nombre'].capitalize()} -> https://open.spotify.com/artist/{row['link']}' for row in reader]), 200

    # Un artisata en especifico
    else:
        artista = ' '.join(artista.split('%20')) # Separamos el nombre del artista
        datos=Artista('','',artista,0,'')
        if datos.mostrar_canciones_populares() == 'Artista no encontrado':
            return f'{artista} no se encuentra entre los artistas disponibles', 404
        else:
            return datos.__str__(), 200


@app.route('/data/artistas', methods=['PUT'])
@jwt_required()
def anyadir_artista():
    """
    Añadimos un artista al csv de artistas_disponibles. Solo permitido con jwt

    Lee el archivo artistas_disponibles.csv y comprueba que el artista no este añadido ya.
    Si el artista ya esta añadido devuelve error 418. En caso contrario añade al artista junto
    a su link de spotify.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje correcto y código 200 si todo sale bien.
        - Mensaje de error y código 418 si ya está añadido.
    """
    artista = request.args.get('artista', '')
    artista = ' '.join(artista.split('%20')) # Separamos el nombre del artista
    link = request.args.get('link', '')

    result = anadir_artista(artista, link)
    status = 200 if result != f'Artista {artista} ya ha sido añadido previamente' else 418

    return result, status


@app.route('/data/artistas', methods=['DELETE'])
@jwt_required()
def quitar_artista():
    """
    Eliminamos un artista al csv de artistas_disponibles. Solo permitido con jwt

    Lee el archivo artistas_disponibles.csv y comprueba que el artista exista.
    Si el artista no existe devuelve error 418. En caso contrario elimina al artista

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje correcto y código 200 si todo sale bien.
        - Mensaje de error y código 418 si no existe.
    """
    artista = request.args.get('artista', '')
    artista = ' '.join(artista.split('%20')) # Separamos el nombre del artista

    result = eliminar_artista(artista)
    status = 200 if result != f'Artista {artista} no encontrado entre los artistas disponibles.' else 418

    return result, status

@app.route('/data/servicio', methods=['POST'])
@jwt_required()
def anyadir_servicio():
    """
    Añade un nuevo servicio a un festival existente.

    Esta función recibe mediante desde los argumentos de la petición (request.args) la
    información del servicio a añadir, así como el nombre del festival al que se asociará.
    Si el festival existe, se actualiza su lista de servicios y se almacena también
    el nuevo servicio en el fichero Servicios.csv.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje de éxito y código 200 si los datos se añadieron correctamente al festival y al fichero de servicios.
        - Mensaje de error y código 404 si el festival no se encuentra.
        - Mensaje de error y código 404 si el archivo de festivales no se encuentra.
    """
    datos_festi=[]
    datos_servicios=[]
    nombre_festi = request.args.get('festival', '')
    nombre_servicio =request.args.get('servicio', '')
    lugar = request.args.get('lugar', '')
    horario = request.args.get('horario', '')
    alquiler = request.args.get('alquiler', '')
    trabajadores = request.args.get('trabajadores', '')
    festi_found=False
    try:
        with open('informacion_festivales.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for festival in reader:
                if nombre_festi == festival[0]:
                    servicios= ast.literal_eval(festival[7])
                    if nombre_servicio not in servicios:
                        servicios.append(nombre_servicio)
                    festival[7] = str(servicios)
                datos_festi.append(festival)

        if not festi_found:
            return f'El festival {nombre_festi} no se ha encontrado', 404
    except FileNotFoundError:
        return 'No existe el documento con los festivales', 404

    with open('informacion_festivales.csv', 'w') as info:
        writer = csv.writer(info, delimiter=',')
        writer.writerows(datos_festi)
    with open('Servicios.csv','r') as servi:
        reader=csv.reader(servi, delimiter=',')
        for row in reader:
            datos_servicios.append(row)
    with open('Servicios.csv','w') as servi:
        writer= csv.writer(servi, delimiter=',')
        datos_servicios.append([nombre_servicio,horario,alquiler,lugar,trabajadores,nombre_festi])
        writer.writerows(datos_servicios)
        return f'Datos añadidos en el festival {nombre_festi} y en el fichero de servicios', 200

@app.route('/data_nombres/servicios', methods=['GET'])
def mostrar_servicios():
    """
    Devuelve una lista con los nombres de todos los servicios registrados.

    Esta función abre el archivo Servicios.csvn y extrae el nombre de cada servicio,
    el cual se asume que se encuentra en la primera columna. La lista resultante
    se devuelve al cliente.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Lista con los nombres de los servicios y código 200 si se lee correctamente el archivo.
        - Mensaje de error y código 404 si el archivo Servicios.csv no se encuentra.
    """
    nombres_servi=[]
    contador=0
    try:
        with open('Servicios.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if contador==0:
                    contador+=1
                else:
                    nombres_servi.append(row[0])
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404
    return nombres_servi, 200

@app.route('/data/trabajadores', methods=['GET'])
def mostrar_trabajadores():
    """
    Devuelve una lista con los nombres y DNI de todos los trabajadores registrados.

    Esta función abre el archivo staff.csv,y extrae los nombres y DNI de cada trabajador.
    Devuelve una cadena con ambas listas concatenadas de forma legible.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje con los nombres y DNI de los trabajadores y código 200 si se lee correctamente el archivo.
        - Mensaje de error y código 404 si el archivo staff.csv no se encuentra.
    """
    nombres_trabajadores=[]
    dni_trabajadores=[]
    contador=0
    try:
        with open('staff.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if contador==0:
                    contador+=1
                else:
                    nombres_trabajadores.append(row[2])
                    dni_trabajadores.append(row[1])
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404
    return f'Trabajan las personas: {nombres_trabajadores} con dni: {dni_trabajadores} ', 200

@app.route('/data/publico', methods=['GET'])
def mostrar_publico():
    """
    Devuelve una lista con los nombres de todas las personas del público.

    Esta función abre el archivo publico.csv, y extrae los nombres de cada
    persona registrada como público. Devuelve una cadena con la lista.

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje con los nombres del público y código 200 si se lee correctamente el archivo.
        - Mensaje de error y código 404 si el archivo publico.csv no se encuentra.
    """
    nombres_publico=[]

    contador=0
    try:
        with open('publico.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if contador==0:
                    contador+=1
                else:
                    nombres_publico.append(row[2])
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404
    except IndexError:
        return 'Error inesperado', 404
    return f'Son publico las personas: {nombres_publico}', 200

@app.route('/data/anyadir_publico', methods=['POST'])
def anyadir_publico():
    """

    Esta función abre el archivo publico.csv, y escribe los datos del nuevo atendiente

    Returns
    -------
        Un par (respuesta, código de estado):
        - Mensaje de éxito y código 200 si se escribe correctamente el archivo.
        - Mensaje de error y código 404 si el archivo publico.csv no se encuentra.
    """

    fecha_nacimiento = request.args.get('fecha_nacimiento', '')
    dni = request.args.get('dni', '')
    nombre = request.args.get('nombre', '')
    apellido1  = request.args.get('apellido1', '')
    apellido2  = request.args.get('apellido2', '')
    tipo_entrada  = request.args.get('tipo_entrada', '')
    dinero_actual = request.args.get('dinero_actual', '')
    festival=request.args.get('festival', '')


    datos = [fecha_nacimiento,dni,nombre,apellido1,tipo_entrada,dinero_actual,apellido2, festival]

    try:
       # Abrir en modo append para no sobrescribir
       with open('publico.csv', 'a') as publico:
           writer = csv.writer(publico, delimiter=',')
           writer.writerow(datos)  # Escribir una fila
           return 'Público añadido correctamente', 200


    except FileNotFoundError:
       return 'No se ha encontrado el archivo de publico', 404

@app.route('/data/publico_data', methods=['GET'])
def datos_atendiente():
    """

        Esta función abre el archivo publico.csv, y extrae los datos de la persona indicada.

        Returns
        -------
            Un par (respuesta, código de estado):
            - Mensaje con los datos del atendiente y código 200 si se lee correctamente el archivo.
            - Mensaje de error y código 404 si el archivo publico.csv no se encuentra.
            - Mensaje de error y código 404 si no se encuentra el atendiente en el fichero.
        """
    nombre = request.args.get('nombre', '')
    dni = request.args.get('dni', '')
    contador=0
    try:
        with open('publico.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if contador == 0:
                    contador += 1
                else:
                    if row[1]==dni and row[2]==nombre:
                        texto=f'Fecha de nacimiento: {row[0]}\nDni: {row[1]}\nNombre: {row[2]}\nApellido1: {row[3]}\nApellido2: {row[6]}\nTipo de entrada: {row[4]}\nDinero: {row[5]}\nFestival al que atiende: {row[7]}\n--------------------------------------'
                        return texto, 200
            return f'No se encontró {nombre} con dni {dni}', 404
    except FileNotFoundError:
        return 'No encontrado el archivo con los atendientes', 404

@app.route('/data/eliminar_publico', methods=['DELETE'])
def eliminar_atendiente():
    """

        Esta función abre el archivo publico.csv, y sobreescribe el fichero con todas las filas menos
        la fila del atendiente que queremos eliminar

        Returns
        -------
            Un par (respuesta, código de estado):
            - Mensaje con los datos del atendiente y código 200 si se lee correctamente el archivo.
            - Mensaje de error y código 404 si el archivo publico.csv no se encuentra.
            - Mensaje de error y código 404 si no se encuentra el atendiente en el fichero.
        """
    try:
        dni = str(request.args.get('dni', ''))
        with open('publico.csv', 'r') as publico_read:
            lineas = publico_read.readlines()
            lineas_nuevas = [linea for linea in lineas if dni not in linea]

        if lineas_nuevas == lineas:
            return f'No hay atendiente con dni: {dni}', 404

        else:
            with open('publico.csv', 'w') as publico_write:
                for linea in lineas_nuevas:
                    publico_write.write(linea)
            return f'Atendiente eliminado con exito', 200
    except FileNotFoundError:
        return f'No se ha encontrado el archivo', 404



if __name__ == '__main__':
    app.run(debug=True)