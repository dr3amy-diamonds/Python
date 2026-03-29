import pandas as pd


def limpiar_fecha(fecha_sucia):
    fecha_texto = str(fecha_sucia)

    if fecha_texto.isdigit():
        #  Convertir a int para que pandas lo trate como Unix timestamp
        resultado = pd.to_datetime(int(fecha_texto), unit='s')
    else:
        resultado = pd.to_datetime(fecha_texto, dayfirst=True ,errors="coerce")

    return resultado


def cargar_y_limpiar(ruta_archivo):
    """
    Función maestra que carga los datos desde una ruta específica 
    y ejecuta todas las herramientas de limpieza necesarias.
    """
    # 1. Leemos el archivo usando el parámetro que viene desde el notebook
    raw_data = pd.read_csv(ruta_archivo)

    # 2. Aplicamos la herramienta de fechas a la columna y guardamos los cambios
    raw_data['transaction_date'] = raw_data['transaction_date'].apply(limpiar_fecha)

    # 3. Aplicamos limpieza para la columna 'status' y guardamos los cambios
    raw_data['status'] = raw_data['status'].str.strip().str.capitalize()

    # 4. Retornamos la tabla completa ya con las fechas perfectas
    return raw_data

def limpiar_comercio(nombre_sucio):
    texto_min = str(nombre_sucio).lower()

    marcas = [
        (['amazon', 'amzn'],   'Amazon'),
        (['apple'],            'Apple'),
        (['netflix'],          'Netflix'),
        (['uber'],             'Uber'),
        (['starbucks', 'strbcks'], 'Starbucks'),
    ]

    for palabras_clave, marca in marcas:
        if any(clave in texto_min for clave in palabras_clave):
            return marca

    return 'Otro'

def limpiar_moneda (moneda_sucia):
    texto_mayu = str(moneda_sucia).strip().upper()

    tasas_cambio = {
        'USD': 1.0,
        'COP': 0.00026,
        'EUR': 1.082,
        'GBP': 1.244
    }

    try:
        tasa = tasas_cambio[texto_mayu]
        return tasa

    except KeyError:
        return None

def mapa_codigos(meses_sucios):
    mapa = {
        1: 'Enero', 2: 'Febrero', 3: 'Marzo',
        4: 'Abril', 5: 'Mayo', 6: 'Junio',
        7: 'Julio', 8: 'Agosto', 9: 'Septiembre',
        10: 'Octubre', 11: 'Noviembre', 12: 'Diciembre'
    }
    return mapa.get(meses_sucios)






