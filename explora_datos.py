import pandas as pd

# 1. Definimos los nombres de las columnas manualmente
nombres_columnas = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'species']

# 2. Cargamos el archivo indicando que no hay encabezados (header=None)
# y asignamos nuestra lista de nombres (names=nombres_columnas)
df = pd.read_csv('flores.csv', skiprows=1, header=None, names=nombres_columnas)

# 3. revisamos si se ve bien
print(df.head())

#contador de flores por especie
print("\nConteo por especie:")
print(df['species'].value_counts())
