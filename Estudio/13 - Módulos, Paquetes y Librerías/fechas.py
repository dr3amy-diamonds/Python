import datetime

# Obtener la fecha y hora actual
fecha_hora_actual = datetime.datetime.now()

# Con formato personalizado
formato_personalizado = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Formato personalizado:", formato_personalizado)

#Con solo la fecha (Día, Mes y Año)
solo_fecha = fecha_hora_actual.strftime("%d-%m-%Y")
print("FORMATO DD-MM-AAAA:", solo_fecha)

# 5. Ejemplo con formato solo hora
solo_hora = fecha_hora_actual.strftime("%H:%M:%S")
print("Solo hora:", solo_hora)

#Con formato AAAA-MM-DD
formato_aaaa_mm_dd = fecha_hora_actual.strftime("%Y-%m-%d")
print("Formato AAAA-MM-DD:", formato_aaaa_mm_dd)