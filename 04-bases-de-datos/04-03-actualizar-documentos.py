from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

MONGO_URI="mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.Northwind
collection = db.Customers

query = {"Country": "EEUU"}

newValues = {
    "$set" : {
        "Country": "USA"
    }
}

resultado = collection.update_many(query, newValues)

print(resultado.matched_count, "documentos encontrados")
print(resultado.modified_count, "documentos modificados")
print("Estado de la operacion", resultado.acknowledged)
print()
print(collection.count_documents(query), "Clientes EEUU")
print(collection.count_documents({"Country": "USA"}), "Clientes USA")

exit()

query = {"CustomerID": "DEM10"}
documento = collection.find_one(query)

pprint(documento)

newValues = { 
    "$set" : {
        "Address" : "Calle Serrano, 81",
        "PostalCode": "28016",
        "Phone": "914502525"
    }
}

resultado = collection.update_one(query, newValues)

print(resultado.matched_count, "documentos encontrados")
print(resultado.modified_count, "documentos modificados")
print("Estado de la operacion", resultado.acknowledged)
print()
print(collection.find_one(query))