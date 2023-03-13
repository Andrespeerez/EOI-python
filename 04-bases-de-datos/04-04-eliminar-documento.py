from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint
import sys
import json

MONGO_URI="mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.Northwind
collection = db.Customers

result = collection.delete_many({"CustomerID": {"$regex": "DEM"}})

print(f"Estado de la Operacion: {result.acknowledged}")
print(f"# documentos eliminados : {result.deleted_count}")