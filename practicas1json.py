import json 

# Creamos un diccionario en Python
nomina = {"name": "Jose", "edad": 29, "genero": "masculino"}

# Serializamos el objeto de Python para convertirlo en un texto JSON
nomina_json = json.dumps(nomina, indent=4)

# Imprimimos el JSON
print("JSON generado:")
print(nomina_json)

# Guardamos el JSON en un archivo llamado "nomina.json"
with open("nomina.json", "w") as archivo:
    json.dump(nomina, archivo, indent=4)  # ✅ Usamos json.dump() para escribir en el archivo

print("Archivo JSON guardado correctamente.")

# Leemos el JSON desde el archivo y lo deserializamos convirtiendolo en un objeto de Python
with open("nomina.json", "r") as archivo:
    objeto_python = json.load(archivo)  # ✅ Usamos json.load() para leer y convertir en objeto de Python

# Imprimimos el objeto recuperado
print("Objeto de Python recuperado del archivo:")
print(objeto_python)

