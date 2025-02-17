ci=float(input("Ingresar capital inicial: "))
n=int(input("Ingresar número de meses: "))
if ci< 1000:
    i=0.08
    print(f"Interés : {i*100} %")
elif ci > 1000 and ci< 5000:
    i= 0.10
    print(f"Interés : {i*100} %")
elif ci > 5000:
    i= 0.12
    print(f"Interés : {i*100} %")
cf=ci*(1+(i*n))
intereses=ci*(i*n)

print(f"Capital final: {cf:.2f}")
print(f"Cantidad ganada en intereses: ${intereses:.2f}")


         
         