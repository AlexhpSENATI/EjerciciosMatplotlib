import matplotlib.pyplot as plt

# Datos para el gráfico
x = [0, 10]
y = [0, 10]

# Crear una figura y un conjunto de ejes
fig, ax = plt.subplots()

# Graficar la línea diagonal
ax.plot(x, y, label='Línea ')

# Añadir etiquetas y título
ax.set_xlabel('Eje X')
ax.set_ylabel('Eje Y')
ax.set_title(' Línea ')
ax.legend()

# Establecer los límites de los ejes
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)

# Mostrar el gráfico
plt.show()
