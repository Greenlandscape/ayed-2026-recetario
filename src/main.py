from src.config import TEMA
from src.persistencia.texto import cargar_texto
from src.catalogo import listar_catalogo
from src.dominio.recetario import Recetario


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

ruta_recetas = "data/recetas.txt"
ruta_subrecetas = "data/subrecetas.txt"
# Type lista de dicc
recetas = cargar_texto(ruta_recetas)
subrecetas = cargar_texto(ruta_subrecetas)
# Instanciamos el recetario
Libro_recetas = Recetario()
# Cargamos las recetas y subrecetas
Libro_recetas.cargar_recetas(recetas)
Libro_recetas.cargar_subrecetas(subrecetas)

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def mostrar_menu():
    nombre = TEMAS.get(TEMA, TEMA or "(sin tema)")
    print()
    print(f"=== {nombre} — AyED C2 2026 ===")
    print("1. Listar catálogo")
    print("2. Ver detalle")
    print("3. Buscar")
    print("4. Ordenar")
    print("5. Operación recursiva")
    print("6. Colección principal (equipo / menú / playlist)")
    print("7. Historial (pila)")
    print("8. Cola")
    print("9. Guardar / cargar archivos")
    print("0. Salir")


def main():
    if TEMA not in TEMAS:
        print("Seteá TEMA en src/config.py: 'pokedex', 'recetario' o 'musica'.")
        return

    opcion = None
    while opcion != "0":
        mostrar_menu()
        opcion = input("> ").strip()
        if opcion == "0":
            print("Chau.")
        elif opcion == "1":
            listar_catalogo(recetas)
        elif opcion == "2":
            receta_id = int(input("Ingrese el id de la receta para mostrar detalles: "))
            if not Libro_recetas.mostrar_datos_receta(receta_id): # si existe la muestra, si no, muestra msj
                print("No existe una receta con ese id")
        elif opcion == "5":
            r_desglosar = int(input("Ingrese el número de la receta a desglosar: "))
            # any() recorre el catálogo y devuelve True si algún dict tiene id == receta_id (convertido a str). Corta al primer match.
            if not any(receta["id"] == str(r_desglosar) for receta in Libro_recetas.catalogo_recetas):
                print("No existe una receta con ese id")
            else:
                receta_desglosada = Libro_recetas.desglosar_subrecetas(r_desglosar)
                print(f"Desgloce: {receta_desglosada}")
        elif opcion in {"3", "4", "6", "7", "8", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
