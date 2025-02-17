import math

def es_primo(numero):
    if numero < 2:  # Los números menores a 2 no son primos
        return False
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:  # Si el número es divisible por i, no es primo
            return False
        return True  # Si no se encontraron divisores, es primo


# Entrada de datos
numero = int(input("Ingrese un número entero mayor o igual a 2: "))

# Verificar si el número es primo y mostrar el resultado
if es_primo(numero):
    print(f"{numero} es un número primo.")
else:
    print(f"{numero} no es un número primo.")