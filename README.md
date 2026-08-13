
## 🚀 Instrucciones de Ejecución
Sigue estos pasos para replicar el análisis en tu entorno local:
1. Clonar el repositorio: `git clone https://github.com/Disvarianza/auditoria_inventario.git`
2. Instalar las dependencias (requiere Python instalado): `pip install -r requirements.txt` (Alternativa: `pip install pandas`)
3. Ejecutar el script principal: `python scripts/limpieza_y_analisis.py`
4. Verificar los resultados: Abre la carpeta `reportes/` para ver `datos_limpios.csv` y `hallazgos.txt`.

## 🔍 Proceso de Limpieza y Análisis (Metodología)
El script `limpieza_y_analisis.py` ejecuta automáticamente el siguiente flujo de trabajo:
1. Carga de datos: Importación del archivo `inventario_raw.csv`.
2. Eliminación de duplicados: Identifica y remueve registros idénticos.
3. Gestión de valores nulos: Detecta campos vacíos y los imputa con el promedio (técnica estadística).
4. Detección de anomalías: Precios con valores negativos y cantidades con valores negativos.
5. Corrección de datos: Transforma los valores negativos a su valor absoluto para preservar la integridad del negocio.
6. Exportación de resultados: Guarda el dataset limpio en `reportes/datos_limpios.csv` y guarda un resumen ejecutivo de hallazgos en `reportes/hallazgos.txt`.

## 📊 Dashboard en Power BI
A continuación, se muestra una captura del dashboard interactivo generado con Power BI para la visualización de los datos limpios:
![Dashboard Power BI](dashboard_powerbi.png)
> 💡 Este dashboard permite filtrar por categoría de producto y visualizar métricas clave como precios promedio, cantidad total y distribución del inventario.

## 📈 Resultados y Hallazgos Obtenidos
Tras la ejecución del proceso de limpieza, se obtuvieron los siguientes resultados:
- Registros duplicados: 1 detectado y eliminado.
- Precios negativos: 1 detectado y corregido a valor absoluto.
- Cantidades negativas: 1 detectada y corregida a valor absoluto.
- Valores nulos en precio: 1 detectado y rellenado con el promedio del inventario.

✅ Conclusión: El dataset ahora es confiable, consistente y apto para ser utilizado en procesos de consultoría, control interno y toma de decisiones estratégicas.

## 🔮 Próximos Pasos y Mejoras Futuras
- Conectar el script directamente a una base de datos SQLite o PostgreSQL en lugar de archivos CSV.
- Implementar pruebas unitarias para validar la robustez del código.
- Agregar más visualizaciones avanzadas en Power BI (mapas, indicadores KPI).
- Escalar el análisis a otras fuentes de datos y sectores industriales.

## 📬 Contacto y Portafolio
**Rosaura Elly González Hall**  
📧 ellyhall21@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/rosaura-elly-gonzalez-hall-79954a117)  
🐙 [GitHub - Disvarianza](https://github.com/Disvarianza)
