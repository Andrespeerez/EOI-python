import sqlite3, json

disco = False
if(disco):
############################################################
# Conexion con db
    conn = sqlite3.connect('basedatos.db') # si no existe lo crea
else:
############################################################
# Conexion con db en memoria RAM!!
    conn = sqlite3.connect(':memory:') 

############################################################
# Crea el cursor
cursor = conn.cursor()

############################################################
# Consultamos si existe alguna tabla en la BD
# Si la tabla no existe, se crea
commando = "SELECT count(*) FROM sqlite_master WHERE type = 'table' AND name = 'Alumnos'"
cursor.execute(commando)

numTables = cursor.fetchone()[0] # cursor contiene una tupla

print(f"Numeros de tablas Alumnos: {numTables}") 

# Si no existe la creamos
if(numTables == 0):
    commando = """CREATE TABLE Alumnos (id, nombre, apellidos, curso, notas)"""

    cursor.execute(commando)
    print(f"Tablas creada")


############################################################
# Insertar datos con INSERT
insertar_1 = True
if(insertar_1):
    command = """
        INSERT INTO Alumnos(id, nombre) VALUES('000', 'Andres')
        """
    cursor.execute(command) 
    conn.commit()
    print("Registro Insertado")

    command = """
        INSERT INTO Alumnos VALUES('001', 'Sara', 'Martinez', '2A', Null)
        """
    cursor.execute(command)
    conn.commit()
    print("Registro Insertado")

insertar_mas = True
if(insertar_mas):
    lista = [
        ('002', 'Ana', 'Trujillo', '2c', None),
        ('003', 'Adrian', 'Sánz', '2A', json.dumps([7.5, 6, 9, 5, 6.9])),
        ('004', 'María', 'Sánchez', '2B', None)
    ]
    command = """
        INSERT INTO Alumnos VALUES( ? , ? , ? , ? , ? )
        """
    cursor.executemany(command, lista)
    conn.commit()
    print(f"Numero de registros insertados: {cursor.rowcount}")


############################################################
# Consultar datos con SELECT
command = """
    SELECT * FROM Alumnos
        """
cursor.execute(command)

registro = cursor.fetchone()
while(registro):
    print(registro)
    registro = cursor.fetchone()


############################################################
# Actualizar un registro utilizando UPDATE
update = True
if(update):
    command = "UPDATE Alumnos SET apellidos = 'Perez' WHERE id = '000'"
    cursor.execute(command)
    conn.commit()
    print("Numero de registros actualizados: ", cursor.rowcount)

############################################################
# Actualizar un registro utilizando DELETE
delete = True
if(delete): 
    command = "DELETE FROM Alumnos WHERE id = '004'"
    cursor.execute(command)
    conn.commit()
    print("Numero de registros eliminados: ", cursor.rowcount)

print()
############################################################
# Consultar datos con SELECT
command = """
    SELECT * FROM Alumnos
        """
cursor.execute(command)

for ii in cursor.fetchall():
    print(ii)
