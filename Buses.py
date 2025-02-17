# Una compañía de viajes cuenta con tres tipos de autobuses (A, B y C), cada uno tiene un 
# precio por kilómetro recorrido por persona, los costos respectivos son $2.0, $2.5 y $3.0. Se 
# requiere determinar el costo total y por persona del viaje considerando que cuando éste se 
# presupuesta debe haber un mínimo de 20 personas, de lo contrario el cobro se realiza con 
# base en este número límite. 

Tipo_Bus=input("Ingrese el tipo de bus (A,B,C)").upper()
npr=int(input("Ingrese cantidad de personas"))
bus_A=2.0
bus_B=2.5
bus_C=3.0
km = int(input("Ingrese cantidad de kms"))
min_personas =20
if Tipo_Bus == 'A':
    precio_km =bus_A
elif Tipo_Bus == 'B':
    precio_km = bus_B
elif Tipo_Bus == 'C':
    precio_km = bus_C
else:
    print("Tipo de bus no válido")
    exit()
    
if npr<min_personas:
    npr = min_personas
print(f"El viaje se realizará con {npr} personas")

Costo_total= npr * km * precio_km

Costo_persona = Costo_total/npr
print(f"El costo total del viaje es: ${Costo_total:.2f}")
print(f"El costo por persona es : ${Costo_persona:.2f}")
