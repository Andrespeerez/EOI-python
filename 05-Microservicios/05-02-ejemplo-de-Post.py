import requests, pprint

url = "https://postman-echo.com/post"


myHeaders = {
    "Content-Type": "application/json",
    "api-key": "jdsjeuurksmd~$dkf"
}
myParams = {
    "id": 100,
    "process": "orders"
}
myData = {
    "text": "Supercalifragilistico"
}

#response = requests.post(url, params=myParams, headers=myHeaders, data=myData)
response = requests.request("POST", url, params=myParams, headers=myHeaders, data=myData)

# Mostrar el código de estado
print(f"Codigo de estado : {response.status_code}")
print(f"Estado : {response.reason}") 

print()

# Pintar las cabezeras
print("Cabeceras", response.headers)
print("\nContent-Type", response.headers['Content-Type'])
print("Content-Length", response.headers['Content-Length'], 'bytes')

# Pintar el cuerpo
print("\nContenido", response.content) # en modo bytes
print("Contenido", response.text) # en modo texto

"""
##########################################################
# Formas de enviar datos en un mensaje tipo post

# Enviar datos en la URL:
url = "https://dominio.com/api/customers/100/orders"

# Enviar datos como parámetros:
url = "https://dominio.com/api/customers?id=100&process=orders"
myParams = {
    "id": 100,
    "process": "orders"
}

# Enviar datos en la cabezera:
url = "https://dominio.com/api/customers"
myHeaders = {
    "Content-Type": "application/json",
    "api-key": "jdsjeuurksmd~$dkf",
    "id": 100,
    "process": "orders"
}

# Enviar datos en el cuerpo del mensaje:
url = "https://dominio.com/api/customers"
myHeaders = {
    "Content-Type": "application/json",
    "api-key": "jdsjeuurksmd~$dkf"
}
myData = {
    "id": 100,
    "process": "orders"
}
"""