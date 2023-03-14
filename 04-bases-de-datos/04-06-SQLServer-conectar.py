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

# Ejemplos de comandos SELECT 
# para recuperar registros de la BD

cursor.execute("SELECT * FROM dbo.Customers")

# mostramos el contenido del cursor mediante FOR
for row in cursor.fetchall():
    print(f"     ID : {row['CustomerID']}")
    print(f"Empresa : {row['CompanyName']}\n")

print("(========================)\n")

# Filtrar datos
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = 'USA'")

# mostramos el contenido del cursor mediante FOR
for row in cursor.fetchall():
    print(f"     ID : {row['CustomerID']}")
    print(f"Empresa : {row['CompanyName']}")
    print(f"Empresa : {row['Country']}")
    print(f"Empresa : {row['City']}\n")

print("(========================)\n")

# Filtrar datos con comodines
cursor.execute("SELECT * FROM dbo.Customers WHERE Country = %d", "Spain")

# mostramos el contenido del cursor mediante FOR
for row in cursor.fetchall():
    print(f"     ID : {row['CustomerID']}")
    print(f"Empresa : {row['CompanyName']}")
    print(f"Empresa : {row['Country']}")
    print(f"Empresa : {row['City']}\n")

print("(========================)\n")


# Ordenar por ciudad
cursor.execute("SELECT CustomerID, CompanyName, Country, City FROM dbo.Customers WHERE Country = %d ORDER BY City", "Spain")

# mostramos el contenido del cursor mediante FOR
for row in cursor.fetchall():
    print(f"     ID : {row['CustomerID']}")
    print(f"Empresa : {row['CompanyName']}")
    print(f"Empresa : {row['Country']}")
    print(f"Empresa : {row['City']}\n")

################################################

# Insertar en la base de datos
resultado = cursor.execute("INSERT INTO dbo.Customers(CustomerID, CompanyName, ContactName, City, Country) VALUES('DEMO9', 'Comidas 1 2 3, SL', 'Borja Cabeza', 'Madrid', 'Spain')")


# utilizamos la funcion commit para confirmar la transacion
# y las operaciones de insercion, actualización y borrado
#connection.commit()
