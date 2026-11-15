from src.config import TEMA
from src.catalogo import listar_catalogo
from src.excepciones import (
    ColeccionLlenaError,
    PilaVaciaError,
    ColaVaciaError,
    ArchivoInvalidoError,
    ItemNoEncontradoError,
)
from src.dominio.menu_semanal import Menu_Semanal
from src.tads.pila import Pila
from src.tads.cola import Cola
from src.dominio.receta import Receta
from src.algoritmos.busqueda import busqueda_lineal, busqueda_binaria
from src.algoritmos.ordenamiento import ordenar_seleccion, ordenar_insercion
from src.dominio.recetario import (
    Recetario,
    armar_catalogo_desde_txt,
    armar_subrecetas_desde_txt,
    filas_del_catalogo,
    ENCABEZADOS,
)
from src.persistencia.texto import (
    cargar_texto,
    guardar_texto,
    RUTA_RECETAS,
    RUTA_SUBRECETAS,
    RUTA_BIN,
)
from src.persistencia.binario import (
    guardar_binario,
    cargar_binario,
    actualizar_registro,
    posicion_del_id,
    alta_binario,
    baja_binario,
)


def cargar_catalogo(recetario):
    """Carga los datos desde los archivos .txt.
    Arma el catálogo como objetos del dominio y carga la tabla
    de subrecetas como una lista de diccionarios.
    """
    recetario.catalogo_recetas = armar_catalogo_desde_txt(RUTA_RECETAS)
    recetario.tabla_subrecetas = armar_subrecetas_desde_txt(RUTA_SUBRECETAS)


def guardar_todo():
    """Guarda el catálogo en los dos formatos. Memoria y archivos quedan iguales."""
    guardar_texto(
        RUTA_RECETAS, filas_del_catalogo(Libro_recetas.catalogo_recetas), ENCABEZADOS
    )
    guardar_binario(RUTA_BIN, Libro_recetas.catalogo_recetas)


TEMAS = {
    "pokedex": "Pokédex",
    "recetario": "Recetario",
    "musica": "Biblioteca musical",
}

# Instanciamos el recetario
Libro_recetas = Recetario()

# Al iniciar, cargamos el catálogo desde recetas.txt.
# Esto permite disponer de las recetas desde el comienzo,
# sin necesidad de realizar una carga manual desde el menú.
try:
    cargar_catalogo(Libro_recetas)
    print(
        f"Catálogo cargado desde TXT: "
        f"{Libro_recetas.catalogo_recetas.tamanio()} ítems."
    )
except ArchivoInvalidoError as error:
    print(f"Archivo inválido: {error}")

# Colección MenuSemanal con tope por defecto = 6
Menu_semana = Menu_Semanal()

cola_turnos = Cola()
pila_historial = Pila()


def pendiente():
    print("Todavía no está implementado. Completar en la entrega que corresponde.")


