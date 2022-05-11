# Son indexadas, son inmutables
ciudad = "Cartagena"
print(ciudad[0])
print(ciudad[1])
print(ciudad[2])
print(ciudad[3])
print(ciudad[4])
print(ciudad[5])
print(ciudad[6])
print(ciudad[7])
print(ciudad[8])

print(len(ciudad))

#rebanadas
print(ciudad[0:9])
print(ciudad[:7])
print(ciudad[6:])
print(ciudad[2:7:2])
print(ciudad[:3]+ciudad[5:])
print(ciudad.replace('ta', ''))
print(ciudad)
ciudad = "Barranquilla"
print(ciudad)

for i in ciudad: # la variable i va tomando el valor de cada caracter
    print(i)
