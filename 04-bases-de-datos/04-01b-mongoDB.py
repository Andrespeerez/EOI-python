from pymongo import MongoClient, collation
#from bson.objectid import Objectid
from pprint import pprint
import sys
import json
# modulo para conexion, NO AÑADIDO AL REPOSITIO
from conexion import MONGO_URI 

# Establecemos la conexion con el servidor
MONGO_URI="mongodb://localhost:27017"
client = MongoClient(MONGO_URI)

# listar los nombres de las bases de datos
print(client.list_database_names())

# Elegimos la base de datos con la que vamos a trabajar:
# Sintaxis de objeto
db = client.Northwind

# Sintaxis de coleccion
db2 = client["Northwind"]

# listar los nombres de las colecciones de la base de datos
print(db.list_collection_names()) 
print(db2.list_collection_names())

# seleccionar una coleccion de la base de datos
collection = db.Customers

# Numero de documentos en la coleccion
print(f"{collection.estimated_document_count()} documentos en la coleccion")


# LEER DATOS
print("\nFind_one")
result = collection.find_one({"Country": "USA"})
pprint(result)

print("\nFind (devuelve un cursor que es como un generador)")
results = collection.find({"Country": "USA"})
pprint(results) # devuelve un cursor que es como un generador

