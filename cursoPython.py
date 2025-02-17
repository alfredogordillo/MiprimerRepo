# palabra='HOLA A TODOS'
# # print(palabra.count('a'))
# # print(palabra.index('d'))
# # print(palabra [:4]) # trae los primeros 4 caracteres de la palabra
# # print(palabra [4:]) # quita los 4 primeros de la palabra
# print(palabra.lower())

# palabra='Hola a todos'
# # print(palabra.isnumeric())  #si es numerico el valor de la palabra me sale True, else False.

# print(palabra.center(50))

# print(palabra.ljust(10))

# print(palabra.rjust(20))
# print(len(palabra))

# Ejercicio 2 WHILE
# conteo=0
# while (conteo<9):
#     print("El conteo es:",conteo)
#     conteo +=1
# print("Conteo completo")

# conteo=10
# while (conteo>2):
#     print("El conteo es:",conteo)
#     conteo -=2
# print("Conteo completo")

# Ejercicio 3 WHILE
# valor=int(input("Ingresar valor"))
# f=1
# while f <=valor:
#     print("Valor=",f)
#     f +=1
# print("gracias")

# Ejercicio 4 FOR
# for f in range(10):
#     print("Valor de f: ", f)

# Ejercicio 4 pero con WHILE
# f=0
# while f <10:
#     print("Valor de f: ", f)
#     f+=1

# Ejercicio 5 FOR
# for f in range(20,30,2): # primer numero es limite inf, segudo numero es lim superior y el 2 es paso.
#     print("Valor de f: ", f)
# print("fin de ciclo")

# Ejercicio 6 FOR
# suma=0
# for f in range(3):
#     valor=int(input("Ingrese valor"))
#     suma = suma + valor

# print("La suma es: ", suma)
# promedio=suma/10

# print("El promedio es: ", promedio)

# Ejercicio 7 FOR
# for f in 'Python':
#     print(f)

# # for f in 'python':
# #     print(f,end=' ')

# for f in 'python':
#     print("Eureka ",end=' ')

# Ejercicio 8 FOR
#arroba='@'
# cantidad=0
# mail=input("Ingrese se correo")
# for f in mail:
#     if f =='@':
#         cantidad +=1

# if cantidad ==1:
#     print("El correo es correcto")
# else:
#     print("El correo es incorrecto")

    # Ejercicio 9 FOR
# lista=['Juan','Pedro','Ana','Maria']
# for nombre in lista:
#     print("Hola", nombre)

   #Ejercicio 10 FOR tabla multiplicar
# valor=int(input("Ingresar tabla multiplicar"))
# print("Usted eligió la tabla de multiplicar:", valor)
# for i in range(11):
#     #print(f"{valor} x {i} = {valor*i}")
#     print(valor, 'x',i, '=', i*valor)

# Ejercicio 11 FOR
# for letra in 'programación':
#     print(letra)
#     if letra == 'm':
#         break

# print("letra encontrada :", letra,"fin bucle")

# Ejercicio 12 Fwhile  y  Break
# conteo=10
# while conteo>0:
#     print("Conteo en :", conteo)
#     conteo -=1
#     if conteo==5:
#         break
# print("Fin del conteo")

# Ejercicio 13 Continue
# for letra in 'programeción':
#     if letra == 'e':
#         print("Letra errónea")
#         continue
#     print(letra)

# print("Fin del bucle")

# Ejercicio 14 listas

#listas_enteros = [1,2,3,4,5,6]
#print(listas_enteros)
# listas_letras= ['a', 'b','c','d']
# #print(listas_letras)
# materias=['fisica', 'matamaticas', 'geometría', '1600', 'True']
# #print(materias)
# precios=[25.12,32.14,1.54,100]
# #print(precios)
# print(listas_enteros[2])
# print(listas_letras[2:5])
# print(materias[:3]) # los tres primeros
# print(precios[2:]) #los dos últimos

# listas_enteros.append(7) #Para agregar datos
# print(listas_enteros)
# materias.append('Chemistry')
# print(materias)
# del materias[2]

# print(materias)

# Ejercicio 15 Listas
listas_enteros = [1,2,3,4,5,5,5,6]
#print(listas_enteros)
listas_letras= ['a', 'b','c','d']
#print(listas_letras)
materias=['fisica', 'matamaticas', 'geometría', '1600', 'True']
#print(materias)
precios=[25.12,32.14,1.54,100]

# print(max(precios))
# print(len(listas_enteros))
# print(listas_enteros.count(5)) # me cuenta cuantos 5 hay en la lista
# materias.extend('fisica')

# print(materias)
# precios.pop(0)  # Elimina la posición que se seleccione de la lista.

# print(precios)
# precios.remove(100) # Elimina el valor de la lista, no la posición.

# print(precios)
# listas_letras.reverse()

# print(listas_letras)

for f in listas_letras:
   # print("Gracias",f, end=' ')  # se pone el end=' ' para ver horizontal
    print("Gracias",f, end='/')