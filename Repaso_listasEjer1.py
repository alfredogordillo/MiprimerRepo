# ejercicio 1
# Mostrar la cantidad de veces que se repite cada color.
# Eliminar los colores duplicados, dejando sólo uno de cada color.
# Crear una nueva lista con los colores violeta, negro, cyan, rosa y
# café.
# Crear una lista nueva concatenando las 2 listas de colores.
# Ordenar la lista resultante

# Lista inicial de colores
colores = ["azul", "verde", "rojo", "amarillo", "naranja", "verde", "gris", "blanco", "blanco",
           "amarillo", "rojo", "verde", "naranja", "azul", "verde"]

# 1. Mostrar la cantidad de veces que se repite cada color
from collections import Counter
conteo_colores = Counter(colores)
print("Cantidad de veces que se repite cada color:")
for color, cantidad in conteo_colores.items():
    print(f"{color}: {cantidad}")

# 2. Eliminar los colores duplicados, dejando solo uno de cada color
colores_unicos = list(set(colores))
print("\nColores sin duplicados:", colores_unicos)

# 3. Crear una nueva lista con los colores 'violeta', 'negro', 'cyan', 'rosa' y 'café'
nueva_lista = ["violeta", "negro", "cyan", "rosa", "café"]

# 4. Crear una lista nueva concatenando las dos listas de colores
lista_concatenada = colores_unicos + nueva_lista
print("\nLista concatenada:", lista_concatenada)

# 5. Ordenar la lista resultante
lista_ordenada = sorted(lista_concatenada)
print("\nLista ordenada:", lista_ordenada)



