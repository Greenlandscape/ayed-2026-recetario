from src.tads.nodo import Nodo

class ListaEnlazada:
    """TAD lista enlazada simple. No se usan list de Python por debajo. Se usan nodos."""

    def __init__(self):
        self._cabeza = None
        self._tamanio = 0

    def esta_vacia(self):
        return self._cabeza is None # Devuelve True (está vacía) o False según corresponda

    def tamanio(self):
        return self._tamanio

    def insertar_al_inicio(self, dato):
        self._cabeza = Nodo(dato, self._cabeza) # crea un nodo al inicio, o sea, reemplaza la cabeza 
        self._tamanio += 1
        
    def insertar_al_final(self, dato):
        # Ahora inserta al final, por lo tanto, debemos encontrar ese último nodo
        nuevo = Nodo(dato)
        if self.esta_vacia():
            self._cabeza = nuevo # si está vacía, el final es la cabeza
        else:
            # si no está vacía, hay que recorrerla hasta encontrar el último nodo
            actual = self._cabeza
            while actual.siguiente: # mientras en nodo actual tenga un siguiente...
                actual = actual.siguiente # se asigna ese siguiente al actual
            actual.siguiente = nuevo # terminó el while, en el último nodo asignamos el nuevo
        self._tamanio += 1
                   

    def insertar_ordenado(self, dato, clave):
        raise NotImplementedError # no lo pide en el mail de 3a entrega

    def eliminar(self, dato):
        # 3 casos: es vacía; el dato esta en la cabeza; otro.
        if self.esta_vacia():
            return
        if self._cabeza.dato == dato:
            self._cabeza = self._cabeza.siguiente # "corro" el nodo
            self._tamanio -= 1    
        # ahora recorremos la lista hasta hallar el dato a eliminar
        actual = self._cabeza
        while actual.siguiente: # no estaba en la cabecera, empezamos por el segundo nodo
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente # encontré el dato y "corro" el nodo
                self._tamanio -= 1
                return
            actual = actual.siguiente

    def buscar(self, dato):
        actual = self._cabeza
        while actual:
            if actual.dato == dato:
                return actual
            actual = actual.siguiente
        return None # terminó el while y no estaba 

    def __iter__(self):
        actual = self._cabeza
        while actual:
            yield actual.dato # yield permite que una función produzca valores uno por uno sin terminar su ejecución
            actual = actual.siguiente