from src.dominio.receta import Receta

class Recetario:
    """Clase principal para guardar y manejar todas las recetas del sistema.

    Attributos:
        catalogo_recetas: lista de diccionarios con los datos de recetas.txt.
            Ej: {"id": "9", "nombre": "Empanadas de carne"}
        tabla_subrecetas: lista de diccionarios con los datos de subrecetas.txt.
            Ej: {"receta_id": "9", "subreceta_id": "2"}
    """
    def __init__(self):
        """Prepara el recetario vacío al instanciar la clase."""
        self.catalogo_recetas = []
        self.tabla_subrecetas = []

    def cargar_recetas(self, recetas):
        """Guarda en el catálogo los datos que ya leyó el main desde los archivos.
        Las recetas son una lista de diccionarios.
        """
        self.catalogo_recetas = recetas

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
        """Desglosa una receta en la lista completa de todos los ids de sub-recetas involucradas.
        
        Recibe receta_id (int). 
        
        Devuelve una lista de ints: el primer elemento es la receta original, seguida de todos sus subrecetas.
        Devuelve None si la receta no existe."""
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

    def mostrar_datos_receta(self, receta_id):
        """Busca en el catálogo el diccionario correspondiente a receta_id,
        crea un objeto Receta con esos datos y lo muestra por pantalla.

        receta_id es un int; se convierte a str para comparar contra
        los valores del catálogo, que son strings.
        
        Devuelve True si encontró y mostró la receta, False si no existe.
        """
        
        for receta in self.catalogo_recetas:
            if receta["id"] == str(receta_id):
                r = Receta(
                receta["nombre"],
                receta["id"],
                receta["tiempo_min"],
                receta["dificultad"],
                receta["categoria"]
            )
                r.mostrar_datos()
                return True
        return False
    