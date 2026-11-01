# Informe del TP

Completar y hacer crecer en cada entrega. No hace falta prosa larga: oraciones claras y tablas.

## 1. Grupo y tema

- Tema: Recetario.
- Por qué lo eligieron (5–8 líneas): El tema del recetario es sencillo y de fácil comprensión global. Nos permite enfocarnos en el código y en los detalles técnicos del proyecto. Además, las recetas y sus ingredientes son elementos fáciles de identificar y relacionar. Estimamos que la simplicidad de la idea es una ventaja a la hora de incorporar estructuras de datos más complejas, como los TADs, y desarrollar las clases que representarán los objetos del dominio en las próximas entregas.

## 2. Modelo

Qué es un ítem del catálogo. Qué es mutable y qué no (E1). Cómo se relacionan catálogo, colección principal, pila y cola.

Un item del catálogo es un elemento de la lista de diccionarios que se obtiene al cargar los txt. Cada elemento de esa lista es un diccionario de una receta en particular. Hasta la entrega 1 utilizamos: Mutables: listas, diccionarios. Inmutables: strings. 

```text
(pueden pegar un diagrama ASCII o una lista de clases)
```

## 3. Recursión (E2)

- Función: Libro_recetas.desglosar_subrecetas(id)
- Caso base: si la receta no tiene subrecetas → devolver [id] (concatenando a una lista)
- Caso recursivo: [id] + Libro_recetas.desglosar_subrecetas(subreceta siguiente)
- Traza de un ejemplo real del dataset:
    Traza para Asado (id 9): según subrecetas.txt, tiene dos subrecetas: 1 y 2.
    Llamada 1: Libro_recetas.desglosar_subrecetas(9) → tiene subrecetas 1 y 2.
    → devuelve [9] + Libro_recetas.desglosar_subrecetas(1)
    Llamada 2: Libro_recetas.desglosar_subrecetas(1) → no tiene subrecetas, es hoja.
    → devuelve [1]
    Llamada 3: Libro_recetas.desglosar_subrecetas(2) → no tiene subrecetas, es hoja.
    → devuelve [2]
    Resultado: [9] + [1] + [2] = [9, 1, 2]


## 4. TADs (E3)

| TAD | Operaciones | Invariante |
| --- | --- | --- |
| ListaEnlazada |  |  |
| Pila |  |  |
| Cola |  |  |

Dónde se usa cada uno en el dominio.

## 5. Complejidad (E4)

| Operación | Tiempo | Espacio | Por qué |
| --- | --- | --- | --- |
| Listar catálogo | O(n) | O(1) | Recorre los n elementos de la colección una sola vez mediante un iterador. |
| Búsqueda lineal | O(n) en el peor caso / O(1) en el mejor caso | O(1) | Recorre los elementos hasta encontrar el buscado o llegar al final de la colección. |
| Búsqueda binaria | O(n) | O(1) | En cada comparación descarta la mitad del rango de búsqueda pero para llegar al nodo medio tiene que recorrer nodos desde iqz. Eso suma n. El problema aquí es que para buscar hay que ordenar antes, así que el costo real de esa opción desde el menú está dominado por el ordenamiento (O(n²)) |
| Ordenar por selección | O(n²) en todos los casos | O(1) | Utiliza dos bucles anidados. Realiza aproximadamente n²/2 comparaciones para encontrar los mínimos e intercambiar elementos. |
| Ordenar por inserción | O(n²) en todos los casos | O(1) | Como la lista no permite retroceder, la búsqueda del lugar siempre parte de la cabeza y recorre la parte ordenada, incluso si ya estaba ordenada. |
| Ver detalle de un ítem | O(n) en el peor caso / O(1) en el mejor | O(1) | Recorre la lista enlazada con el iterador, comparando receta_id en cada nodo hasta encontrarlo o llegar al final. |

Mediciones (`time.perf_counter`):

| Operación | n | segundos |
| --- | --- | --- |
| Búsqueda lineal (nombre) | 30 | 0.000011 |
| Búsqueda lineal (n × 10) | 300 | 0.000247 |
| Búsqueda binaria (nombre) | 30 | 0.000004 |
| Búsqueda binaria (n × 10) | 300 | 0.000016 |
| Ordenar por selección | 30 | 0.000115 |
| Ordenar por selección (n × 10) | 300 | 0.021400 |
| Ordenar por inserción | 30 | 0.000055 |
| Ordenar por inserción (n × 10) | 300 | 0.006177 |

**Cómo se midió:** con `time.perf_counter()`. En las búsquedas se promedian 100 repeticiones sobre el peor caso (un nombre inexistente, así se recorre todo el rango), con la lista ya ordenada. En los ordenamientos se mide una sola ejecución sobre una lista desordenada recién armada. Para n × 10 se repitió el catálogo 10 veces en una `ListaEnlazada` nueva.

**Análisis:**

Al pasar de 30 a 300 recetas (10 veces más datos), el tiempo de cada operación creció así:

- **Búsqueda lineal:** tardó unas 22 veces más. Es el crecimiento esperado para O(n): más datos, más nodos por recorrer. (Dio más de 10 veces por costos propios de la máquina, pero la tendencia es lineal.)
- **Búsqueda binaria:** tardó solo unas 4 veces más, bastante menos que la lineal. Hace pocas comparaciones, porque descarta la mitad del rango en cada vuelta. Igual no es O(log n) puro: como la lista enlazada no tiene índices, llegar al nodo del medio exige recorrer nodos, y por eso su cota real es O(n). Con tamaños tan chicos, ese recorrido pesa poco.
- **Ordenar por inserción:** tardó unas 112 veces más. Con 10 veces más datos, el tiempo se multiplica por cerca de 100, que es lo esperable para O(n²).
- **Ordenar por selección:** tardó unas 186 veces más, también cerca de las 100 veces que predice O(n²).

**Conclusión:** buscar crece de a poco (10 veces más datos, entre 4 y 22 veces más tiempo), mientras que ordenar se dispara (10 veces más datos, más de 100 veces más tiempo). Por eso conviene ordenar una sola vez y buscar muchas.

## 6. Persistencia (E5)

- Layout del registro binario (campos, `struct`, anchos):
- Header:
- Cómo se actualiza un registro por posición:

## 7. Reparto de trabajo (E6)

| Integrante | Qué hizo | Qué puede defender |
| --- | --- | --- |
|  |  |  |
