# Protocolo de pruebas

Pruebas **manuales**. Cada fila es un caso. Ejecutar sobre el tag que entregan.

Leyenda de resultado: `pasa` / `no pasa` / `no corrido`.

Mínimos: 8 casos escritos en E2; ejecutados en E3; 15 de regresión en E6 (pila, cola, archivos, recursión, búsquedas).

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas |
| --- | --- | --- | --- | --- | --- | --- |
| P01 | E1 | Arrancar el programa y listar catálogo | dataset de la cátedra | lista no vacía, sin traceback |  |  |
| P02 | E1 | Elegir un ítem inexistente | id = -1 | mensaje claro, el menú sigue |  |  |
| P03 | E2 | Operación recursiva sobre un ítem con cadena | ver consigna §3.3 | imprime la cadena completa |  |  |
| P04 | E2 | Operación recursiva sobre un ítem sin derivados |  | solo el ítem (caso base) |  |  |
| P05 | E3 | Agregar a la colección principal hasta el tope | equipo de 6 / equivalente | el séptimo falla con excepción propia | pasa |  |
| P06 | E3 | Desapilar historial vacío | pila vacía | excepción propia, menú sigue | pasa |  |
| P07 | E3 | Desencolar cola vacía | cola vacía | excepción propia, menú sigue | pasa |  |
| P08 | E3 | Listar colección con el iterador | 2+ ítems | el orden coincide con las inserciones | pasa |  |
| P09 | E4 | Búsqueda lineal de un nombre que existe |  | lo encuentra |  |  |
| P10 | E4 | Búsqueda lineal de un nombre que no existe |  | no encontrado, sin traceback |  |  |
| P11 | E4 | Búsqueda binaria con catálogo desordenado |  | avisa o reordena; no da un falso hit |  |  |
| P12 | E4 | Ordenar por un criterio y después por otro |  | el orden cambia |  |  |
| P13 | E5 | Guardar texto (`.txt`), salir, volver a entrar |  | los datos siguen |  |  |
| P14 | E5 | Guardar binario y modificar un registro por id |  | al recargar, ese campo cambió |  |  |
| P15 | E5 | Abrir un binario truncado o con magia mala | archivo basura | excepción de archivo inválido |  |  |
| P16 | E2 | Desglosar una receta con más de un nivel de profundidad | id = 9 | imprime la lista completa |  |  |
| P17 | E2 | Desglosar una receta con un solo nivel de profundidad | id = 1 | imprime el id de la hoja |  |  |
| P18 | E2 | Arrancar el programa (carga de recetas y subrecetas) | recetas.txt, subrecetas.txt | el programa arranca sin errores, catálogo y tabla de subrecetas cargados |  |  |
| P19 | E2 | Ver el detalle de una receta que existe | id = 9 | muestra nombre, tiempo, dificultad y categoría |  |  |
| P20 | E2 | Ver el detalle de una receta que NO existe | id = -1 | avisa que no existe |  |  |
| P21 | E2 | Desglosar una receta que no existe | id = -1 | avisa que no existe |  |  |
| P22 | E4 | Ordenar por id con selección | id | orden numérico | pasa | Antes de usar `int(receta.receta_id)` salía "1, 10, 11...". Corregido en la clave. |
| P23 | E4 | Ordenar por nombre con inserción | nombre | orden alfabético | pasa | Lista alfabética correcta (Arroz con leche ... Tortilla de papas). |
| P24 | E4 | Ordenar por dos criterios a la vez | Nombre + Dificultad (inserción) | ordena por el principal; el secundario desempata | pasa | Se usa una tupla como clave. Con nombre único el desempate no se nota. |
| P25 | E4 | Búsqueda binaria de primer elemento | "Arroz con leche" | lo encuentra | pasa | Reordena y avisa antes de buscar. |
| P26 | E4 | Búsqueda binaria de último elemento | "Tortilla de papas" | lo encuentra | pasa | Caso donde más fácil falla el cálculo de `rango`. |
| P27 | E4 | Búsqueda binaria de nombre inexistente | "Pizza" | "No se encontró la receta." | pasa | Sin traceback, el menú sigue. |
| P28 | E5 | Guardar texto (`.txt`), salir, volver a entrar |  | Los datos siguen | pasa | Se comprobó la persistencia de los datos en TXT. |
| P29 | E5 | Guardar binario y modificar un registro por id; recargar desde BIN (9d) |  | Al recargar, ese campo cambió | pasa | Alta, baja y modificación probadas. Se verificó la persistencia al recargar desde BIN. |
| P30 | E5 | Abrir un binario truncado o con magia mala | Archivo truncado y archivo con magia incorrecta | Excepción de archivo inválido, sin traceback | pasa | Se probaron ambos casos; el programa muestra el error y continúa. |
| P31 | E5 | Cargar un TXT con una línea que tiene campos de más | `recetas_pruebas.txt` con una línea de 6 campos | `ArchivoInvalidoError`, el programa continúa | pasa | Se comprobó también durante la carga automática al iniciar. |

