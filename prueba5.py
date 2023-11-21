import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('ventas.xlsx')

data = df[['Cantidad vendida', 'País', 'Precio unitario', 'Total de ventas', 'Ingresos totales por región', 'Ingresos promedio por región', 'Tendencia de ventas a lo largo del tiempo']]

plt.figure(figsize=(8, 6))

for column in data.columns:
    if column == 'País':
        continue  # Ignora la columna de los países
    plt.plot(data[column], marker='o', label=column)

for i, pais in enumerate(data['País']):
    for column in data.columns:
        if column == 'País':
            continue
        plt.annotate(pais, (i, data[column][i]))

plt.xlabel('Fila')
plt.ylabel('Cantidad')
plt.title('Gráfico Lineal')
plt.legend()
plt.grid(True)

plt.show()