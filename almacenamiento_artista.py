import csv

def anadir_artista(nombre: str, link: str) -> str:
    """
    Función para añadir artistas a la base de datos local

    Parámetros:
    -------------
    nombre:
        Nombre de spotify del artista, todo en minúscula
    link:
        id del artista de spotify
    """
    # Comprobamos si el artista ha sido ya incorporado en la base de datos local
    with open('artistas_disponibles.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            if row['nombre'] == nombre:
                # Si ya se encuentra en la base de datos devolvemos un mensaje de error
                return f'Artista {nombre} ya ha sido añadido previamente'

    # Añadimos al artista
    with open('artistas_disponibles.csv', 'a') as csv_file:
        fieldnames = ['nombre', 'link']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({'nombre': nombre, 'link': link})
        # Devolvemos un mensaje para asegurarnos que lo hemos añadido correctamente
        return f'¡Artista {nombre} ha sido correctamente almacenado!'


def eliminar_artista(nombre: str) -> str:
    """
    Función para eliminar artistas a la base de datos local

    Parámetros:
    -------------
    nombre:
        Nombre de spotify del artista, todo en minúscula
    """
    # leemos el archivo, apuntando todos los artistas menos el que queramos borrar
    with open('artistas_disponibles.csv', 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        artistas = [(row['nombre'], row['link']) if row['nombre'] != nombre else None for row in reader]
        try:
            index_eliminado = artistas.index(None)
        except ValueError:
            # Mensaje de error
            return f'Artista {nombre} no encontrado entre los artistas disponibles.'
        else:
            artistas.pop(index_eliminado)

    # Reescribimos el archivo con el reste de artistas
    with open('artistas_disponibles.csv', 'w') as csv_file:
        fieldnames = ['nombre', 'link']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({'nombre': 'nombre', 'link': 'link'}) # Esta linea evita que se borre la cabecera

        for nom, link in artistas:
            writer.writerow({'nombre': nom, 'link': link})
        # Devolvemos un mensaje para asegurarnos que lo hemos borrado correctamente
        return f'¡Artista {nombre} ha sido correctamente eliminado!'