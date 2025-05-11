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

app = Flask(__name__)
app.config['JWT_SECRET_KEY']='$ecret0 dE_verdAd*'
jwt = JWTManager(app)

@app.route('/signup', methods=['POST'])
def signup():
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
    artista = request.args.get('artista', '')
    datos=Artista('','',artista,0,'')
    # en main llamamos a las funciones de mostrar los datos, 'datos' es un objeto de la clase artista
    return datos, 200

@app.route('/data/servicio', methods=['POST'])
@jwt_required()
def anyadir_servicio():
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
    nombres_publico=[]
    dni_publico=[]
    contador=0
    try:
        with open('publico.csv', 'r') as info:
            reader = csv.reader(info, delimiter=',')
            for row in reader:
                if contador==0:
                    contador+=1
                else:
                    nombres_publico.append(row[2])
                    dni_publico.append(row[1])
    except FileNotFoundError:
        return 'No encontrado el archivo con los festivales', 404
    return f'Son publico las personas: {nombres_publico} con dni: {dni_publico} ', 200



if __name__ == '__main__':
    app.run(debug=True)