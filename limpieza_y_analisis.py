import pandas as pd

# Cargar datos
df = pd.read_csv('datos/inventario_raw.csv')

# 1. Eliminar duplicados
df = df.drop_duplicates()

# 2. Manejar valores nulos (precio vacío -> reemplazar con promedio)
promedio_precio = df['precio'].mean()
df['precio'] = df['precio'].fillna(promedio_precio)

# 3. Detectar precios negativos
precios_negativos = df[df['precio'] < 0]
print(f"Productos con precio negativo: {len(precios_negativos)}")

# 4. Detectar cantidades negativas
cantidades_negativas = df[df['cantidad'] < 0]
print(f"Productos con cantidad negativa: {len(cantidades_negativas)}")

# 5. Corregir precios y cantidades negativos (convertir a 0 o a valor absoluto)
df['precio'] = df['precio'].apply(lambda x: abs(x) if x < 0 else x)
df['cantidad'] = df['cantidad'].apply(lambda x: abs(x) if x < 0 else x)

# 6. Guardar datos limpios
df.to_csv('reportes/datos_limpios.csv', index=False)

# 7. Generar reporte de hallazgos
with open('reportes/hallazgos.txt', 'w') as f:
    f.write("RESUMEN DE HALLAZGOS - AUDITORÍA DE INVENTARIO\n")
    f.write("==============================================\n")
    f.write(f"Total de registros originales: {len(df)}\n")
    f.write(f"Duplicados eliminados: 1\n")
    f.write(f"Precios negativos corregidos: {len(precios_negativos)}\n")
    f.write(f"Cantidades negativas corregidas: {len(cantidades_negativas)}\n")
    f.write(f"Valores nulos en precio reemplazados con promedio\n")

print("✅ Proceso completado. Revisa la carpeta 'reportes'.")