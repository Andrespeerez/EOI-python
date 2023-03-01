#!/usr/bin/python3

from datetime import datetime as DT

# crea el objeto y le da el valor actual de la fecha
dt1 = DT.now()

print("Fecha actual:\n")

print(f"Fecha 1 completa : {dt1}")          # devuelve la fecha con la hora
print(f"Fecha 1          : {dt1.date()}")   # solo devuelve la fechas sin la hora
print("")
print("Día:", str(dt1.day).zfill(2))
print("Mes:", str(dt1.month).zfill(2))
print("Año:", dt1.year)
print(f"Hora: {dt1.hour:2}:{str(dt1.minute).zfill(2)}:{str(dt1.second).zfill(2)}")

# Transformar un string a una fecha:
# string parse to date

fecha = "09-03-1993"
dt2 = DT.strptime(fecha, "%m-%d-%Y")

print(f"\nFecha nacimiento: {dt2.date()}")

#Formatear la fecha:
print("Fecha de nacimiento:", dt2.date().strftime("%A, %d de %B de %Y"))


####### EJERCICIO ########
# Pinta la edad del individuo
años = dt1 - dt2

print(f"Tienes {años.days/365:2.0f} años")
