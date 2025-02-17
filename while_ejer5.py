# Realizar un programa que, dados 2 números enteros positivos, realice
# la operación de dividirlos, pero sin utilizar las operaciones de división (/)
# ni residuo (%). Debe mostrar como resultado el cociente y el residuo de
# la división, ambos como enteros.

# def dividir_por_resta_repetida(dividendo, divisor):
#     cociente = 0
#     residuo = dividendo
    
#     while residuo >= divisor:
#         residuo -= divisor
#         cociente += 1
    
#     return cociente, residuo
   
dividendo = float(input("Ingrese el dividendo: "))
divisor=float(input("Ingrese el divisor: "))

cociente = 0
residuo = dividendo
    
while residuo >= divisor:
        
    residuo -= divisor
    cociente += 1
print(f"El cociente es: {cociente}")
print(f"El residuo: {residuo}")




