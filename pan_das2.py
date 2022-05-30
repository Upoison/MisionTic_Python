import pandas

inventario = {
    'impresoras': ['Hp', 'Canon', 'Epson'],
    'Cantidad' : [ 50, 40, 80]
}

InventrioDF = pandas.DataFrame(inventario)
print(InventrioDF)