def menu_abm_recetas(recetario):
    while True:
        print("\n--- ABM del catálogo de recetas ---")
        print("1. Alta")
        print("2. Baja")
        print("3. Modificación")
        print("0. Volver")

        opcion = input("> ").strip()

        if opcion == "0":
            break

        elif opcion == "1":
            catalogo = recetario.catalogo_recetas

            nombre = input("Nombre de la receta: ").strip()
            tiempo = int(input("Tiempo en minutos: "))
            dificultad = input("Dificultad: ").strip() or None
            categoria = input("Categoría: ").strip()

            nuevo_id = max((receta.receta_id for receta in catalogo), default=0) + 1

            nuevo = Receta(nombre, nuevo_id, tiempo, dificultad, categoria)

            catalogo.insertar_al_final(nuevo)
            alta_binario(RUTA_BIN, nuevo)
            guardar_texto(RUTA_RECETAS, filas_del_catalogo(catalogo), ENCABEZADOS)

            print(f"Receta agregada: {nuevo.nombre} (ID: {nuevo_id})")

        elif opcion == "2":
            catalogo = recetario.catalogo_recetas
            id_borrado = int(input("ID de la receta que desea eliminar: "))

            try:
                posicion = posicion_del_id(catalogo, id_borrado)

                receta = None
                for item in catalogo:
                    if item.receta_id == id_borrado:
                        receta = item
                        break

                catalogo.eliminar(receta)
                baja_binario(RUTA_BIN, posicion)

                guardar_texto(RUTA_RECETAS, filas_del_catalogo(catalogo), ENCABEZADOS)

                print(f"Receta eliminada: {receta.nombre}")

            except ItemNoEncontradoError as e:
                print(e)

        elif opcion == "3":
            catalogo = recetario.catalogo_recetas
            id_modificado = int(input("ID de la receta que desea modificar: "))

            try:
                posicion = posicion_del_id(catalogo, id_modificado)

                receta = None
                for item in catalogo:
                    if item.receta_id == id_modificado:
                        receta = item
                        break

                print(f"Modificando: {receta.nombre}")
                receta.nombre = input("Nuevo nombre: ").strip()
                receta.tiempo = int(input("Nuevo tiempo en minutos: "))
                receta.dificultad = input("Nueva dificultad: ").strip() or None
                receta.categoria = input("Nueva categoría: ").strip()

                actualizar_registro(RUTA_BIN, posicion, receta)

                guardar_texto(RUTA_RECETAS, filas_del_catalogo(catalogo), ENCABEZADOS)

                print(f"Receta modificada: {receta.nombre}")

            except ItemNoEncontradoError as e:
                print(e)


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
    print("6a. Colección principal (menú)")
    print("6b. ABM del catálogo de recetas")
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

            # Regla de al E5: después de cada cambio al catálogo (cargar, ordenar, ABM), se guardan los
            # archivos. Así el .bin siempre tiene el MISMO orden que la memoria y la posición de un ítem es la misma
            guardar_todo()

        elif opcion == "5":
            r_desglosar = int(input("Ingrese el número de la receta a desglosar: "))
            # any() recorre el catálogo y devuelve True si algún dict tiene id == receta_id. Corta al primer match.
            if not any(
                receta.receta_id == r_desglosar
                for receta in Libro_recetas.catalogo_recetas
            ):
                print("No existe una receta con ese id")
            else:
                receta_desglosada = Libro_recetas.desglosar_subrecetas(r_desglosar)
                print(f"Desgloce: {receta_desglosada}")

        elif opcion == "6a":
            menu_coleccion(Menu_semana, pila_historial, cola_turnos, Libro_recetas)

        elif opcion == "6b":
            menu_abm_recetas(Libro_recetas)

        elif opcion == "7":
            print("\n--- Historial ---")
            pila_historial.mostrar()

        elif opcion == "8":
            print("\n--- Cola de preparación ---")
            cola_turnos.mostrar()

        elif opcion == "9":
            print(" a) Cargar catálogo desde el .txt de la cátedra")
            print(" b) Guardar catálogo en .txt")
            print(" c) Guardar catálogo en binario (.bin)")
            print(" d) Cargar catálogo desde binario (.bin)")
            sub = input(" Subopción > ").strip().lower()
            try:
                if sub == "a":
                    # Armamos el catálogo directamente como objetos del dominio
                    # y cargamos la tabla de subrecetas como lista de diccionarios
                    cargar_catalogo(Libro_recetas)
                    print(
                        f"Catálogo cargado: {Libro_recetas.catalogo_recetas.tamanio()} ítems."
                    )
                    # Regla de al E5: después de cada cambio al catálogo (cargar, ordenar, ABM), se guardan los
                    # archivos. Así el .bin siempre tiene el MISMO orden que la memoria y la posición de un ítem es la misma
                    guardar_todo()
                elif sub == "b":
                    guardar_texto(
                        RUTA_RECETAS,
                        filas_del_catalogo(Libro_recetas.catalogo_recetas),
                        ENCABEZADOS,
                    )
                    print("Catálogo guardado en .txt.")
                elif sub == "c":
                    guardar_binario(RUTA_BIN, Libro_recetas.catalogo_recetas)
                    print("Catálogo guardado en .bin.")
                elif sub == "d":
                    Libro_recetas.catalogo_recetas = cargar_binario(RUTA_BIN)
                    print(
                        f"Catálogo cargado desde .bin: "
                        f"{Libro_recetas.catalogo_recetas.tamanio()} ítems."
                    )
                    # Regla de al E5: después de cada cambio al catálogo (cargar, ordenar, ABM), se guardan los
                    # archivos. Así el .bin siempre tiene el MISMO orden que la memoria y la posición de un ítem es la misma
                    guardar_todo()
                else:
                    print("Subopción inválida.")
            except ArchivoInvalidoError as error:
                print(f"Archivo inválido: {error}")

        else:
            print("Opción inválida.")


if __name__ == "__main__":
    main()
