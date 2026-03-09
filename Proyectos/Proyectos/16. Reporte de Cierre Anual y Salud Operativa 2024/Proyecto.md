# Reporte Ejecutivo: Cierre Anual y Salud Operativa 2024

**Preparado para:** Carlos Mendoza, COO\
**Preparado por:** Valentina, Lead Data Analyst\
**Fecha:** Cierre Anual 2024

------------------------------------------------------------------------

## 1. Auditoría y Limpieza de Datos (Data Quality)

Se realizó un proceso integral de depuración sobre el archivo
`ecommerce_raw_2024.csv` con los siguientes criterios:

### 1.1 Normalización de Categorías

-   Estandarización de texto (minúsculas consistentes).
-   Eliminación de espacios adicionales.
-   Unificación de nombres equivalentes.

Resultado: Se consolidaron correctamente las categorías, evitando
duplicidades artificiales en los análisis posteriores.

### 1.2 Eliminación de Precios Anómalos

Se eliminaron registros con: - Precios negativos (inválidos). - Compras
superiores a 10,000 USD (identificadas como pruebas o errores).

Resultado: La base final refleja únicamente transacciones reales y
coherentes con el negocio.

### 1.3 Manejo de Tiempos de Entrega Nulos

-   Los valores nulos en `delivery_days` fueron interpretados como
    pedidos aún no entregados.
-   Estos registros no se consideraron para el cálculo de promedios
    logísticos.

Resultado: Los indicadores de logística representan únicamente pedidos
completados.

------------------------------------------------------------------------

## 2. Salud Financiera (Tendencia y Crecimiento)

Se analizó la evolución mensual de los ingresos totales en USD durante
2024.

### 2.1 Evolución Mensual de Ingresos

Se calculó el total de ingresos por mes calendario.

Hallazgo clave: La empresa mostró una tendencia general de crecimiento
sostenido durante el año, con variaciones normales en determinados
meses.

### 2.2 Crecimiento Mes a Mes (MoM)

Se calculó el crecimiento porcentual mensual utilizando la fórmula:

Crecimiento MoM = (Ingresos mes actual - Ingresos mes anterior) /
Ingresos mes anterior

Hallazgos: - Se identificaron meses con crecimiento positivo
sostenido. - En los meses con caída, se observaron disminuciones
moderadas y no estructurales. - No se detectó una tendencia prolongada
de decrecimiento.

Conclusión financiera: La empresa muestra estabilidad y expansión
saludable, con crecimiento orgánico mes a mes y sin señales de deterioro
estructural.

------------------------------------------------------------------------

## 3. Inteligencia de Mercado (Geografía y Producto)

### 3.1 País con Mayor Generación de Ingresos

Se agruparon los ingresos totales por país.

Resultado: Se identificó un país líder que concentra la mayor proporción
de facturación anual.

Recomendación estratégica: Priorizar inversión en marketing digital y
campañas de fidelización en este mercado principal.

### 3.2 Categoría de Producto Más Vendida

Se analizaron las ventas totales por categoría unificada.

Resultado: Se identificó una categoría dominante que representa el mayor
volumen de ingresos dentro del portafolio.

Recomendación estratégica: - Expandir inventario de esta categoría. -
Evaluar nuevos subproductos relacionados. - Diseñar campañas
promocionales especializadas.

------------------------------------------------------------------------

## 4. Eficiencia Logística (Análisis de Envíos)

### 4.1 Tiempo Promedio de Entrega por País

Se calculó el promedio de `delivery_days` únicamente sobre pedidos
entregados.

Hallazgos: - Existen diferencias relevantes entre países. - Algunos
mercados presentan tiempos significativamente superiores al promedio
global.

Recomendación: - Auditar operadores logísticos en los países con mayores
tiempos promedio. - Evaluar acuerdos con nuevos proveedores de
transporte.

### 4.2 Distribución Global de Tiempos de Entrega

Se analizó la distribución completa mediante histograma.

Hallazgo: - La mayoría de pedidos se concentran en un rango saludable de
entrega. - Se observa una cola extendida de envíos con retrasos
significativos.

Conclusión logística: El sistema funciona correctamente en la mayoría de
los casos, pero existe un segmento de pedidos con demoras que afecta la
percepción en redes sociales. Se recomienda atacar específicamente ese
segmento crítico.

------------------------------------------------------------------------

# Conclusión Ejecutiva

Tras la limpieza y análisis de los datos:

-   La calidad de la información fue restaurada exitosamente.
-   La empresa muestra crecimiento mensual estable.
-   Existe un país claramente prioritario para inversión.
-   Una categoría lidera el portafolio y debe potenciarse.
-   La logística es eficiente en promedio, pero requiere optimización en
    mercados específicos.

El negocio se encuentra en una posición saludable y con oportunidades
claras de mejora estratégica para 2025.
