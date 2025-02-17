# import json

# # Diccionario de Python
# persona = {
#     "nombre": "Carlos",
#     "edad": 28,
#     "ciudad": "Madrid"
# }

# # Serializar: Convertir diccionario a JSON
# json_persona = json.dumps(persona, indent=4)

# print(json_persona)  # Ahora es un texto en formato JSON


# import json

# # Diccionario con datos de una persona
# persona = {
#     "nombre": "Carlos",
#     "edad": 28,
#     "ciudad": "Madrid"
# }

# # Abrir un archivo en modo escritura y guardar el JSON
# with open("persona.json", "w") as archivo:
#     json.dump(persona, archivo, indent=4)

# print("Archivo JSON guardado exitosamente.")

# Ejemplo de Serialización

import json

# Creamos un diccionario en Python
persona = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Bogotá"
}

#Serializamos el diccionario a una cadena JSON
json_persona = json.dumps(persona)

print("Objeto en JSON:")
print(json_persona)

 #Ejemplo de Deserialización
#Convertimos la cadena JSON de nuevo a un diccionario de Python
import json
objeto_python = json.loads(json_persona)

print("\nObjeto de Python:")
print(objeto_python)

# Accedemos a un valor específico del diccionario
print("\nNombre de la persona:", objeto_python["nombre"])