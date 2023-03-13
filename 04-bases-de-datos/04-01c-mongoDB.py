from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json
# modulo para conexion, NO AÑADIDO AL REPOSITIO
from conexion import MONGO_URI 

# Establecemos la conexion con el servidor/basededatos/coleccion
MONGO_URI="mongodb://localhost:27017"
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

"""
===================================================
 Listado de operadores relacionales
===================================================
$eq - equal - igual
$lt - low than - menor que
$lte - low than equal - menor o igual que
$gt - greater than - mayor que
$gte - greater than equal - mayor o igual que
$ne - not equal - distinto
$in - in - dentro de
$nin - not in - no dentro de
"""

# Ambas sentencias son la misma, pero una ponemos explicitamente el operador
cursor = collection.find({"Country": "USA"})
cursor = collection.find({"Country": {"$eq": "USA"}})

while(cursor.alive):
    document = cursor.next()
    print(document["CompanyName"], document["Country"], document["City"])

print("\n\nOperadores:")
# todos los que no sean de USA
cursor = collection.find({"Country": {"$ne": "USA"}})
print("Numero de documentos encontrados: ", collection.count_documents({"Country": {"$ne": "USA"}}))

# multiples paises (USA y Mexico)
#cursor = collection.find({"Country": {"in": ["USA", "Mexico"]}})

# EJERCICIO:
"""
Quiero buscar los clientes de Mexico
Mostrar su informacion : Nombre de la empresa
Mostrar los pedidos que tienen : CustomerID -> Pedidos
"""

Clientes = db.Customers
Pedidos = db.Orders

cursorClientes = Clientes.find({"Country": "Mexico"})

i = 0
while(cursorClientes.alive):
    i += 1
    d = cursorClientes.next()
    print(f"\nCLIENTE # {i}")
    print(d['ContactName'],"  :  " ,d['CompanyName'])
    cursorPedidos = Pedidos.find({"CustomerID": d['CustomerID']})
    ii = 0
    while(cursorPedidos.alive):
        ii += 1
        d2 = cursorPedidos.next()
        print("Pedido #"+str(ii)+" >> orderID :  "+d2['OrderID']+" |  Fecha : "+d2['OrderDate'])


# Obtener un cliente y todos sus pedidos en una única consulta

cursor = Clientes.aggregate([
    {"$match": {"CustomerID": "ANATR"}},
    {"$sort": {"City" : 1}},
    {"$lookup": {
        "from": "Orders",
        "localField" : "CustomerID",
        "foreignField": "CustomerID",
        "as": "Pedidos"
    }}
])

print()
while(cursor.alive):
    customer = cursor.next()
    print(customer['ContactName'],"  :  " , customer['CompanyName'])
    for ii in customer['Pedidos']:
        print(" >> orderID :  "+ii['OrderID']+" |  Fecha : "+ii['OrderDate'])



