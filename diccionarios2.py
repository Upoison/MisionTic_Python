datosPersonales = dict(nombre = 'Juan', edad = 25, direcciones = 'Av 20 1518')
print(datosPersonales)
# Metodo clear, borra un diccionario
datosPersonales.clear()
print(datosPersonales)

datosPersonales.setdefault('nombre', 'Sofia')
print(datosPersonales)

print(datosPersonales.get('nombre')) #Get obtiene el valor de una llave

print(datosPersonales.values())
print(datosPersonales.keys())

