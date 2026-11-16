import struct
from pathlib import Path
from src.excepciones import ArchivoInvalidoError, ItemNoEncontradoError
from src.dominio.receta import Receta
from src.config import TEMA
from src.tads.lista_enlazada import ListaEnlazada

"""Registros de longitud fija con struct.

Layout sugerido (documentar el definitivo en docs/INFORME.md):

Header:
  magia     4s   b'AYED'
  tema      1s   b'P' | b'R' | b'M'
  cantidad  I    unsigned int

El registro depende del tema. Recetario:

"<I 30s H 10s 15s"
id
nombre(30) 
tiempo_min
dificultad(10) 
categoría(15)
"""


FORMATO = struct.Struct("<I 30s H 10s 15s")  # 61 bytes por registro
HEADER = struct.Struct("<4s 1s I")  # 9 bytes: magia, tema, cantidad
TEMA = b"R"  # Recetario: R


def _a_bytes(texto, ancho):
    """Texto → bytes UTF-8 de 'ancho' exacto: recorta o rellena con \\x00."""
    return texto.encode("utf-8")[:ancho].ljust(ancho, b"\x00")


def _a_texto(datos):
    """Bytes → texto: le saca los \\x00 del final."""
    return datos.rstrip(b"\x00").decode("utf-8")


def _item_a_tupla(p):
    """Objeto del dominio → tupla lista para FORMATO.pack. Ajustado a Recetario."""
    return (
        p.receta_id,
        _a_bytes(p.nombre, 30),
        p.tiempo,
        _a_bytes(p.dificultad or "", 10),
        _a_bytes(p.categoria, 15),
    )


def _tupla_a_item(t):
    """Tupla que salió de FORMATO.unpack → objeto del dominio. Ajustado a Recetario."""
    return Receta(
        id=t[0],
        nombre=_a_texto(t[1]),
        tiempo_min=t[2],
        dificultad=_a_texto(t[3]) or None,
        categoria=_a_texto(t[4]),
    )


def guardar_binario(ruta, catalogo):
    """Escribe el archivo completo: header (magia + tema + cantidad) + registros."""
    with open(ruta, "wb") as archivo:
        archivo.write(HEADER.pack(b"AYED", TEMA, catalogo.tamanio()))
        for item in catalogo:  # iterador de E3 otra vez
            archivo.write(FORMATO.pack(*_item_a_tupla(item)))


def cargar_binario(ruta):
    """Lee el binario con validaciones. Devuelve la ListaEnlazada de ítems."""
    with open(ruta, "rb") as archivo:
        cabecera = archivo.read(HEADER.size)
        if len(cabecera) < HEADER.size:
            raise ArchivoInvalidoError(
                "Binario truncado: ni siquiera tiene header completo."
            )
        magia, tema, cantidad = HEADER.unpack(cabecera)
        if magia != b"AYED":
            raise ArchivoInvalidoError(
                "Magia incorrecta: este archivo no es de este TP."
            )
        if tema != TEMA:
            raise ArchivoInvalidoError(
                f"El tema del archivo ({tema!r}) no es el mío ({TEMA!r})."
            )
        catalogo = ListaEnlazada()
        for _ in range(cantidad):
            datos = archivo.read(FORMATO.size)
            if len(datos) < FORMATO.size:
                raise ArchivoInvalidoError(
                    "Binario truncado: el header dice más registros de los que hay."
                )
            catalogo.insertar_al_final(_tupla_a_item(FORMATO.unpack(datos)))
        return catalogo


def actualizar_registro(ruta, posicion, item):
    """Pisa SOLO el registro número 'posicion' (0-based) sin tocar el resto."""
    with open(ruta, "r+b") as archivo:  # r+b = leer Y escribir
        archivo.seek(HEADER.size + posicion * FORMATO.size)  # el salto del dibujo
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))


def posicion_del_id(catalogo, id_buscado):
    """Devuelve la posición (0-based) del ítem con ese id, usando el iterador."""
    # enumerate funciona sobre la lista enlazada porque tiene un iterador
    for posicion, item in enumerate(catalogo):
        if item.receta_id == id_buscado:
            return posicion
    raise ItemNoEncontradoError(f"No hay ítem con id {id_buscado}")


def alta_binario(ruta, item):
    """Agrega un registro AL FINAL y actualiza la cantidad del header."""
    with open(ruta, "r+b") as archivo:
        cabecera = archivo.read(
            HEADER.size
        )  # lee los bytes del encabezado y los asigna a cabecera
        magia, tema, cantidad = HEADER.unpack(cabecera)  # aquí lo desarma en una tupla
        archivo.seek(0, 2)  # 2 = saltar al FINAL del archivo (el dos indica eso)
        archivo.write(FORMATO.pack(*_item_a_tupla(item)))
        archivo.seek(0)  # volver al principio
        archivo.write(HEADER.pack(magia, tema, cantidad + 1))  # arreglar cantidad


def baja_binario(ruta, posicion):
    """Quita el registro 'posicion': relee, saca ese registro y reescribe todo."""
    with open(ruta, "r+b") as archivo:
        cabecera = archivo.read(HEADER.size)
        magia, tema, cantidad = HEADER.unpack(cabecera)
        # Lee todos los registros y los almacena en una lista.
        registros = [archivo.read(FORMATO.size) for _ in range(cantidad)]
        del registros[posicion]  # afuera el dado de baja
        # mueve el cursor al inicio del archivo
        archivo.seek(0)
        # Borra todo el contenido del archivo a partir de la posición actual (0)
        archivo.truncate()
        # reescribe el archivo completo sin el que fue borrado
        archivo.write(HEADER.pack(magia, tema, len(registros)))
        for datos in registros:
            archivo.write(datos)
