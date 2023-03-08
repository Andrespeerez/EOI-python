demo = lambda nombre : print(f"Hola, me llamo {nombre}")

demo("Ana")

####################################

def sumar(num):
    return lambda a : a + num

def restar(num):
    return lambda a : a - num

resta2 = restar(2)

print(resta2(3))

def calcular(formula, valor):
    return formula(valor)

print(calcular(sumar(3), 4))

#####################################
# queremos una funcion que devuelva los valores > 100

numeros = [1, 85, 200, 15, 152, 450, 5, 3601, 63, 77, 8]

def Func1(x):
    if(x > 100):
        return True
    else:
        return False

# Opcion de filtrado con una funcion
def MayorDeCien(lista):
    resultado = []

    for ii in lista:
        if(Func1(ii)):
            resultado.append(ii)

    return resultado

print(MayorDeCien(numeros))

# Opcion de filtrado usando filter()
"""
filter(funcion, objeto) se usa para filtrar un objeto utilizando una funcion
que devuelva true o false. Esta devuelve otro objeto que podemos convertir en
una lista.
"""
print(list(filter(Func1, numeros)))

print(list(filter(lambda x: x > 100, numeros))) # Sin necesidad de escribir la funcion


#######################################
# Crear la funcion de filtrado

def Filtrado(formula, datos):
    resultado = []
    for ii in datos:
        if(formula(ii)):
            resultado.append(ii)

    return resultado

print(f">>> {Filtrado(lambda x: x > 100, numeros)}")