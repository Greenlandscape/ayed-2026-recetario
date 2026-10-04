from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColaVaciaError

class Cola:
    """TAD cola implementado sobre ListaEnlazada (FIFO)"""

    def __init__(self):
        self._items = ListaEnlazada()

    # Encapsula el acceso a la lista enlazada que implementa internamente la cola.
    def esta_vacia(self):
        return self._items.esta_vacia()

    def encolar(self, dato):
        """Agrega al final de la cola."""
        self._items.insertar_al_final(dato)

    def desencolar(self):
        """Quita del frente. Si la cola está vacía, lanzá ColaVaciaError."""
        if self.esta_vacia():
            raise ColaVaciaError("No hay elementos en la cola.")
        frente = self._items._cabeza.dato
        # primero lo eliminamos, luego lo devolvemos
        self._items.eliminar(frente)
        return frente

    def ver_frente(self):
        """Mira el del frente sin sacarlo."""
        if self.esta_vacia():
            raise ColaVaciaError("La cola está vacía.")
        return self._items._cabeza.dato
