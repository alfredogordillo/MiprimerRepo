ci=int(input("Ingresa capital inicial"))
n=int(input("Ingresa nu´mero de meses"))
if ci<1000:
    i=0.08
    print(f"Interes es de: {i*100}%")
elif ci<5000:
    i=0.10
    print(f"Interes es de: {i*100}%")
elif ci>5000:
    i=0.12
    print(f"Interes es de: {i*100}%")
cf=ci*(1+(i*n))
intereses=ci*(i*n)
print(f"Capital final es :{cf}")
print(f"Cantidad intereses ganados: ${intereses}")
