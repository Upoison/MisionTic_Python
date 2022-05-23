#sintaxis
#reduce(funcion, objeto iterable)
# la funcion debe tener dos parametros obligatorios, uno que actue como acomulador y otro que actue como elemento.
from funtools import reduce
lista = [4,5,8,9]
# forma imperactiva

acumulador = 0
for i in lista:
    acumulador +=i
print(acumulador)
# forma funcional

resultado = reduce(lambda acumulador, numero: acumulador + numero, lista,40)
print(resultado)
#resultado = reduce(lambda acumulador, numero: acumulador + numero**2, lista)
print(resultado)