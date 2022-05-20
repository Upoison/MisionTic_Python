# Funcion lambda o funcion anonima 
# la sintaxis de lambda es:
# 1° la palabra lambda : cuaerpo de la funcion

conteo = lambda a: a+1
print(conteo(6), type(conteo))

def operaciones (a , b, fn):
    return fn(a , b)

suma = operaciones(10,8,lambda x,y: x+y)
print(suma)

resta = operaciones(25,19, lambda x,y: x-y)
print(resta)