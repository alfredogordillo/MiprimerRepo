#Paso 1: Instalar librerías necesarias
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error

#Paso 2: Crear un data set ficticio
data = {
    'Metros_Cuadrados': [50, 60, 75, 80, 100, 120, 150, 200, 250, 300],
    'Precio': [150000, 180000, 220000, 250000, 300000, 350000, 400000, 500000, 600000, 700000]
}
df = pd.DataFrame(data)

#Paso 3: Dividir datos en entrenamiento y de prueba
X = df[['Metros_Cuadrados']]
y = df['Precio']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Paso 4: Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(X_train, y_train)

#Paso 5: Predecir el precio de un nuevo metro cuadrado
y_pred = modelo.predict(X_test)

#Paso 6: Evaluar el modelo
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'Error Absoluto Medio (MAE): {mae:.2f}')
print(f'Raíz de la media de los errores al cuadrado (RMSE): {rmse:.2f}')

#Paso 7: Visualizar la regresión
plt.title('Modelos predictivos -Machine Learning')
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, modelo.predict(X), color='red', label='Línea de regresión')
plt.xlabel('Metros Cuadrados')
plt.ylabel('Precio')
plt.legend()
plt.show()