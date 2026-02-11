import requests

#Pedir los datos de la API, se usa get
respuesta = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu", timeout=10)
respuesta.raise_for_status()

#Usar Json para convertirlo en diccionario
data = respuesta.json()

#Extraer al valor del json
nombre = data["name"]
peso = data["weight"]

#Imprimir el valor del json
print("Nombre:", nombre)
print("Peso:", peso)
