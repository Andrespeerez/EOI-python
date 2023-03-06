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