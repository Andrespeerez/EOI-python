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
    print()
    if(response.status_code == 200):
        data = response.json()
        token = data['data'][0]['accessToken']

except:
    print(f"Error :  {response.reason}")

input_parada = input("Parada:  ")
urlBusStop = f"https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/{input_parada}/arrives"

tokenHeader = {
    "accessToken" : token
}

print(token)



myBody = {
    "cultureInfo":"ES",
    "Text_StopRequired_YN":"Y",
    "Text_EstimationsRequired_YN":"Y",
    "Text_IncidencesRequired_YN":"N",
    "DateTime_Referenced_Incidencies_YYYYMMDD":"20230316"
}

myBody_json = json.dumps(myBody)


try:
    response = requests.post(urlBusStop, headers=tokenHeader, data=myBody_json)
    print(response.status_code, response.reason)
    if(response.status_code == 200):
        data = response.json()
        for ii in data['data'][0]['Arrive']:
            print(f"Bus {ii['bus']} llega a parada {ii['stop']} en {ii['estimateArrive']:<5} segundos")
            

except:
    print(f"Error : busStop")