# Correcciones realizadas durante la revisión del programa E6

| Opción | Falla detectada | Corrección realizada | Estado |
|---|---|---|---|
| 2. Ver detalle | Al dejar vacío el ID de la receta, el programa generaba un error y se interrumpía. | Se corrigió el manejo de entradas vacías. | Corregida |
| 3. Buscar | Al dejar vacío el tipo de búsqueda, el programa generaba un error. | Se corrigió la validación de la entrada. | Corregida |
| 4. Ordenamiento | Al dejar vacío el tipo de ordenamiento o alguno de los criterios, el programa generaba un error. | Se corrigió la validación de las entradas. | Corregida |
| 6a. Colección principal (menú) | La opción 2, destinada a listar el menú, no mostraba los elementos cargados. | Se corrigió el funcionamiento de la opción para listar la colección. | Corregida |
| 6a. Colección principal (menú) | Se producía un error al trabajar con el ID de una receta debido a una conversión innecesaria a `str`. | Se eliminó la conversión sobrante. | Corregida |

# Pruebas complementarias — Opción 4: Ordenamiento

| ID | Categoría | Prueba realizada | Resultado |
|---|---|---|---|
| O01 | Tipo de ordenamiento | Dejar vacío el tipo de ordenamiento. | Pasa |
| O02 | Tipo de ordenamiento | Ingresar letras en lugar de un número. | Pasa |
| O03 | Tipo de ordenamiento | Ingresar 3 como tipo de ordenamiento. | Pasa |
| O04 | Tipo de ordenamiento | Seleccionar ordenamiento por selección (1). | Pasa |
| O05 | Tipo de ordenamiento | Seleccionar ordenamiento por inserción (2). | Pasa |
| O06 | Criterio principal | Dejar vacío el criterio principal. | Pasa |
| O07 | Criterio principal | Ingresar letras en el criterio principal. | Pasa |
| O08 | Criterio principal | Ingresar 0 como criterio principal. | Pasa |
| O09 | Criterio principal | Ingresar 6 como criterio principal. | Pasa |
| O10 | Criterio principal | Seleccionar ID como criterio principal (1). | Pasa |
| O11 | Criterio secundario | Dejar vacío el criterio secundario. | Pasa |
| O12 | Criterio secundario | Ingresar letras en el criterio secundario. | Pasa |
| O13 | Criterio secundario | Ingresar 0 como criterio secundario. | Pasa |
| O14 | Criterio secundario | Ingresar 6 como criterio secundario. | Pasa |
| O15 | Criterio secundario | Ingresar el mismo criterio principal y secundario (por ejemplo, 2 y 2). | Pasa |
| O16 | Ordenamiento válido | Selección: ordenar por ID y desempatar por nombre. | Pasa |
| O17 | Ordenamiento válido | Inserción: ordenar por ID y desempatar por nombre. | Pasa |
| O18 | Ordenamiento válido | Selección: ordenar por tiempo y desempatar por dificultad. | Pasa |
| O19 | Ordenamiento válido | Inserción: ordenar por categoría y desempatar por nombre. | Pasa |
| O20 | Ordenamiento válido | Comprobar que, ante valores iguales en el criterio principal, se aplique el secundario. | Pasa |
| O21 | Ordenamiento válido | Comprobar que el resultado se muestre correctamente. | Pasa |
| O22 | Persistencia | Comprobar que los archivos TXT y BIN se guarden después del ordenamiento. | Pasa |
| O23 | Persistencia | Cerrar y volver a ejecutar el programa. | Pasa |
| O24 | Persistencia | Comprobar que el catálogo conserve el ordenamiento realizado. | Pasa |
| O25 | Persistencia | Comprobar que los archivos TXT y BIN mantengan el mismo orden. | Pasa |

# Regresión
**Tabla de pruebas finales de la Entrega 6. Regresión.**

