archivo1 = open('archivo_prueba.txt')
# write('texto a escribir'), si no se pone el 'w' se sobreescribe
# Read('texto a leer') si no se pone el 'r' se lee todo el archivo
# agregar 'a' para agregar al final del archivo
for i in archivo1:
    print(i)

print(archivo1.readline()) #lee una linea
print(archivo1.read(10)) #lee 10 caracteres

archivo1.close()

archivo2 = open('archivo_prueba2.txt', 'w')
archivo2.write('Este es un texto nuevo')
archivo2.close()