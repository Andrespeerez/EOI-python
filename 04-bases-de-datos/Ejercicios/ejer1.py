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


# Cuantos productos tenemos
print(f"Tenemos {productos.count_documents({})} productos")


# Mostrar el número de productos y un listado
todos_productos = productos.find({})

print(f"{'   Nombre del producto':<40}:   {'Cantidad':<8}")

while(todos_productos.alive):
    item = todos_productos.next()
    print(f"{item['ProductName']:<40}:   {item['UnitsInStock']:<8}")

# productos agotados usando filter()
cursor = productos.find({})

agotados = list(filter(lambda x: (x['UnitsInStock'] == '0') , cursor))

print("\nProductos agotados:")
for ii in agotados:
    print(f"{ii['ProductName']:<40}:   {ii['UnitsInStock']:<8}")

# Valor total de los productos:
cursor = productos.find({})
precios = list(map(lambda x: [x['ProductName'] , float(x['UnitsInStock']) * float(x['UnitPrice'])], cursor))
cursor = productos.find({})
total = sum(map(lambda x: (int(x['UnitsInStock']) * float(x['UnitPrice'])), cursor))

print("\nValor total de los productos:")
for ii in precios:
    print(f"{ii[0]:<40}:   {ii[1]:6.2f}€")

print(f"\nValor total del stock: {total:6.2f}€")

# usando aggregate() $sum y $mul

query = [
    {"$match": {"UnitsInStock" : {"$ne" : "0"}}}, # get documents with Stock != 0
    {"$addFields": { # add some fields to the match
        "Price" : {"$toDouble" : "$UnitPrice"}, # str to double
        "Stock" : {"$toInt" : "$UnitsInStock"} # str to int
    }},
    {"$group": { # for each document:
        "_id" : "Valor del Stock",
        "Total" : {"$sum": {"$multiply": ["$Price", "$Stock"]}}, 
        "Products" : {"$sum" : 1}
    }}
]

cursor = productos.aggregate(query)

print(f"\nValor total del stock: {cursor.next()['Total']}€")

