# Proyecto: Auditoría de Datos para Control Interno – Inventario

## 📌 Descripción
Este proyecto simula un análisis de datos para una firma de consultoría en control interno. El objetivo es **limpiar, transformar y analizar** un dataset de inventario, detectando inconsistencias (precios negativos, datos duplicados, valores nulos) y generando un reporte de hallazgos.

## 🛠️ Tecnologías utilizadas
- Python (Pandas para limpieza y transformación)
- SQL (consultas para análisis exploratorio)
- Power BI / Excel (para visualización, opcional)

## 📂 Estructura del proyecto
- `datos/` – Datos originales (sucios)
- `scripts/` – Código Python y consultas SQL
- `reportes/` – Datos limpios y resumen de hallazgos

## 🚀 Cómo ejecutar
1. Clonar el repositorio.
2. Instalar dependencias: `pip install -r requirements.txt`
3. Ejecutar: `python scripts/limpieza_y_analisis.py`

## 📊 Resultados obtenidos
- Duplicados eliminados
- Precios y cantidades negativas corregidas
- Valores nulos reemplazados
- Reporte de hallazgos generado automáticamente

## 📌 Próximos pasos
- Integrar con Power BI para visualización interactiva
- Conectar a base de datos real (SQLite o PostgreSQL)