from flask import Flask, request
from flask_jwt_extended import (JWTManager, create_access_token, jwt_required, get_jwt_identity, get_jwt)
import hashlib
from festival import Festival
from publico import Público
from Personal.artista import Artista
from Personal.persona import Persona
from Personal.staff import Staff
import csv

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
            return f'Ususario {user} añadido correctamente', 200
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
        return f'El usuarios {user} fue eliminado correctamente', 200