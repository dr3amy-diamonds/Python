import numpy as np

# Generación de datos
def generar_analizarmatriz():
    # Generar matriz de enteros y convertir a float para poder usar NaN
    matriz_float = np.random.randint(-10, 100, size=(10,5)).astype(float)
    
    # Insertar algunos NaN para el ejemplo
    matriz_float[1, 2] = np.nan
    matriz_float[3, 4] = np.nan
    matriz_float[2, 2] = np.nan
    matriz_float[2, 3] = np.nan
    
    return matriz_float

# Mostrar la matriz formateada (enteros y NaN)
def mostrar_matriz(matriz, titulo="Matriz"):
    print(f"--- {titulo} ---")
    # Formateador visual para que los float parezcan int pero manteniendo NaN
    matriz_formateada = np.array2string(
        matriz,
        formatter={'float_kind': lambda x: f"{int(x)}" if not np.isnan(x) else "NaN"}
    )
    print(matriz_formateada)

# Exploración de datos
def exploracion_data(matriz):
    print("\n--- Exploración ---")
    print("Shape:", matriz.shape)
    print("Número de dimensiones:", matriz.ndim)
    print("Tipo de matriz:", matriz.dtype)

# Limpiar valores NaN y Negativos
def limpiar_matriz(matriz):
    # Trabajamos sobre una copia para no alterar la original
    matriz_temp = matriz.copy()

    # 1. Convertir negativos a NaN
    matriz_temp[matriz_temp <=0] = np.nan

    # 2. Eliminar filas que contengan NaN (ya sean originales o negativos convertidos)
    # ~ invierte la condición (nos quedamos con las que NO tienen NaN)
    matriz_sin_nan = matriz_temp[~np.isnan(matriz_temp).any(axis=1)]

    # 3. Convertir a ENTEROS (int)
    # Como ya no hay NaNs, podemos hacer esta conversión segura para quitar los puntos
    return matriz_sin_nan.astype(int)

def aplicar_transformaciones(matriz_sin_nan):
    print("\n--- Aplicando Transformaciones ---")
    
    # a) Logaritmo Natural
    # No necesita validación extra porque ya limpiamos <= 0
    mat_log = np.round(np.log(matriz_sin_nan), 2)
    print("Logaritmo Natural:\n",mat_log)

    # b) Raíz Cuadrada
    # No necesita validación extra porque ya limpiamos negativos
    mat_sqrt = np.round(np.sqrt(matriz_sin_nan), 2)
    print("Raíz Cuadrada:\n",mat_sqrt)
    
    # c) Potencia al cuadrado
    mat_cuadrado = matriz_sin_nan ** 2
    print("Potencia al cuadrado:\n",mat_cuadrado)



def aplicar_estadisticas(matriz_sin_nan):
    print("\n--- Aplicando Estadisticas ---")

    #1. Media
    mat_media=np.mean(matriz_sin_nan)
    print("Media de la matriz:",mat_media)

    #2. Minimo y máximo
    maxindex = np.argmax(matriz_sin_nan)
    minindex = np.argmin(matriz_sin_nan)
    print("Valor Minimo:",minindex)
    print("Valor Máximo:",maxindex)

    #3. Desviación Estandar
    matriz_std=np.std(matriz_sin_nan)
    print("Desviación Estandar:",matriz_std)

    #4. Globales y por columnas (`axis`)
    media_columnas = np.mean(matriz_sin_nan, axis=0)
    suma_columnas = np.sum(matriz_sin_nan, axis=0)
    std_columnas = np.std(matriz_sin_nan, axis=0)

    print("\nESTADÍSTICAS POR COLUMNAS (axis=0)")
    print(f"Media por columna: {media_columnas}")
    print(f"Suma por columna: {suma_columnas}")
    print(f"Desviación estándar por columna: {std_columnas}")



# --- Ejecución ---

# 1. Generar
matriz = generar_analizarmatriz()

# 2. Mostrar original
mostrar_matriz(matriz, "Matriz Original (con NaNs y Negativos)")
exploracion_data(matriz)

# 3. Limpiar y transformar
matriz_sin_nan = limpiar_matriz(matriz)

# 4. Transformaciones matematicas
mate=aplicar_transformaciones(matriz_sin_nan)

# 4. Resultado final
print("\n--- Matriz Limpia (Solo enteros positivos) ---")
print(matriz_sin_nan)
print("Tipo final:", matriz_sin_nan.dtype)