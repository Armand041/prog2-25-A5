# Gestión de festivales
[//]: # (Incluid aquí la descripción de vuestra aplicación. Por cierto, así se ponen comentarios en Markdown)
Este proyecto busca simplificar el almacenamiento y estructuración de festivales, para ayudar a clientes y organizadores a tener una mejor idea de la organización de sus eventos musicales favoritos. Permitirá planear, modificar y ejecutar varios festivales en diferentes lugares y tiempos. Añdiendo también una lista de artistas invitados, que contará con la opción de poder escuchar sus canciones. 

## Autores

* (Coordinador) [Daniel Paredes Valverde](https://github.com/Armand041)
* [David Diez Pérez ](https://github.com/daviddiez06)
* [Maria Ripoll Gomis ](https://github.com/mariaripoll4)
* [Pablo serna Soriano](https://github.com/PabloSerna4542)
* [Raúl Uclés Lajara ](https://github.com/RaulUclesLajara)

## Profesor
[//]: # (Dejad a quien corresponda)
[Miguel A. Teruel](https://github.com/materuel-ua)

## Requisitos
[//]: # (Indicad aquí los requisitos de vuestra aplicación, así como el alumno responsable de cada uno de ellos)
- Crear, modificar y eliminar festivales (lugar, fecha, duración, coste, aforo/espacio libre, permisos): Raúl Uclés Lajara 

- Añadir artistas invitados (canciones a cantar, dias que cantan, duración) y Trabajadores varios: Pablo Serna Soriano 

- Añadir servicios a los diferentes festivales (que ofrecen, precio, horario, lugar donde se ubican, trabajadores): Maria Ripoll Gomis 

- Creacion de Publico (Tipo de entrada) y relacion Publico/Festival (Aforo, asistencia): David Díez Pérez

- Relación de Servicios/Festival y Artista/Festival: David Díez Pérez 

- Permitirá acceder a canciones populares de los artistas (API de Spotify o Youtube): Daniel Paredes Valverde

- Clase Persona y Publico: Daniel Paredes Valverde 

## Instrucciones de instalación y ejecución

#### Instalación Nativa

- Primeramente debemos instalar un entorno virtual a través del fichero 'requirements.txt'.
  Para ello podemos utilizar el comando **pip install -r requirements.txt'** en la terminal de Linux

- A continuación ejecutaremos el fichero 'api_principal.py' 

- Por último, ejecutaremos el fichero 'main.py'

#### Uso de Ejecutables

- Ejecutar el archivo api_principal

- Ejecutar el archivo main

- ¡No sacar de la carpeta!

[//]: # (Indicad aquí qué habría que hacer para ejecutar vuestra aplicación)

## Resumen de la API


#### USUARIOS

- Sign up: Registra un **nuevo** usuario
    
    - POST 

    - Usuario: Nombre del usuario

    - Password: Contraseña para iniciar sesión


- Sign in: Inicia sesión en un usuario **existente**
    
    - GET
    
    - Usuario: Nombre del usuario

    - Password: Contraseña para inciciar sesión

- Sign out: Elimina un usuario **existente**
    
    - DELETE
    
    - Usuario: Nombre del usuario

    - Password: Contraseña para inciciar sesión


#### Festival

- Crear festival
    
    - POST
    
    - Requiere JWT 

    - Parámetros: nombre, fecha, lugar, aforo, coste
    

- Modificar festival 
  
    - PUT 
 
    - Requiere JWT

    - Parámetros : nombre, servicio, artista, atendiente, fecha, aforo, coste, lugar


- Eiminar festival 
  
    - DELETE
 
    - Requiere JWT

    - Parámetros: datos_nuevos(list), festi_found(bool), festival
  

- Get_datos_festival
    
    - GET
    
    - No requiere JWT 

    - Parámetros: festival


- Mostrar festivales: Muestra el nombre de todos los festivales creados
  
    - GET
 
    - No requiere JWT

    - Parámetros: nombres_festi


#### STAFF, ARTISTAS Y PUBLICO

- Datos_artista
    
    - GET     

    - No requiere JWT

    - Parámetros: artista
 
- Anyadir_artista

    - PUT
 
    - Requiere jwt
 
    - Parámetros: artista, link

 
- Quitar_artista

    - DELETE
 
    - Requiere jwt
 
    - Parámetros: artista
    

- Mostrar_publico
    
    - GET     

    - No requiere JWT

    - Parámetros: nombres_publico, dni_publico


- Mostrar_trabajadores
    
    - GET     

    - No requiere JWT

    - Parámetros: nombres_trabajadores, dni_trabajadores

- Mostrar_datos_atendiente
    
    - GET

    - No requiere JWT

    - Parámetros: nombre, dni

- Anyadir_publico
  
  - POST
  - No requiere JWT
  - Parámetros: fecha_nacimiento, dni, nombre, apellido1, apellido2,
   
    tipo_entrada, dinero_actual, festival

- Eliminar_atendiente
  
  - DELETE
  - No requiere JWT
  - Parámetros: dni

- Datos_atendiente

  - GET
  - No requiere JWT
  - Parámetros: nombre, dni

   
    
### SERVICIOS 

- Anyadir_servicio
    
    - POST   

    - Requiere JWT

    - Parámetros: datos_festi, datos_servicios, nombre_festi, nombre_servicio, 
  
      lugar, horario, alquiler, trabajadores, festi_found(bool) 


- Mostrar_servicios
    
    - GET

    - No requiere JWT

    - Parámetros: nombres_servi
  
     
