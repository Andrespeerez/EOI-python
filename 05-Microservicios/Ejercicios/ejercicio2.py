import requests


url = "https://api.apilayer.com/exchangerates_data/symbols"

# este servicio requiere mandar una "apikey" en la cabecera
myHeaders = {
    "apikey" : "WqVzJ6pWHbPkkil5ya8tzBYyBM2fKj1z"
}

try:
    response = requests.get(url, headers=myHeaders)

    if(response.status_code == 200):
        data = response.json()
        for ii in data['symbols']:
            print(f"{ii:<8} :   {data['symbols'][ii]:<30}")
    else:
        print(f"Razón : {response.reason}")
except:
    print("Error")