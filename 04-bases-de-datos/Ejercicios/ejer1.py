from pymongo import MongoClient, collation
from bson.objectid import ObjectId
from pprint import pprint

MONGO_URI="mongodb://localhost:27017"
client = MongoClient(MONGO_URI)
db = client.Northwind
productos = db.Products
pedidos = db.Orders


"""
# Cuantos productos tenemos

# Mostrar el número de productos y un listado

# filtrar los productos con UnitsInStock 0 utilizando filter()

# valor del stock de cada producto (UnitsInStock x UnitPrice)
# con un FOR o realizarlo con un map() y la funcion sum()
# con una funcion aggregate() y los operadores $sum y $multiply 

# Con un ID de pedido, 
#   Mostramos datos:
#   -> ShipName, ShipAddress, ShipCity, ShipCountry, OrderDate, ShipDate
#   -> Producto, Cantidad, Precio, Precio total, Total pedido

Trucos de formateo, añadir espacios:

ejemplo = "ejemplo"
print(f"{'Pedido':<30} {ejemplo:<10}")

"""

query = {}