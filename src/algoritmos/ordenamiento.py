def ordenar_seleccion(coleccion, obtener_clave):
    """Ordena la colección (lista enlazada) in place (la modifica) por selección (ascendente)."""
    actual = coleccion._cabeza
    while actual:
        # Considera que el elemento actual es el menor.
        # Recorre el segmento que todavía no está ordenado
        pos_min = actual
        buscador = actual.siguiente
        while buscador:
            # Si encuentra un nodo con un dato menor, guarda ese nodo como mínimo.
            if obtener_clave(buscador.dato) < obtener_clave(pos_min.dato):
                pos_min = buscador
                # aquí encontró uno menor, seguirá comparando hasta al fin del bucle
            buscador = buscador.siguiente
        # Terminó de buscar en el segmento desordenado, entonces,
        # Intercambia el elemento actual con el menor encontrado.
        actual.dato, pos_min.dato = pos_min.dato, actual.dato
        actual = actual.siguiente


def ordenar_insercion(coleccion, obtener_clave):
    """Ordena la colección (lista enlazada) in place (la modifica) por inserción (ascendente)."""
    # Si está vacía
    if coleccion._cabeza is None:
        return
    # Separamos la colección en dos, ordenados y no ordenados
    ordenado = coleccion._cabeza
    desordenado = ordenado.siguiente

    while desordenado:
        nodo_ordenado = coleccion._cabeza
        anterior = None
        # Aquí nodo_ordenado avanza siempre desde la cabeza de la lista hacia adelante en la parte ordenada.
        # Entra cuando un nodo_ordenado es menor O IGUAL (estable) que el desordenado
        # y termina cuando eso no pasa (hay que insertar)
        while nodo_ordenado is not desordenado and obtener_clave(
            nodo_ordenado.dato
        ) <= obtener_clave(desordenado.dato):
            # conservamos este nodo para poder arreglar los enlaces luego
            anterior = nodo_ordenado
            nodo_ordenado = nodo_ordenado.siguiente
        # terminado el while, recorrió toda la parte ordenada y comparó nodos
        if nodo_ordenado is desordenado:
            # desordenado es mayor O IGUAL a los ordenados, estaba en el lugar correcto
            ordenado = (
                desordenado  # se mueve un lugar y "agranda" la parte de ordenados
            )
        else:
            # desordenado es menor que nodo_ordenado (el primer mayor): hay que insertarlo justo antes
            # el nodo ordenado ahora apunta al que sigue en la parte desordenada, o sea,
            # que se saltee un nodo
            ordenado.siguiente = desordenado.siguiente
            # como nodo_ordenado es mayor que desordenado, hay que lograr
            # que desordenado apunte a ese nodo
            desordenado.siguiente = nodo_ordenado
            # falta el último paso: enganchar desde atrás.
            # si no hay anterior, desordenado pasa a ser la nueva cabeza;
            # si hay, anterior apunta a desordenado
            if anterior is None:
                coleccion._cabeza = desordenado
            else:
                anterior.siguiente = desordenado

        desordenado = ordenado.siguiente
