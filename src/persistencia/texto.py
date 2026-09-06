def cargar_texto(ruta):
    """Carga secuencial de un .txt: un registro por línea, separado por coma.
    Devuelve una lista de dicts (E1 puede quedar así)."""
    lineas_archivo = []
    # Abrimos el archivo de forma segura y cargamos el contenido a una lista.
    # Dicha lista contiene str, el primero son los headers
    with open(ruta, "r", encoding="utf-8") as lineas:
        for linea in lineas:
            linea_limpia = linea.strip()
            lineas_archivo.append(linea_limpia)

    # Tomamos los headers del primer elemento y hacemos una lista
    lista_claves = lineas_archivo[0].split(",")
    # Tomamos las siguientes lineas, que son los valores y hacemos otra lista por comprensión
    lista_valores = [renglon.split(",") for renglon in lineas_archivo[1:]]
    lista_diccs = []

    # Armamos la lista de diccionarios que queremos devolver.
    for lista_valor in lista_valores:
        #Tomamos dos listas, una con las claves, otra con los valores de esas claves,
        # zip junta los valores de cada lista creando parejas clave/valor; dict los transforma en diccionario
        diccionario = dict(zip(lista_claves, lista_valor)) 
        lista_diccs.append(diccionario)
    return lista_diccs

    

def guardar_texto(ruta, filas, encabezados):
    """Escribe el catálogo en .txt con la primera línea de encabezados."""
    raise NotImplementedError
