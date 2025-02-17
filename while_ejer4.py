


capital = float(input("Ingrese el capital a invertir: "))

tiempo_meses = int(input("Ingrese el tiempo en meses: "))

if capital <= 1000:
    tasa_interes = 0.08
    ganancias_mensuales = capital * tasa_interes
    print(f"Tasa de interés: {tasa_interes * 100:.2f}%")
    print("Capital al finalizar cada mes:")
    total_capital = capital
    for i in range(tiempo_meses):
        print(f"Mes {i+1}: ${total_capital:.2f}")
        total_capital += ganancias_mensuales



    print(f"Ganancias totales: ${total_capital - capital:.2f}")






    

