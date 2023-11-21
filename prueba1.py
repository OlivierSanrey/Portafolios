# Importar la biblioteca Pandas
import pandas as pd

# Supongamos que tienes un DataFrame llamado 'ventas' con las siguientes columnas: 'Fecha', 'Region', 'Ingresos'
# y que la columna 'Fecha' está en un formato de fecha

# Crear un DataFrame de ejemplo
data = {'Fecha': ['2023-01-01', '2023-01-01', '2023-02-01', '2023-02-01', '2023-01-01'],
        'Region': ['Norte', 'Sur', 'Norte', 'Sur', 'Norte'],
        'Ingresos': [1000, 1200, 800, 1500, 900]}

# Utilizar Pandas para crear un DataFrame a partir de los datos
ventas = pd.DataFrame(data)

# Convertir la columna 'Fecha' al formato de fecha utilizando Pandas
ventas['Fecha'] = pd.to_datetime(ventas['Fecha'])

# Filtrar por regiones utilizando Pandas
ventas_norte = ventas[ventas['Region'] == 'Norte']
ventas_sur = ventas[ventas['Region'] == 'Sur']

# Calcular ingresos medios por región utilizando Pandas
ingresos_medios_norte = ventas_norte['Ingresos'].mean()
ingresos_medios_sur = ventas_sur['Ingresos'].mean()

# Imprimir resultados
print(ventas)