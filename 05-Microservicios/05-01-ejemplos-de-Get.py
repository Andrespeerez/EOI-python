import requests, pprint

force_error = False
if(force_error):
    # endpoint del microservicio
    url = "http://api.open-notify.org/iss-now.json2"
else:
    # endpoint del microservicio
    url = "http://api.open-notify.org/iss-now.json"

# empleamos get() para realizar una llamada GET
# la función get() retorna una respuesta
response = requests.get(url)

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


if(response.status_code == 200 and 
   response.headers['Content-Type'] == 'application/json'):
    data = response.json()
    print(f"\nMensaje: {data['message']}")
    print(f"Longitud: {data['iss_position']['longitude']}")
    print(f"Latitud: {data['iss_position']['latitude']}")