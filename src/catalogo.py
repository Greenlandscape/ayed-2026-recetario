"""Funciones para gestionar el catálogo de recetas."""

def listar_catalogo(lista_enlazada_recetas):
    """Muestra en pantalla la lista enlazada de objetos Receta."""
    print(f"=== CATÁLOGO ===")
    # Recorremos cada elemento, es decir, cada objeto tipo Receta
    for receta in lista_enlazada_recetas:
        print(f"🔹 ELEMENTO {receta.receta_id}")
        print(f"   • Nombre : {receta.nombre.upper()}")
        print(f"   • Tiempo : {receta.tiempo}")
        print(f"   • Dificultad : {receta.dificultad}")
        print(f"   • Categoría : {receta.categoria}")
        print("-" * 40) # Separador
    