import requests, json
from secretos import login, login2

# para hacer login en emtmadrid
loginHeader = {
    "X-ClientId" : login2['X-ClientId'],
    "passKey" : login2['passKey']
}

urlLogin = f"https://openapi.emtmadrid.es/v1/mobilitylabs/user/login/"

try:
    response = requests.get(urlLogin, headers=loginHeader)
    print()
    if(response.status_code == 200):
        data = response.json()
        token = data['data'][0]['accessToken']

except:
    print(f"Error :  {response.reason}")


urlBusStop = "https://openapi.emtmadrid.es/v2/transport/busemtmad/stops/888/arrives"

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
        print("correcto")
        data = response.json()
        print(response.headers)
        for ii in data['data']:
            print(ii)

except:
    print(f"Error : busStop")
