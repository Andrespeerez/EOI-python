#!/usr/bin/python3

# Installar pytz para zonas horarias
# en Linea de comandos
# pip install pytz

from datetime import datetime, timedelta
from pytz import timezone
import pytz

# Mostrar las zonas horarias disponibles
# print(pytz.all_timezones)
print()

# Mostrar la fecha actual
dt = datetime.now()
print(dt)
print(datetime.now(pytz.timezone("Asia/Tokyo")))
print(datetime.now(pytz.timezone("Europe/Madrid")))
print(datetime.now(pytz.timezone("US/Alaska")))
print(datetime.now(pytz.timezone("UTC")))