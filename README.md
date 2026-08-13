
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
![Dashboard Power BI]<img width="1272" height="607" alt="image" src="https://github.com/user-attachments/assets/db1ea24e-4cc8-436a-ae94-9d494804710d" />

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
## 📊 Análisis del Dashboard – Inventario Limpio

A partir de los datos depurados, el dashboard generado en Power BI permite extraer las siguientes conclusiones clave para la toma de decisiones:

### 1. Distribución de precios por categoría
- La categoría **Electrónica** presenta el precio promedio más alto del inventario, lo cual es consistente con el valor comercial de este tipo de productos.
- Las categorías **Papelería** y **Periféricos** muestran precios promedio más accesibles, lo que sugiere una estrategia de precios escalonada por tipo de producto.

### 2. Comportamiento del inventario por cantidad
- La categoría **Papelería** concentra la mayor cantidad de unidades disponibles, lo que podría indicar una alta rotación o una sobrecompra de estos artículos.
- La categoría **Electrónica**, a pesar de tener el precio más alto, presenta una cantidad relativamente baja, lo que sugiere que podría tratarse de productos de mayor valor unitario con un stock más controlado.

### 3. Estado general del inventario
- El inventario se encuentra **completamente depurado**: no existen registros duplicados, precios negativos, cantidades negativas ni valores nulos.
- La base de datos actual es **confiable y consistente**, lo que permite su uso inmediato para análisis financieros, auditorías de control interno y planificación de compras.

### 4. Oportunidades de mejora detectadas
- Se observa que la categoría **Muebles** tiene pocos registros y una cantidad limitada, lo que podría indicar una baja demanda o una necesidad de revisar la estrategia de surtido.
- El análisis sugiere que la empresa podría beneficiarse de un seguimiento más detallado de las categorías con mayor rotación para optimizar la gestión de inventarios.

### 5. Conclusión ejecutiva
Este dashboard demuestra que, tras aplicar un proceso riguroso de limpieza y transformación de datos con Python y Pandas, se obtuvo una **visión clara y accionable** del estado del inventario. La información generada permite a un equipo de consultoría o control interno:
- ✅ Identificar categorías con mayor y menor valor.
- ✅ Detectar desbalances en la distribución de cantidades.
- ✅ Contar con una base sólida para recomendar mejoras operativas y financieras.

> 💡 **Valor agregado:** La combinación de automatización con Python y visualización con Power BI permite que este análisis sea **reproducible, escalable y fácil de comunicar** a equipos directivos o clientes de consultoría.

## 📬 Contacto y Portafolio
**Rosaura Elly González Hall**  
📧 ellyhall21@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/rosaura-elly-gonzalez-hall-79954a117)  
🐙 [GitHub - Disvarianza](https://github.com/Disvarianza)
