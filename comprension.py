lista = []

for i in range(1, 11):
    lista.append(i)
print(lista)

#Comprension de lista
lista2 = [i for i in range(1, 11)]
print(lista2)
lista2 = [i**2 for i in range(1, 11)]
print(lista2)

lista = ['Marina', 'Oscar', 'Juan', 'Sofia', 'Laura']
lista2 = [i.lower() for i in lista]
print(lista2)