| ID | Entrega | Acción (pasos en el CLI) | Datos | Resultado esperado | Resultado | Notas | Resultado inicial | Falla detectada | Corrección realizada | Verificación posterior |
|---|---|---|---|---|---|---|---|---|---|---|
| P01 | E1 | Ejecutar `python -m src.main` | Catálogo de la cátedra | Inicia el programa y carga el catálogo |  | Se mostró el menú completo y se informó la carga de 30 ítems | Pasa | | — | Inicio y carga comprobados |
| P02 | E1 | Buscar Ítem inexistente: piza | Catálogo de la cátedra |  | Salida: "No se encontró la receta o no la ingresó.". No se rompe. |  | Pasa | | — |  |
| P03 | E2 | Opción 5: desglosar una receta con subrecetas | ID 9: Asado; subrecetas 1 y 2 | Obtener la receta y sus derivados | Pasa | Salida: `[9, 1, 2]` | Pasa | Ninguna | — | Se confirmó que 9 corresponde a Asado y que tiene las subrecetas 1 y 2 |
| P04 | E2 | Ejecutar la operación recursiva sobre un ítem sin derivados | Receta ID 2 | Devolver únicamente el ítem original | Pasa | Salida observada: [2] | — | — | — | Caso base comprobado |
| P05 | E3 | Agregar recetas a la colección principal hasta alcanzar el máximo | ID 7, al intentar superar el límite de 6 recetas | Rechazar la incorporación y mostrar un mensaje claro | Pasa | Mensaje observado: «El menú semanal está lleno (máximo 6)» | — | — | — | Límite de capacidad comprobado: se rechazó el séptimo elemento |
| P06 | E3 | Entrar a la colección principal (6a) y ejecutar Deshacer (opción 3) sin operaciones previas | Pila vacía | Informar que no hay elementos para deshacer, sin traceback | Pasa | Mensaje observado: «No hay elementos para deshacer.» | — | — | — | Excepción por pila vacía controlada correctamente |
| P07 | E3 | Entrar a la colección principal (6a) y ejecutar Siguiente turno (opción 4) con la cola vacía | Cola vacía | Informar que no hay elementos en la cola, sin traceback | Pasa | Mensaje observado: «No hay elementos en la cola.» | — | — | — | Excepción por cola vacía controlada correctamente |
| P08 | E3 | Recorrer la colección principal mediante el iterador (6a, opción 2) | Asado, Salsa criolla y Pesto, agregados en ese orden | Listar respetando el orden de inserción | Pasa | La salida mostró: Asado, Salsa criolla, Pesto | — | — | — | Orden de inserción comprobado correctamente |
| P09 | E4 | Elegir búsqueda lineal (opción 3) e ingresar el nombre de una receta existente | Pesto | Encontrar la receta y mostrar sus datos | Pasa | Salida: Pesto, 15 min, dificultad baja, categoría salsa | — | — | — | Búsqueda lineal comprobada correctamente |
| P10 | E4 | Elegir búsqueda lineal (opción 3) e ingresar el nombre de una receta inexistente | dragon | Informar que no se encontró la receta | Pasa | Mensaje observado: «No se encontró la receta.» | — | — | — | Búsqueda de elemento inexistente controlada correctamente |
| P11 | E4 | Elegir búsqueda binaria (opción 3) con el catálogo desordenado | Arroz con leche | Detectar que el catálogo está desordenado, ordenarlo y encontrar la receta | Pasa parcialmente | Mensaje observado: «¡Se ordenó la lista antes de buscar!». Encontró Arroz con leche y mostró sus datos. El programa ordena siempre, sin comprobar previamente si hace falta | — | No verifica si el catálogo ya está ordenado | — | Búsqueda binaria funcional; queda pendiente revisar la comprobación previa del orden |
| P12 | E4 | Elegir ordenamiento por selección (opción 4) y aplicar dos criterios | Criterio principal: dificultad; secundario: nombre | Ordenar por dificultad y, dentro de cada grupo, alfabéticamente | Pasa | La salida mostró las recetas agrupadas por dificultad y ordenadas alfabéticamente dentro de cada grupo. | — | — | — | Desempate comprobado correctamente |
| P13 | E5 | Guardar el catálogo en TXT, salir y volver a iniciar el programa | Catálogo con 31 recetas; ID 31: Arroz con leche | Recuperar los datos guardados al reiniciar | Pasa | Mensaje: «Catálogo guardado en .txt». Al reiniciar cargó 31 ítems. Se consultó el ID 31 y recuperó correctamente sus datos | — | — | — | Persistencia en TXT comprobada correctamente |
| P14 | E5 | Guardar el catálogo en binario, modificar una receta por ID, guardar nuevamente, reiniciar y cargar el archivo binario | ID 31: Arroz con leche | Recuperar la modificación realizada | Pasa | Tras cargar el .bin, el ID 31 conservó los valores modificados: 35 min, dificultad media, postre | — | — | — | Persistencia binaria comprobada correctamente |
| P15 | E5 | Intentar cargar un archivo binario inválido | Archivo con magia incorrecta | Capturar ArchivoInvalidoError y mostrar un mensaje claro, sin traceback | Pasa | Mensaje observado: «Archivo inválido: Magia incorrecta: este archivo no es de este TP.» | — | — | — | Manejo de archivo binario inválido comprobado correctamente |