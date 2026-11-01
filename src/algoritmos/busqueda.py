def busqueda_lineal(coleccion, clave, obtener_clave=None):
    """Devuelve el elemento cuya clave es igual a 'clave', o None si no existe.
    obtener_clave: función que de un elemento devuelve la clave a comparar
    (ej: lambda p: p.nombre). Si es None, compara el elemento entero.
    """
    # Nuestra lista_enlazada ya tiene un iter, por lo cual, podemos usar for
    for elemento in coleccion:
        if obtener_clave is None:
            if elemento == clave:
                return elemento
        elif obtener_clave(elemento) == clave:
            return elemento
    return None


def busqueda_binaria(coleccion, clave, obtener_clave):
    """Búsqueda binaria. REQUIERE que la colección esté ordenada por esa
    clave."""
    izq = coleccion._cabeza
    # Utilizamos tamanio(), el método propio de lista_enlazada, en lugar de len()
    rango = coleccion.tamanio()

    while rango > 0:
        pasos = rango // 2
        nodo_medio = izq
        # Nos movemos hacia el medio una cantidad de pasos
        for _ in range(pasos):
            nodo_medio = nodo_medio.siguiente
        valor = obtener_clave(nodo_medio.dato)
        if valor == clave:
            return nodo_medio.dato
        elif valor < clave:  # está a la derecha del medio
            # entonces movemos izq
            izq = nodo_medio.siguiente
            # se descartan los pasos nodos de la izquierda y nodo_medio
            rango = rango - pasos - 1
        else:
            # el valor está en la mitad izquierda, por lo cual, izq no se mueve
            # los pasos nodos a la izquierda de nodo_medio son lo que queda del rango
            rango = pasos
    return None
