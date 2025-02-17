
#Ejercicio 1
# paises={'Argentina': 'Buenos Aires', 'España': 'Madrid',
#          'Colombia': 'Bogota', 'Rep. Dominicana': 'Santo Domingo'}
# print(paises)

# def dic_paises(paises):
#     for capital in paises:
#         print(capital, paises[capital])

# dic_paises(paises)

#Ejercicio 2
def carga_productos():
    productos={}
    for f in range(3):
        nombre=input("Ingrese nombre producto:")
        precio=float(input("Ingrese precio: "))
        productos[nombre]=precio
    return productos
def imprime(productos):
    print("Listado de productos")
    for nombre in productos:
        print(nombre, productos[nombre])

articulos=carga_productos()

imprime(articulos)

#Ejercicio 3
