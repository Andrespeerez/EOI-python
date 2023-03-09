from pymongo import MongoClient, collation
#from bson.objectid import Objectid
from pprint import pprint
import sys
import json
# modulo para conexion, NO AÑADIDO AL REPOSITIO
from conexion import MONGO_URI 

# Establecemos la conexion con el servidor/basededatos/coleccion
MONGO_URI = "mongodb://host-mongodb-eoi.northeurope.cloudapp.azure.com:27017"
client = MongoClient(MONGO_URI)
db = client.Northwind
collection = db.Customers

cursor = collection.find({"Country": "USA"})

print(f"Numero de documentos encontrados:  {cursor.count()}")
print("Numero de documentos encontrados: ", collection.count_documents({"Country": "USA"}))

print("Datos pendientes de leer:", cursor.alive)

while(cursor.alive):
    pprint(cursor.next()) # se mueve por el cursor

print("Datos pendientes de leer:", cursor.alive)

cursor = collection.find({"Country": "USA"}).limit(3) # los 3 primeros
cursor = collection.find({"Country": "USA"}).skip(5) # los 5 primeros saltalos
cursor = collection.find({"Country": "USA"}).skip(10).limit(10) # salta 10 y lee los 10 siguientes

cursor = collection.find({"Country": "USA"}).sort("City", 1) # en orden A to W
cursor = collection.find({"Country": "USA"}).sort("City", -1) # en orden W to A

while(cursor.alive):
    document = cursor.next()
    print(document["CompanyName"], document["Country"], document["City"])