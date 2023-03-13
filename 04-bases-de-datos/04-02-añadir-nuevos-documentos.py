from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

class Customer:
    CustomerID = None
    CompanyName = None
    ContactName = None
    ContactTitle = None
    Address = None
    City = None
    Country = None
    PostalCode = None
    Region = None
    Phone = None
    Fax = None  


MONGO_URI="mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.Northwind
collection = db.Customers

cliente = Customer()
cliente.CustomerID = "DEM10"
cliente.CompanyName = "Un dos tres bebidas SL"
cliente.ContactName = "Andres"
cliente.ContactTitle = "Propietario"
cliente.Address = "Gran Via, 42"
cliente.Region = "Madrid"
cliente.City = "Madrid"
cliente.Country = "Spain"
cliente.PostalCode = "28044"
cliente.Phone = "912002010"
cliente.Fax = "912002011"

print(cliente)

# transforma un objeto en un diccionario
print(cliente.__dict__)

resultado = collection.insert_one(cliente.__dict__)

print(f"\nObjectID : {resultado.inserted_id}")

cursor = collection.find({"CustomerID": {"$regex" : "DEM"}})

while(cursor.alive):
    doc = cursor.next()
    print(f"{doc['CustomerID']}# {doc['CompanyName']}")

exit()

cliente = {
    "CustomerID" : "DEMO2",
    "CompanyName" : "Uno Comidas SL",
    "ContactName" : "Andres Perez",
    "ContactTitle" : "Propietario",
    "Address" : "Calle Gran Via, 42",
    "City" : "Madrid",
    "Country" : "Spain",
    "PostalCode" : "28044",
    "Region" : "Madrid",
    "Phone" : "912002010",
    "Fax" : "912002011"  
}

resultado = collection.insert_one(cliente)
# collection.insert_many([cliente1, cliente2, cliente3])

print(f"Resultado : {resultado}")
print(f"Object_ID : {resultado.inserted_id}")
print(f"Acknowledged : {resultado.acknowledged}") # True, insertado con éxito
