import math
def es_primo(numero):
    if numero<2:
        return False
    for i in range(2,int(math.sqrt(numero))+1):
        if numero % i == 0:
            return False
        return True
    #Entrada de datos

numero = int(input("Ingrese un número mayor o igual a 2"))
    
    #Llamada a la función
if es_primo(numero):
        print(f"{numero} es un número primo")
else:
        print(f"{numero} no es un número primo")
                 