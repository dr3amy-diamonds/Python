# Taller Corporativo: Análisis de Series de Tiempo

------------------------------------------------------------------------

## Misión 1: El Cierre Contable (Resampling Mensual)

### Contexto de Negocio

El Director Financiero (CFO) se está preparando para la junta anual.
Revisar miles de transacciones individuales resulta inviable desde una
perspectiva estratégica. Se necesita una visión agregada que permita
evaluar la salud financiera general del negocio.

### Objetivo

Calcular el total de dinero ingresado (monto_transaccion) agrupado por
mes.

### Teoría Aplicada

Este ejercicio se fundamenta en el concepto de *Downsampling*. Según Wes
McKinney, reducir la frecuencia de los datos ---por ejemplo, pasar de
registros diarios o por segundo a datos mensuales--- permite eliminar el
ruido operativo y visualizar tendencias estructurales.

El re-muestreo mensual consolida la información y transforma datos
transaccionales en información estratégica, adecuada para reportes
ejecutivos y análisis financieros de alto nivel.

------------------------------------------------------------------------

## Misión 2: Auditoría de Crisis (Slicing + GroupBy)

### Contexto de Negocio

El equipo de Soporte Técnico detectó múltiples quejas relacionadas con
lentitud durante agosto de 2024. Se requiere identificar qué servidor
presentó mayores problemas durante ese periodo específico.

### Objetivos

1.  Filtrar la información para conservar únicamente los datos
    correspondientes a agosto de 2024 mediante slicing temporal.
2.  Agrupar los datos filtrados por servidor_id.
3.  Calcular el promedio de latencia (latencia_ms) por servidor.

### Teoría Aplicada

El uso de un DatetimeIndex permite realizar selecciones parciales
basadas en cadenas de texto que representan fechas. McKinney destaca que
este tipo de indexación temporal facilita consultas como seleccionar un
mes completo sin necesidad de construir filtros booleanos complejos.

Posteriormente, el uso de agrupación permite resumir métricas por
entidad (en este caso, servidor), lo cual es clave en procesos de
auditoría técnica y análisis de desempeño.

------------------------------------------------------------------------

## Misión 3: Análisis de Tráfico de Dispositivos (Resampling Semanal)

### Contexto de Negocio

El equipo de Marketing Digital busca analizar el volumen de
interacciones en la plataforma. El enfoque no está en el valor monetario
sino en la cantidad de eventos generados por los usuarios, segmentados
por tipo de dispositivo.

### Objetivo

Calcular el conteo de interacciones re-muestreado por semana,
considerando un tipo de dispositivo específico (por ejemplo, Mobile) o
segmentando adecuadamente antes del re-muestreo.

### Teoría Aplicada

Este caso aplica la transformación de eventos irregulares a frecuencias
regulares. Matt Harrison recomienda este enfoque como base para la
construcción de gráficos de tendencia, ya que convierte datos dispersos
en series temporales estructuradas y comparables.

El re-muestreo semanal permite observar patrones de crecimiento,
estacionalidad o caídas en la interacción de usuarios a lo largo del
tiempo.

------------------------------------------------------------------------

## Misión 4: Crecimiento Month-over-Month (MoM)

### Contexto de Negocio

El crecimiento Month-over-Month (MoM) es una de las métricas más
relevantes en startups y empresas tecnológicas. El CEO necesita conocer
el porcentaje de crecimiento o decrecimiento de las ventas respecto al
mes inmediatamente anterior.

### Objetivos

1.  Crear una estructura mensual con la suma total de ventas.
2.  Generar una columna que represente el ingreso del mes anterior.
3.  Calcular el porcentaje de crecimiento mensual usando la variación
    relativa entre el ingreso actual y el ingreso del mes previo.

### Teoría Aplicada

El desplazamiento temporal permite comparar cada periodo contra su
equivalente inmediato anterior sin necesidad de procesos manuales. Esta
técnica es estándar en análisis financiero profesional y constituye la
base para métricas de crecimiento comparativo.

El cálculo porcentual resultante proporciona una métrica dinámica que
permite evaluar aceleración, desaceleración o contracción del negocio en
el tiempo.

------------------------------------------------------------------------

## Conclusión General

Este taller integra conceptos fundamentales del análisis de series de
tiempo:

-   Re-muestreo para agregación estratégica.
-   Indexación temporal para consultas precisas.
-   Agrupación para análisis segmentado.
-   Desplazamiento temporal para métricas comparativas.

Dominar estas técnicas permite transformar datos operativos en
información ejecutiva, facilitando la toma de decisiones a nivel
directivo.
