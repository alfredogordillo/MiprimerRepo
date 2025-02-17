# import matplotlib.pyplot as plt
# # Datos
# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]

# # Crear gráfico
# plt.plot(x, y, marker='d',markerfacecolor='red', color ='blue', linestyle='--')

# # Personalizar
# # plt.scatter(x,y, marker='s',color='black')
# # plt.scatter(x,y, color='blue', label='Puntos de ebullición')
# # plt.plot(x,y, marker='d', markerfacecolor='black',label='linea contínua')
# # plt.title("Correlación de puntos")
# # plt.xlabel("Tiempo, s")
# # plt.ylabel("Temperatura, T")

# # Mostrar
# #plt.legend()
# plt.show()

# import seaborn as sns
# import matplotlib.pyplot as plt

# # Datos de ejemplo
# iris = sns.load_dataset("iris")

# # Crear gráfico de dispersión con Seaborn
# sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=iris)

# # Mostrar gráfico
# plt.show()

#plt.plot para linea continua

# import matplotlib.pyplot as plt

# # Datos
# x = ['Canada', 'España', 'USA', 'Ecuador', 'Mexico']
# y = [10, 20, 25, 30, 40]

# # Crear gráfico de linea
# plt.plot(x, y, color='red')

# # Personalizar
# plt.title("Población por país")
# plt.plot(x, y, color='red', label= 'linea de tendencia')
# plt.scatter(x,y, marker='d',color='yellow', label='Población')
# plt.xlabel("Países")
# plt.ylabel("Cantidad")
# plt.grid(axis='both', linestyle='--', alpha=0.8, linewidth=1.5)  # Líneas guía horizontales

# # Mostrar gráfico

# plt.legend()
# plt.show()

#plt.bar para grafico de barras

import matplotlib.pyplot as plt

# Datos
x = ['Canada', 'España', 'USA', 'Ecuador', 'Mexico']
y = [10, 20, 25, 30, 40]

# Crear gráfico de barras
plt.bar(x, y, color='red', edgecolor='blue')
# Personalizar
plt.title("Población por país")
plt.plot(x, y, color='red', label= 'linea de tendencia')
plt.scatter(x,y, marker='d',color='yellow', label='Población')
plt.xlabel("Países")
plt.ylabel("Cantidad")
plt.grid(axis='both', linestyle='--', alpha=0.8, linewidth=1.5)  # Líneas guía horizontales

# Mostrar gráfico

plt.legend()
plt.show()