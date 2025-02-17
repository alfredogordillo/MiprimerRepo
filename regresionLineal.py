import numpy as np  
import matplotlib.pyplot as plt  
from sklearn.linear_model import LinearRegression  

# Datos de meses (1 = enero, 2 = febrero, etc.) y ventas correspondientes
meses = np.array([1, 2, 3, 5, 6]).reshape(-1, 1)  # Falta el mes 4  
ventas = np.array([10, 15, 20, 30, 35])  # Ventas en cada mes

# Crear y entrenar el modelo de regresión lineal  
modelo = LinearRegression()  
modelo.fit(meses, ventas)  

# Predecir las ventas del mes 4  
mes_faltante = np.array([[4]])  
ventas_predichas = modelo.predict(mes_faltante)  

print(f"Ventas estimadas para el mes 4: {ventas_predichas[0]:.2f}")

# Graficar los datos y la predicción  
plt.title("Regresión lineal",color="red")
plt.scatter(meses, ventas, color='blue', label="Datos reales")  
plt.plot(meses, modelo.predict(meses), color='red', label="Regresión Lineal")  
plt.scatter(mes_faltante, ventas_predichas, color='green', marker='o', label="Predicción (mes 4)")  
plt.xlabel("Mes")  
plt.ylabel("Ventas")  
plt.legend()  
plt.show()