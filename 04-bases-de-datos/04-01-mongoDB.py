from pymongo import MongoClient, collation
#from bson.objectid import Objectid
from pprint import pprint
import sys, json
from conexion import MONGO_URI

"""
# ATLAS URI
MONGO_URI = ""
"""
# Creamos el objeto que representa el cliente para trabajar con la base de datos
# Se requiere la cadena de conexion
client = MongoClient(MONGO_URI)

# Mostrar el estado del servidor
# Nos posicionamos sobre la base de datos
db = client.admin

# Ejecutamos comandos sobre la base de datos
# Los comandos nos permiten INSERTAR, ACTUALIZAR, ELIMINAR, LEER informacion

# serverStatus -> return estado servidor en formato JSON
status = db.command("serverStatus")
print(status)
