import pymssql

# Establecer conexión con la base de datos:
connection = pymssql.connect( server = "host-sqlserver-eoi.database.windows.net",
                              user = "Administrador",
                              password = "azurePa$$w0rd",
                              database = "Northwind"
                            )

# Creamos un Cursor para ejecutar comando en BD
# Retorna tuplas
cursor = connection.cursor()

# Retorna Diccionarion
cursor = connection.cursor(as_dict=True)

# Actualizamos algun registro
cursor.execute("UPDATE dbo.Customers SET ContactName = 'Amancio Ortega' WHERE CustomerID LIKE '%DE%'")

connection.commit()
print(f"Numero de filas afectadas : {cursor.rowcount}")

