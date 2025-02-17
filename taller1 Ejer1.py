peso=float(input("Ingresar peso:"))
altura=float(input("Ingresar altura:"))
IMC = peso / (altura** 2)

print(f"Tu IMC es:", round(IMC, 2))

if IMC < 18.5:
    print("tienes bajo peso")
elif IMC > 18.5 and IMC < 24.9:
    print("tienes peso normal")
elif IMC > 24.9 and IMC < 29.9:
    print("tienes sobrepeso")
elif IMC < 30:
    print("tienes obesidad")



        


    