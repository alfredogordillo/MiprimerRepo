import math

numero = int(input("Ingrese un número entero mayor o igual a 2: "))


if numero < 2:
    print(f"{numero} no es un número primo.")
else:
    es_primo = True 

   
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            es_primo = False  
            break  

    if es_primo:
        print(f"{numero} es un número primo.")
    else:
        print(f"{numero} no es un número primo.")