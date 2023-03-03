"""
Necesitamos calcular la velocidad en km/h pero,
los inputs los tenemos en metros por minuto

Mostraremos la velocidad en km/h y si es alta, baja o moderada

    - Alta : > 75km/h 
    - Baja : < 30km/h -
    - Moderada : 30 a 75 km/h
"""

# conversion unidades
horatomin = 60 # min
kmtometro = 1000 # metro

# entrada
print("¿Que velocidad tienes? (en metro/min)")
try: 
    entrada = float(input())
except:
    print("Introduce un número valido")
    exit()

"""
        km              metro      km        60 min 
salida  ----- = entrada ----- * ---------- * ------  
        hora            min     1000 metro    hora
"""
fConv = horatomin / kmtometro

velocidad = float(entrada) * fConv

if (float(velocidad) > 75):
    print(f"Llevas una velocidad de {velocidad} km/h\nTu velocidad es Alta")
elif (float(velocidad) < 30):
    print(f"Llevas una velocidad de {velocidad} km/h\nTu velocidad es Baja")
else:
    print(f"Llevas una velocidad de {velocidad} km/h\nTu velocidad es Moderada")