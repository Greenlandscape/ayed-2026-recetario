from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import PilaVaciaError

class Pila:
    """TAD pila implementado sobre ListaEnlazada (LIFO)."""

    def __init__(self):
        '''Crea una instancia de una pila implementada mediante una lista enlazada.'''
        self._items = ListaEnlazada()

    # Encapsula el acceso a la lista enlazada que implementa internamente la pila.
    def esta_vacia(self):
        return self._items.esta_vacia() # método de la clase ListaEnlazada
    
    def apilar(self, dato):
        """Agrega al tope. Equivale a insertar_al_inicio en la lista."""
        self._items.insertar_al_inicio(dato)
        
    def ver_tope(self):
        """Mira el del tope sin sacarlo."""
        if self.esta_vacia():
            raise PilaVaciaError("La pila está vacía.")
        return self._items._cabeza.dato
           
    def desapilar(self):
        """Sacá el tope. Si la pila está vacía, lanzá PilaVaciaError."""
        if self.esta_vacia():
            raise PilaVaciaError("No hay elementos para deshacer.")
        tope = self._items.buscar(self._items._cabeza.dato) # tomamos el nodo (eso devuelve buscar) tope para quitarlo luego
        self._items.eliminar(tope.dato)
        return tope.dato




