"""Funciones para gestionar el catálogo de recetas."""


def listar_catalogo(lista_diccionarios):
    """Muestra en pantalla la lista de diccionarios que devuelve cargar_texto()"""
    print(f"=== CATÁLOGO ===")
    for item in lista_diccionarios:
        print(f"🔹 ELEMENTO")
        # Recorremos cada propiedad (clave y valor) de este diccionario en particular
        for clave, valor in item.items():
            # dormato de lista de item con la clave en mayúsculas
            print(f"   • {clave.upper()}: {valor}")
        print("-" * 40) # Separador