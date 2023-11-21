import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo ventas.xlsx en un DataFrame
df = pd.read_excel('ventas.xlsx')

# Seleccionar las columnas relevantes para la gráfica (excluyendo 'Fecha')
data = df[['Cantidad vendida', 'Precio unitario', 'Total de ventas', 'Ingresos totales por región', 'Ingresos promedio por región', 'Tendencia de ventas a lo largo del tiempo']]

# Crear un gráfico de tipo telaraña
labels = data.columns.tolist()
stats = data.mean().tolist()
stats += stats[:1]

angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

ax.fill(angles, stats, color='blue', alpha=0.25)
ax.plot(angles, stats, color='blue', linewidth=2)

ax.set_yticklabels([])
plt.xticks(angles[:-1], labels, color='black', size=10)
plt.show()
