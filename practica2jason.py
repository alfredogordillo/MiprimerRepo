import json

with open("nomina.json","r") as archivo:
    objeto_python=json.load(archivo)

print("Objeto Pyhton recupreado del archivo")
print(objeto_python)
