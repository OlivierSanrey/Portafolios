import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo ventas.xlsx en un DataFrame
df = pd.read_excel('ventas.xlsx')

# Seleccionar las columnas relevantes para la gráfica
data = df[['Fecha', 'Producto', 'País', 'Cantidad vendida', 'Precio unitario', 'Total de ventas', 'Ingresos totales por región', 'Ingresos promedio por región', 'Tendencia de ventas a lo largo del tiempo']]

# Crear la gráfica de barras usando 'Producto' como etiquetas del eje x
ax = data.plot(kind='bar', x='País', figsize=(10, 6))  # 'País' se usará como etiquetas en el eje x
plt.title('Comparación de Ingresos y Gastos')
plt.xlabel('Regiones')
plt.ylabel('Cantidad')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.tight_layout()

# Mostrar la gráfica
plt.show()