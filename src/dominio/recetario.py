from src.dominio.receta import Receta
from src.tads.lista_enlazada import ListaEnlazada

class Recetario:
    """Clase principal para guardar y manejar las recetas del sistema.

    Atributos:
    catalogo_recetas: lista enlazada de objetos Receta.
    tabla_subrecetas: lista de diccionarios con las relaciones entre
        recetas y subrecetas.
    Ej: {"receta_id": "9", "subreceta_id": "2"}
    """
    # los 3 siguientes métodos se modifican para usar lista enlazada
    def __init__(self):
        """Prepara el recetario vacío al instanciar la clase."""
        self.catalogo_recetas = ListaEnlazada()
        self.tabla_subrecetas = []

    def cargar_recetas(self, recetas):
        """Carga las recetas en el catálogo como objetos Receta.
        Recibe una lista de diccionarios con los datos de las recetas,
        crea un objeto Receta por cada diccionario y lo agrega al catálogo
        implementado mediante una lista enlazada."""
        for diccionario in recetas: # recorremos la lista de diccs
            # creamos el objeto receta con cada elemento
            receta = Receta(
                diccionario["nombre"], 
                diccionario["id"], 
                diccionario["tiempo_min"], 
                diccionario["dificultad"], 
                diccionario["categoria"]
                )
            self.catalogo_recetas.insertar_al_final(receta)
            

    def mostrar_datos_receta(self, receta_id):
        """Busca una receta por id y muestra sus datos.
        Recibe el id de una receta, la busca en el catálogo
        mediante el iterador de la lista enlazada y muestra sus datos
        si la encuentra.
        Devuelve True si la receta existe y False si no se encuentra.
        """      
        for receta in self.catalogo_recetas: # uso el iterador de la lista enlazada
            if receta.receta_id == receta_id: # el iterador devuevle devuelve el dato almacenado en cada nodo, que en este caso es un objeto Receta
                receta.mostrar_datos()
                return True
        return False
    
        
    # Los siguientes métodos se mantienen de la entrega 2
    def cargar_subrecetas(self, subrecetas):
        """Guarda en un atributo los datos que ya leyó el main desde los archivos.
        Las subrecetas son una lista de diccionarios.
                """
        self.tabla_subrecetas = subrecetas

    def subrecetas(self, receta_id):
        """Busca las subrecetas de una receta particular.

        La lista de diccs es del tipo {"receta_id": "9", "subreceta_id": "1"} con values str. 
        Viene de subrecetas.txt.
        receta_id es un int, lo convierte para comparar contra los strings del diccionario.

        Devuelve una lista de id de subrecetas (int)
        ej: [1, 2]"""
        lista_id_subrecetas = []

        # Recorre cada dicc y compara los id de la receta, cuando coincide, agrega los id de subrecetas a la lista.
        for dicc in self.tabla_subrecetas:
            if dicc["receta_id"] == str(receta_id):
                 lista_id_subrecetas.append(int(dicc["subreceta_id"]))
        return lista_id_subrecetas   
     
    def desglosar_subrecetas(self, receta_id):
        """Desglosa una receta en la lista completa de todos sus ids de subrecetas.

        Recibe receta_id (int).

        Devuelve una lista de ints: el primer elemento es la receta original,
        seguida de todos sus subrecetas.
        """
        subs = self.subrecetas(receta_id)
        # se arma con el método subrecetas, es decir, devuelve una lista de id de subrecetas (int)
        if not subs:
            return [receta_id] # Caso base, "hoja" (nodos que no tienen hijos)
        resultado = [receta_id]
        # Arriba se creó una lista con el ele pasado por parámetro, tanto si existen
        # subrecetas como si no
        for s in subs:
            resultado += self.desglosar_subrecetas(s)
        return resultado