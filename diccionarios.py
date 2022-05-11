# Los diccionarios son estructuras de datos que se utilizan para 
# almacenar Valores en pares clave-valor 
# ejempolo->> ' nombre' : 'Carlos'
# son mutables
# son indexados por llave

datosPersonales = {
    'nombre' : 'Carlos',
    'apellido' : 'Gutierrez',
    'edad' : 45,
    'accesoAR' : True,
    'direccion' : 'Call 20 58 99',
    'reconocimientos' : {
        2019 : False,
        2020: False,
        2021: True,
    }
}
print(type(datosPersonales))
print(type(datosPersonales['reconocimientos']))
print(type(datosPersonales['edad']))
print(datosPersonales['direccion'])
#print(datosPersonales['5']) #No se puede

for i in datosPersonales:
    print (i)

for i in datosPersonales:
    print(datosPersonales[i])

datosPersonales['edad'] = 38

print(datosPersonales)

print(datosPersonales.pop('direccion'))
print(datosPersonales)
