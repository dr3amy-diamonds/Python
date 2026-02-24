# Proyecto Integrador

## Pipeline de Datos y Análisis de Valorización Inmobiliaria (Q1)

------------------------------------------------------------------------

## 📋 1. Contexto del Negocio

El equipo directivo de una agencia de bienes raíces requiere un reporte
ejecutivo sobre el comportamiento de los precios de las propiedades
durante el primer trimestre del año (Q1).

La información disponible proviene de un sistema legado que exporta
datos fragmentados, desestructurados y con errores de formato. Esto
impide realizar análisis confiables y dificulta la toma de decisiones
estratégicas.

Los datos originales se encuentran distribuidos en tres fuentes
independientes:

1.  **Historial de precios mensuales** en formato ancho (columnas
    separadas por mes).
2.  **Catálogo de propiedades** con inconsistencias tipográficas y datos
    combinados en una misma columna.
3.  **Tabla de referencia socioeconómica** con información adicional por
    ciudad.

------------------------------------------------------------------------

## 🎯 2. Objetivo General del Proyecto

Diseñar y ejecutar un flujo de trabajo (Pipeline ETL) que permita:

-   Extraer los datos desde múltiples fuentes.
-   Limpiar inconsistencias estructurales y tipográficas.
-   Transformar el formato de los datos cuando sea necesario.
-   Consolidar la información en una única base analítica.
-   Generar un reporte dinámico con métricas clave para la dirección.

El entregable final será una **tabla dinámica** que resuma el precio
promedio del metro cuadrado segmentado por ciudad y tipo de inmueble,
lista para análisis gerencial.

------------------------------------------------------------------------

## 🏗️ 3. Arquitectura del Pipeline (Enfoque ETL)

El proyecto sigue la lógica clásica de un proceso ETL:

### 3.1 Extracción (Extract)

-   Lectura de archivos CSV locales.
-   Validación inicial de estructura y tipos de datos.
-   Identificación de columnas clave.

### 3.2 Transformación (Transform)

Incluye múltiples etapas de preparación:

#### 🔹 Reestructuración (Reshaping)

Conversión del formato ancho a formato largo para permitir análisis
temporales y modelado adecuado.

#### 🔹 Limpieza de Texto

-   Normalización de mayúsculas y minúsculas.
-   Eliminación de espacios innecesarios.
-   Separación de columnas combinadas.
-   Corrección de inconsistencias tipográficas.

#### 🔹 Manejo de Valores Nulos

-   Identificación de datos faltantes.
-   Aplicación de estrategias de imputación según el contexto del dato.

#### 🔹 Integración de Fuentes (Merging)

-   Cruce de bases mediante llaves comunes.
-   Uso de uniones que preserven la integridad del conjunto principal de
    datos.

#### 🔹 Ingeniería de Características

Creación de nuevas variables relevantes para el análisis, tales como: -
Precio por metro cuadrado. - Clasificación del inmueble según reglas de
segmentación. - Variables derivadas para análisis estratégico.

### 3.3 Carga (Load)

-   Consolidación del dataset final limpio.
-   Construcción de un reporte dinámico.
-   Generación de métricas agregadas para toma de decisiones.

------------------------------------------------------------------------

## 📊 4. Resultado Esperado

El producto final del proyecto será una tabla dinámica que permita
visualizar:

-   Precio promedio por metro cuadrado.
-   Segmentación por ciudad.
-   Segmentación por tipo de inmueble.
-   Comparación entre categorías (Premium vs. Estándar).
-   Resumen consolidado del primer trimestre (Q1).

Este resultado permitirá:

-   Identificar tendencias de valorización.
-   Detectar mercados con mayor crecimiento.
-   Comparar desempeño entre ciudades.
-   Apoyar decisiones estratégicas de inversión.

------------------------------------------------------------------------

## 🛠️ 5. Habilidades Técnicas Aplicadas

### Lenguaje y Librerías

-   Python
-   Pandas
-   NumPy

### Competencias Técnicas

-   Lectura y validación de datos estructurados.
-   Reestructuración de datos (wide vs. long).
-   Limpieza y estandarización de texto.
-   Manejo de valores faltantes.
-   Integración de múltiples fuentes de información.
-   Ingeniería de variables analíticas.
-   Construcción de reportes ejecutivos con tablas dinámicas.

------------------------------------------------------------------------

## 📚 6. Enfoque Metodológico

Este proyecto integra:

-   Pensamiento analítico.
-   Modelado estructural de datos.
-   Normalización de información para análisis.
-   Preparación de datos para inteligencia de negocios.

Se trata de un ejercicio integral que simula un escenario real del
entorno empresarial, donde la calidad del análisis depende directamente
de la calidad del procesamiento previo de los datos.

------------------------------------------------------------------------

## 🏁 7. Conclusión

El desarrollo de un Pipeline ETL robusto no solo resuelve problemas de
desorden estructural, sino que transforma información fragmentada en
conocimiento accionable.

Este proyecto demuestra cómo, mediante procesos sistemáticos de
limpieza, transformación y consolidación, es posible generar valor
estratégico a partir de datos inicialmente inconsistentes.

------------------------------------------------------------------------

**Documento académico -- Proyecto Integrador de Análisis de Datos**
