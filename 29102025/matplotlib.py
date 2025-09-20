import matplotlib.pyplot as plt

# Datos
categorias = ['A', 'B', 'C', 'D', 'E']
valores = [3, 7, 5, 8, 4]

# Crear gráfico de barras
plt.bar(categorias, valores)

# Agregar etiquetas
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfico de barras simple')

# Mostrar gráfico
plt.show()