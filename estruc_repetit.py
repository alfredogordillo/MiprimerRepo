 #Actividad 2 - Estructuras repetitivas - Ejercicio 2  
bus=input("Ingrese el bus que desea Calcular A, B, C: ") 
km=int(input("Ingrese la cantidad de km: ")) 
npr=int(input("Ingrese la cantidad real de personas: ")) 
if npr<20: 
    npr=20 
precio_viaje=npr*km 
if bus == 'A': 
    tarifa=precio_viaje*2.0 
if bus == 'B': 
    tarifa=precio_viaje*2.5 
if bus == 'C': 
    tarifa=precio_viaje*3.0 
to=tarifa 
cp=to/npr 
print("El costo total es: ","$",to) 
print("El costo por persona es: ","$", cp) 
