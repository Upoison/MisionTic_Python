# Una Tupla es una coleccion de datos que se ustiliza para guardar varios elementos
# las tuplas tambien son ordenadas e idenxadas pero las tuplas son inmutables

frutas = ('manzana', 'piña', 'pera')
print(frutas)
print(type(frutas))
print(frutas[2])
#frutas[2] = 'coco' ##no se puede hacer porque las tuplas son inmutables

tupla1 = ('juan','50', True, [50, 25, 40])
print(tupla1)
tupla1[3][1] = 100 #Internamente la tupla si es modificable
print(tupla1)

def operaciones(a,b):
    suma = a+b 
    resta = a-b 
    mult = a*b 
    div = a/b 
    return suma, resta, mult, div

resultados = operaciones(50,100)
print(resultados)
print(type(resultados))

a = (3,) #si la tupla es de un solo elemnetos entonces se le coloca una coma(,)
b = ('marina',)
c = (True,)
print(type(a), type(b), type(c))
tupla2 = (8,5,4,7,8,5)
lista = list(tupla2)
print(tupla2, lista)