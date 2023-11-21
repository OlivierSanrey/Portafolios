import pandas as pd

# Configurar Pandas para mostrar todas las filas y columnas
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

# Cargar el archivo alquiler.xlsx en un DataFrame
df = pd.read_excel('ventas.xlsx')

# Imprimir el DataFrame completo
print(df)
