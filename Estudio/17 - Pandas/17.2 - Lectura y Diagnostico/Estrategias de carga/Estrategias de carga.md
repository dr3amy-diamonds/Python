# Estrategias de Carga (Input/Output Tools) en Pandas

## 1. Definición y Fundamentos Teóricos

En Pandas, la carga de datos no consiste simplemente en abrir un
archivo. Es un proceso de **ingeniería de serialización**: un conjunto
de mecanismos que traducen datos almacenados en disco (texto plano,
binarios o bases de datos) a objetos vivos en memoria RAM,
principalmente DataFrames.

### El problema de la inferencia

Cuando un archivo se carga sin estrategia, Pandas debe inferir qué tipo
de datos contiene cada columna. Conceptualmente, esto implica dos pasos:

-   **Escaneo**: lectura de una parte del archivo para deducir si
    valores como "100" son números o texto.
-   **Conversión**: transformación de los bytes leídos en objetos de
    Python o NumPy.

Una **estrategia de carga** consiste en configurar explícitamente este
proceso para evitar suposiciones innecesarias, reduciendo el consumo de
memoria y aumentando la velocidad.

------------------------------------------------------------------------

## 2. ¿Para qué sirve tener una estrategia?

Una carga ingenua puede generar problemas graves en entornos reales. Las
estrategias existen para resolver tres cuellos de botella principales:

### Desbordamiento de memoria

Archivos grandes pueden exceder la RAM disponible. Un archivo de 10 GB
no puede cargarse completo en un equipo con 8 GB de memoria sin provocar
un fallo. En estos casos, la carga por bloques es obligatoria.

### Rendimiento

Los formatos de texto como CSV o JSON requieren procesos de parsing
costosos. Los formatos binarios evitan este trabajo, permitiendo
lecturas mucho más rápidas.

### Integridad de tipos

Sin control explícito, Pandas puede convertir datos sensibles (como
códigos postales con ceros iniciales) en números, alterando su
significado original.

------------------------------------------------------------------------

## 3. Toolbox: Funciones de Lectura (Ranking de Utilidad)

Pandas utiliza una API unificada: casi todas las funciones de carga
comienzan con `read_`. Estas pueden clasificarse por su uso en la
industria.

### Nivel 1: Estándares de texto plano

Formatos universales y legibles por humanos, pero computacionalmente
ineficientes.

**read_csv** Función central de Pandas para cargar archivos delimitados.
Es altamente configurable y permite controlar casi todos los aspectos
del proceso de lectura.

**read_json** Utilizada para datos provenientes de APIs o bases de datos
NoSQL. Soporta estructuras anidadas.

**read_html** Extrae automáticamente tablas desde páginas web y las
convierte en DataFrames. Útil para scraping rápido.

### Nivel 2: Hojas de cálculo

**read_excel** Diseñada para archivos de Excel. Es considerablemente más
lenta que CSV y depende de librerías externas. Se recomienda solo para
reportes finales o entradas manuales.

### Nivel 3: Alto rendimiento (formatos binarios)

Estos formatos almacenan los datos de forma muy similar a como residen
en memoria.

**read_parquet** Formato columnar moderno, altamente comprimido y
eficiente. Preserva los tipos de datos y permite leer solo columnas
específicas.

**read_feather** Extremadamente rápido para intercambios temporales
entre Python y R. Ideal como caché, no como formato de almacenamiento a
largo plazo.

------------------------------------------------------------------------

## 4. Utilidades especiales

**read_clipboard** Permite convertir directamente en DataFrame cualquier
tabla copiada al portapapeles. Ideal para pruebas rápidas y exploración.

**read_sql / read_sql_query** Conecta Pandas directamente a bases de
datos relacionales mediante consultas SQL.

------------------------------------------------------------------------

## 5. Parámetros estratégicos clave

La verdadera estrategia no está solo en la función utilizada, sino en
los argumentos que se le pasan.

### Filtrado vertical

Permite cargar únicamente las columnas necesarias, reduciendo de forma
drástica el uso de memoria.

### Optimización de tipos

Definir explícitamente los tipos de datos evita inferencias innecesarias
y permite usar representaciones más eficientes.

### Manejo temporal

Convertir fechas durante la carga evita conversiones posteriores que
duplican temporalmente el uso de memoria.

### Carga por lotes

Procesar archivos en bloques permite trabajar con datos que exceden la
memoria disponible.

### Definición de índice

Asignar el índice durante la carga ahorra pasos adicionales de
procesamiento.

------------------------------------------------------------------------

## 6. Resumen conceptual

Una estrategia de carga profesional sigue este razonamiento:

-   Priorizar formatos binarios cuando sea posible.
-   Cargar solo los datos necesarios.
-   Definir tipos de datos desde el inicio.
-   Procesar por bloques cuando el tamaño lo requiera.

Dominar estos principios elimina errores de memoria y convierte la carga
de datos en un proceso eficiente, controlado y escalable.
