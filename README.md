# TP integrador - AyED C2 2026 — Comision 2 — Recetario - GRUPO 36

## Integrantes:
| Nombre | Mail | GitHub | DNI |
| --- | --- | --- |--- |
| Luciano Aranda | lucianodamian@gmail.com | github.com/Greenlandscape | 30.224.571 |
| Morena Gomez | moreegomezz00@gmail.com | github.com/morenagomez14 | 44.967.566 |
| Daiana Lozada | day2005micaela@gmail.com | github.com/DaianaL0z | 46.898.593 |

## Cómo ejecutarlo
Requiere Python 3.10 o superior. No necesita instalar dependencias externas: utiliza la biblioteca estándar de Python.

Desde la raíz del repositorio, ejecutar:

```text
python -m src.main
```

## Tema

**Tema elegido:** Recetario

## Entregas

Cada vencimiento se marca con un tag. Ver `GIT.md`.

| Tag | Vence |
| --- | --- |
| `preentrega` (opcional, solo repo) | domingo 30-ago-2026 23:59 |
| `entrega-1` | domingo 06-sep-2026 23:59 |
| `entrega-2` | domingo 20-sep-2026 23:59 |
| `entrega-3` | domingo 04-oct-2026 23:59 |
| `entrega-4` | domingo 01-nov-2026 23:59 |
| `entrega-5` | domingo 15-nov-2026 23:59 |
| `entrega-6` | domingo 22-nov-2026 23:59 |

Defensa oral (reemplaza el 2do parcial): 25 y 27-nov-2026.

La cátedra corrige el **tag**, no el último commit suelto de `main`.

El grupo se avisa por mail a diego.ambrossio@unab.edu.ar **y** angel.bianco@unab.edu.ar. Ver `GIT.md`.

## Qué hace
El programa permite:
- Listar el catálogo: visualizar las recetas disponibles.
- Ver detalle: consultar la información de una receta por su ID.
- Buscar recetas: mediante búsqueda lineal o binaria.
- Ordenar el catálogo: utilizando los algoritmos de selección e inserción, con criterios principales y secundarios.
- Operación recursiva: obtener el desglose de una receta y sus subrecetas.
- Gestionar el menú semanal: agregar, consultar y administrar una colección de hasta seis recetas.
- Historial: registrar operaciones y permitir deshacer acciones mediante una pila.
- Cola de preparación: administrar turnos mediante una estructura de tipo cola.
- Persistencia en TXT: guardar y recuperar el catálogo desde archivos de texto.
- Persistencia binaria: guardar y recuperar el catálogo en formato binario utilizando struct.

## Limitaciones conocidas
- El menú semanal admite un máximo de seis recetas.
- El sistema no verifica si una receta ya fue incorporada al menú semanal, por lo que permite agregarla más de una vez.
- No permite agregar ni modificar subrecetas desde la aplicación; estas relaciones se cargan a partir de los archivos del catálogo.
