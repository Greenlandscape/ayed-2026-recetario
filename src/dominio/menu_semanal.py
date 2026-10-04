from src.tads.lista_enlazada import ListaEnlazada
from src.excepciones import ColeccionLlenaError

class Menu_Semanal:
    '''pass'''
    def __init__(self, tope=6):
        """Crea un menú semanal con un tope máximo de recetas."""
        self._recetas = ListaEnlazada()
        self._tope = tope
    
    def agregar(self, receta):
        if self._recetas.tamanio() >= self._tope:
            raise ColeccionLlenaError(f"El menú semanal está lleno (máximo) {self._tope}")
        # si no está llena, agregamos la receta al final
        self._recetas.insertar_al_final(receta)
        
    def eliminar(self, receta):
        self._recetas.eliminar(receta)
    
    def listar(self):
        for receta in self._recetas:
            print(f" {receta}")