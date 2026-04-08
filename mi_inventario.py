import pandas as pd
# definimos los datos (como una lista de diccionarios)
dispositivos = [
    {"nombre": "S25 Ultra", "rol": "Cerebro/Dex", "so": "Android", "precio":1200}, 
    {"nombre": "Tab A9+", "rol": "Estudio/Monitor", "so": "Android", "precio": 250}
    
]

#Convertimos a DataFrame
df = pd.DataFrame(dispositivos)

# Mostramos un analisis rapido
print("-- Mi invetario de Datos --")
print(df)
print("\n--- Resumen estadístico ---")
print(df.describe())
