class Receta:
    """Clase de una receta individual del recetario.

    Attributes:
    nombre: nombre de la receta (str).
    receta_id: identificador único de la receta (int).
    tiempo: tiempo de preparación en minutos (int).
    dificultad: nivel de dificultad de la receta (str).
    categoria: categoría a la que pertenece la receta (str).
    """
    def __init__(self, nombre, id, tiempo_min, dificultad, categoria):
        self.nombre = nombre
        self.receta_id = id
        self.tiempo = tiempo_min
        self.dificultad = dificultad
        self.categoria = categoria


    def mostrar_datos(self):
        print(f"=== Datos de la Receta {self.nombre}: ===")
        print(f"Tiempo de duración: {self.tiempo} min")
        print(f"Dificultad: {self.dificultad}")
        print(f"Categoría: {self.categoria}")