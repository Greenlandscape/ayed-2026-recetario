from src.config import TEMA
from src.persistencia.texto import cargar_texto
from src.catalogo import listar_catalogo
from src.dominio.recetario import Recetario
from src.excepciones import ColeccionLlenaError, PilaVaciaError, ColaVaciaError
from src.dominio.menu_semanal import Menu_Semanal
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.dominio.receta import Receta
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion

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
            listar_catalogo(
                Libro_recetas.catalogo_recetas
            )  # se modificó la función para usar lista enlazada
        elif opcion == "2":
            receta_id = int(input("Ingrese el id de la receta para mostrar detalles: "))
            if not Libro_recetas.mostrar_datos_receta(
                receta_id
            ):  # si existe la muestra, si no, muestra msj
                print("No existe una receta con ese id")
        elif opcion == "3":
            opcion = int(input("Elija el tipo de búsqueda: 1) Lineal 2) Binaria: "))
            nombre_r = input(
                "Ingrese el nombre a buscar (Ejemplos: Sofrito, Pesto, Asado): "
            )
            if opcion == 1:
                # Obtenemos el atributo nombre de cada receta mediante una función lambda.
                receta_buscada = busqueda_lineal(
                    Libro_recetas.catalogo_recetas,
                    nombre_r,
                    lambda receta: receta.nombre,
                )
                if receta_buscada is not None:
                    receta_buscada.mostrar_datos()
                else:
                    print("No se encontró la receta.")
            elif opcion == 2:
                obtener_nombre = lambda receta: receta.nombre
                ordenar_insercion(Libro_recetas.catalogo_recetas, obtener_nombre)
                print("¡Se ordenó la lista antes de buscar!")
                receta_buscada = busqueda_binaria(
                    Libro_recetas.catalogo_recetas,
                    nombre_r,
                    obtener_nombre,
                )
                if receta_buscada is not None:
                    receta_buscada.mostrar_datos()
                else:
                    print("No se encontró la receta.")
            else:
                print("Opción inválida")
        elif opcion == "4":
            tipo = int(
                input("Elija el tipo de ordenamiento: 1) Selección 2) Inserción: ")
            )
            print("Ordenar por:")
            print("1) id")
            print("2) Nombre")
            print("3) Tiempo en minutos")
            print("4) Dificultad")
            print("5) Categoría")
            principal = int(input("Criterio principal: "))
            secundario = int(input("Criterio secundario (desempate): "))

            claves = {
                1: lambda receta: int(receta.receta_id),
                2: lambda receta: receta.nombre,
                3: lambda receta: int(receta.tiempo),
                4: lambda receta: receta.dificultad,
                5: lambda receta: receta.categoria,
            }
            clave_1 = claves[principal]
            clave_2 = claves[secundario]
            obtener_clave = lambda receta: (clave_1(receta), clave_2(receta))
            # obtener_clave devuelve una tupla (criterio principal, criterio secundario).
            # Los algoritmos no cambian: comparan tuplas, y Python las compara
            # elemento por elemento (el secundario solo desempata).

            if tipo == 1:
                ordenar_seleccion(Libro_recetas.catalogo_recetas, obtener_clave)
                print("¡Ordenado por selección!")
            else:
                ordenar_insercion(Libro_recetas.catalogo_recetas, obtener_clave)
                print("¡Ordenado por inserción!")

            print("Resultado: ")
            for receta in Libro_recetas.catalogo_recetas:
                print(f"{receta.nombre} - {clave_1(receta)} - {clave_2(receta)}")

        elif opcion == "5":
            r_desglosar = int(input("Ingrese el número de la receta a desglosar: "))
            # any() recorre el catálogo y devuelve True si algún dict tiene id == receta_id (convertido a str). Corta al primer match.
            if not any(
                receta.receta_id == str(r_desglosar)
                for receta in Libro_recetas.catalogo_recetas
            ):
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

        elif opcion in {"9"}:
            pendiente()
        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
