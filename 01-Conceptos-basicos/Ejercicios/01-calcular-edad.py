"""
Calcula la edad y muestra un mensaje si es mayor o menor de edad.

Requerimientos funcionales:
    - Calcular la edad
        * ENTRADA date FECHA ACTUAL
        * ENTRADA date FECHA DE NACIMIENTO
        * SALIDA int EDAD
    - Mostrar si es mayor de edad
        * ENTRADA int EDAD
        * SALIDA bool / texto
    - SI no es mayor de edad, mostrar los años que le faltan
        * ENTRADA int EDAD
        * SALIDA int FALTA
"""

from datetime import datetime as dt

hoy = dt.now().date()

print("¿Qué día naciste? : (dd-mm-AAAA)")
entrada = input()

try:
    nacimiento = dt.strptime(entrada, "%d-%m-%Y").date()
except:
    print("Introduce una fecha en el formato correcto")
    exit()

edad = int((hoy - nacimiento).days/365.2421) # en años

print(f"Tienes {edad} años")

if(edad > 18):
    print("Eres mayor de edad")
elif(edad < 18):
    falta = 18 - edad
    print(f"Te faltan {falta} para ser mayor de edad")