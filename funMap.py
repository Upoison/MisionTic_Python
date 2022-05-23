# Sintaxis
# map(funcion, objetivo iterable)

# programacion imperativa
lista = [5,4,8,0,6,9,7]
lista2 = []
for i in lista:
    lista2.append(i**2)
print(lista2)

# programacion funcional
def cuadrado(numero):
    return numero**2
lista3 = map(cuadrado, lista)
print(lista3)

# programacion funcional lambda
lista4 = list(map(lambda numero: numero**2, lista))
print(lista4)

diccionario = {
    2019: False,
    2020: False,
    2021: True,
}
lista5 = list(map(lambda valor: not(valor), diccionario.values()))
print(lista5)
diccionario2 = dict(zip(diccionario.keys(), list(map(lambda valor: not(valor), diccionario.values()))))
print(diccionario2)