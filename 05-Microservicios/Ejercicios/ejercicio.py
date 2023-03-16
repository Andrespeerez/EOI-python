import requests

country = "es"
postal_code = input("Codigo postal:  ")
url = f"https://api.zippopotam.us/{country}/{postal_code}"

print(url)

try:
    response = requests.get(url)
    lugar, comunidad = "Lugar", "Comunidad Autónoma"

    json_object = response.json()

    print(f"\n{lugar:<30} :    {comunidad:<20}")
    print("---------------------------------------------------------------")

    if(response.status_code == 200):
        for ii in json_object['places']:
            print(f"{ii['place name']:<30} :    {ii['state']:<20}")

    print()
except:
    print("Error")


