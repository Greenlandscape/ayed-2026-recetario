from src.config import TEMA
from src.persistencia.texto import cargar_texto
from src.catalogo import listar_catalogo
from src.dominio.recetario import Recetario
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.dominio.menu_semanal import Menu_Semanal
from src.tads.pila import Pila
from src.tads.cola import Cola


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

# colección MenuSemanal con tope por defecto = 6
Menu_semana = Menu_Semanal()

cola_turnos = Cola()
pila_historial = Pila()

def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def menu_coleccion(menu_semanal, pila_historial, cola_turnos, recetario):
    """Muestra y gestiona el menú de la colección principal."""
    while True:
        print("\n--- Colección Principal ---")
        print("1. Agregar al Menú semanal")
        print("2. Listar menú")
        print("3. Deshacer (pila)")
        print("4. Siguiente turno (cola)")
        print("5. Agregar turno (cola)")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            receta_id = int(input("ID de la receta: "))

            receta_encontrada = None
            for receta in recetario.catalogo_recetas:
                if receta.receta_id == str(receta_id):
                    receta_encontrada = receta
                    break

            if receta_encontrada is None:
                print("No existe una receta con ese id")
            else:
                try:
                    menu_semanal.agregar(receta_encontrada)
                    print(f"✅ Agregada: {receta_encontrada.nombre}")
                except ColeccionLlenaError as e:
                    print(f"❌ {e}")

        elif opcion == "2":
            menu_semanal.listar()

        elif opcion == "3":
            try:
                item = pila_historial.desapilar()
                print(f"↩ Deshecho: {item.nombre}")
            except PilaVaciaError as e:
                print(f"❌ {e}")

        elif opcion == "4":
            try:
                item = cola_turnos.desencolar()
                pila_historial.apilar(item)
                print(f"→ Turno atendido: {item.nombre}")
            except ColaVaciaError as e:
                print(f"❌ {e}")
        
        elif opcion == "5":
            receta_id = int(input("ID de la receta para preparar: "))

            receta_encontrada = None
            for receta in recetario.catalogo_recetas:
                if receta.receta_id == str(receta_id):
                    receta_encontrada = receta
                    break

            if receta_encontrada is None:
                print("No existe una receta con ese id")
            else:
                cola_turnos.encolar(receta_encontrada)
                print(f"✅ Turno agregado: {receta_encontrada.nombre}")

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
            listar_catalogo(Libro_recetas.catalogo_recetas) # se modificó la función para usar lista enlazada
        elif opcion == "2":
            receta_id = int(input("Ingrese el id de la receta para mostrar detalles: "))
            if not Libro_recetas.mostrar_datos_receta(receta_id): # si existe la muestra, si no, muestra msj
                print("No existe una receta con ese id")
        elif opcion == "5":
            r_desglosar = int(input("Ingrese el número de la receta a desglosar: "))
            # any() recorre el catálogo y devuelve True si algún dict tiene id == receta_id (convertido a str). Corta al primer match.
            if not any(receta.receta_id == str(r_desglosar) for receta in Libro_recetas.catalogo_recetas):
                print("No existe una receta con ese id")
            else:
                receta_desglosada = Libro_recetas.desglosar_subrecetas(r_desglosar)
                print(f"Desgloce: {receta_desglosada}")
        elif opcion == "6":
            menu_coleccion(Menu_semana, pila_historial, cola_turnos, Libro_recetas)
            
        elif opcion == "7":
            print("\n--- Historial ---")
            pila_historial.mostrar()

        elif opcion == "8":
            print("\n--- Cola de preparación ---")
            cola_turnos.mostrar()
            
        elif opcion in {"3", "4", "9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
