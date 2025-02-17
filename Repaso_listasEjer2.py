# EJERCICIO 2
# Crear una lista que contenga los años desde 1980 a 2024.
# Crear una nueva lista con los años que han sido bisiestos (el año 1980
# fue bisiesto).
# Eliminar los años bisiestos de la primera lista.
# Concatenar las 2 listas en una nueva y ordenarla.
# Reemplazar en la nueva lista cada año bisiesto por la palabra “Bisiesto”.
# Eliminar de todas las listas el año de cuarentena



# 1. Crear una lista que contenga los años desde 1980 a 2024
años = list(range(1980, 2025))
print("Lista de años de 1980 a 2024:", años)

# 2. Crear una nueva lista con los años que han sido bisiestos
def es_bisiesto(año):
    return (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)

años_bisiestos = [año for año in años if es_bisiesto(año)]
print("\nLista de años bisiestos:", años_bisiestos)

# 3. Eliminar los años bisiestos de la primera lista
años_no_bisiestos = [año for año in años if año not in años_bisiestos]
print("\nLista de años no bisiestos:", años_no_bisiestos)

# 4. Concatenar las dos listas en una nueva y ordenarla
lista_concatenada = sorted(años_no_bisiestos + años_bisiestos)
print("\nLista concatenada y ordenada:", lista_concatenada)

# 5. Reemplazar en la nueva lista cada año bisiesto por la palabra "Bisiesto"
lista_reemplazada = ["Bisiesto" if año in años_bisiestos else año for año in lista_concatenada]
print("\nLista con años bisiestos reemplazados:", lista_reemplazada)

# 6. Eliminar de todas las listas el año de cuarentena (2020)
lista_final = [año for año in lista_reemplazada if año != 2020]
print("\nLista final sin el año de cuarentena (2020):", lista_final)