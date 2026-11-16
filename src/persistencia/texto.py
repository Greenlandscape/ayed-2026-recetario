from pathlib import Path
from src.excepciones import ArchivoInvalidoError

# RAIZ = la carpeta del repo (donde está README.md).
# texto.py está en src/persistencia/, así que subimos 3 niveles:
# parents[0]=persistencia parents[1]=src parents[2]=repo
RAIZ = Path(__file__).resolve().parents[2]
DATA = RAIZ / "data"
RUTA_RECETAS = DATA / "recetas.txt"
RUTA_SUBRECETAS = DATA / "subrecetas.txt"
RUTA_BIN = DATA / "recetas.bin"

# para pruebas de ArchivoInvalidoError
# RUTA_BIN = DATA / "basura.bin"
# RUTA_BIN = DATA / "recetas_prueba.bin"  # para el truncado
# RUTA_RECETAS = DATA / "recetas_pruebas.txt" # txt roto


def cargar_texto(ruta):
    """Lee un .txt secuencial y devuelve una LISTA DE DICTS, uno por registro.
    La primera línea es el encabezado; cada línea siguiente es un registro
    con campos separados por coma. Si el archivo no existe o una línea
    tiene más/menos campos que el encabezado, lanza ArchivoInvalidoError.
    """

    ruta = DATA / ruta
    if not ruta.exists():
        raise ArchivoInvalidoError(f"No existe el archivo: {ruta}")

    filas = []
    with ruta.open("r", encoding="utf-8") as archivo:
        # archivo.readline() — lee una línea (la del encabezado). .strip() saca el \n del final.
        # .split(",") la parte en una lista: ["id", "nombre", ...]
        encabezado = archivo.readline().strip().split(",")
        for linea in archivo:
            # itera las líneas que quedan, de a una (no carga todo el archivo en RAM de golpe).
            linea = linea.strip()
            if not linea:  # línea vacía al final del archivo
                continue
            valores = linea.split(",")
            if len(valores) != len(encabezado):
                raise ArchivoInvalidoError(
                    f"Línea con {len(valores)} campos "
                    f"(se esperaban {len(encabezado)}): {linea}"
                )
            # zip junta los valores de cada lista creando parejas clave/valor; dict los transforma en diccionario
            fila = dict(zip(encabezado, valores))  # {'id': '1', 'nombre': ...}
            filas.append(fila)
    return filas


def guardar_texto(ruta, filas, encabezados):
    """Escribe el catálogo en .txt: encabezado + un registro por línea.
    filas: iterable de dicts. encabezados: lista con el orden de las columnas.
    """
    ruta = DATA / ruta
    with ruta.open("w", encoding="utf-8", newline="") as archivo:
        archivo.write(",".join(encabezados) + "\n")
        for fila in filas:
            # Arma una lista con los valores del diccionario fila, siguiendo el orden de encabezados.
            campos = [str(fila[clave]) for clave in encabezados]
            archivo.write(",".join(campos) + "\n")
