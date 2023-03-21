import requests, json
from secretos import login

# para hacer login en emtmadrid
loginHeader = {
    "X-ClientId" : login['X-ClientId'],
    "passKey" : login['passKey']
}

# login deprecado (pero funciona)
#loginHeader = {
#    "email" : login3['email'],
#    "password" : login3['password']
#}

urlLogin = f"https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"

try:
    response = requests.get(urlLogin, headers=loginHeader)
    print(response.status_code, response.reason)
    print()
    if(response.status_code == 200):
        data = response.json()
        token = data['data'][0]['accessToken']

except:
    print(f"Error :  {response.reason}")

url_parking_availability = f"https://openapi.emtmadrid.es/v1/citymad/places/parkings/availability"

tokenHeader = {
    "accessToken" : token
}

print(token)

try:
    response = requests.get(url_parking_availability, headers=tokenHeader)
    print(response.status_code, response.reason)
    if(response.status_code == 200):
        data = response.json()

except:
    print(f"Error : Parking")

print()
# filter() para guardar los parking que tienen valores numéricos
parking = filter(lambda x : x['freeParking'] != None, data['data'])

# usamos sum() y map() para calcular el total de plazas libres
free_parking = sum(map(lambda cosas : cosas['freeParking'], parking))

print(f"# de plazas libres totales :  {free_parking}")