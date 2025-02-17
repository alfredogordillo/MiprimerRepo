Peso=int(input("Ingresa tu peso en kg "))
Estatura=float(input("Ingresa tu estatura en metros "))
imc= Peso/Estatura**2
if imc <18.5:
    print("Tienes bajo peso")
elif imc > 18.5 and imc < 24.5:
    print("Tienes peso normal")
elif imc >24.6 and imc < 29.9:
    print("Tienes sobrepeso")
else:
    print("Tienes obesidad")