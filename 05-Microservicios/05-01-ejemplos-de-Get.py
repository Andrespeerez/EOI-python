import requests, pprint

# endpoint del microservicio
url = "http://api.open-notify.org/iss-now.json"

# empleamos get() para realizar una llamada GET
# la función get() retorna una respuesta
response = requests.get(url)

# Mostrar el código de estado
print(f"Codigo de estado : {response.status_code}")
print(f"Estado : {response.reason}") 

print()

if(False)
# endpoint del microservicio
    url = "http://api.open-notify.org/iss-now.json2"

# empleamos get() para realizar una llamada GET
# la función get() retorna una respuesta
    response = requests.get(url)

# Mostrar el código de estado
    print(f"Codigo de estado : {response.status_code}")
    print(f"Estado : {response.reason}") 

    print()

