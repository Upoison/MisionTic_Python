# Realice un programa que lea el código de un producto como llave de un 
# diccionario y en dicha llave va a almacenar nombre, precio y cantidad 
# del producto en una lista.
# El programa debe permitir cargar datos al diccionario, debe mostrar 
# un listado completo del diccionario y debe permitir consultar un producto 
# por su llave.

def crear(producto):
    codigo = int(input('Ingrse el codigo del producto\n'))
    nombre = input('Ingrese el nombre del producto\n')
    precio = int(input('Ingrese el precio del produto\n'))
    cantidad = int(input('Ingrese la cantidad del producto\n'))
    productos.setdefault(codigo,[ nombre, precio, cantidad])
    return productos

def mostrar(productos):
    print('Listado de productos')
    for i in productos:
        print(i, productos[i][0], productos[i][1], productos[i][2])

def consultar(productos):
    cod = int(input('Ingrse el cod del producto\n'))
    if cod in productos:
        print(productos[cod][0], productos[cod][1], productos[cod][2],)

continuar ='s'
productos = {}
while continuar == 's' or continuar == 'S':
    print('MENU')
    print('1. Crear producto')
    print('2. Mostrar producto')
    print('3. Consultar')
    opcion = int(input(f'Digite una opcion\n'))
    if opcion == 1:
        print(crear(productos))
        print("producto creado")
    elif opcion == 2:
        print(mostrar(productos))
    elif opcion == 3:
        print(consultar(productos))
    else:
        print('Digite un valor valido')
    continuar = input('Presione "s" para continuar o culaquier letra para salir\n')



