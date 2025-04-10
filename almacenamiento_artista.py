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