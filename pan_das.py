import pandas as pd
import numpy as np
#Series
ciudades = ['cali','Barranquilla','Bucaramanga','Bogota']
A = pd.Series(ciudades)
print(ciudades)
print(A)
print(A[1])
diccionario = {
    'enero':5000000,
    'febrero':150000000000,
    'marzo':6000000,
}

B = pd.Series(data = diccionario, index = list(diccionario.keys()))
print(B)
print(B['febrero'])
print(B[1])

#DataFrame apartir de un diccionario

inventario = {
    'impresoras': ['Hp', 'Canon', 'Epson'],
    'Cantidad' : [ 50, 40, 80]
}
InventrioDF = pd.DataFrame(inventario)
print(InventrioDF)
#Dataframe apartir de un diccionario que contenga una Serie
diccionario2 = {
    'columna1':[20,80,41,10],
    'columna2': pd.Series(ciudades)
}

DF1 = pd.DataFrame(diccionario2)
print(DF1)

#DataFrame apartir de un Array de Numpy
arreglo = np.array([[4,8,9],[8,8,8],[3,8,5]])

DF2 = pd.DataFrame(arreglo, columns = ['Vainilla','Chocolate','Cereza'], index = ['Lunes','Martes','Miercoles'])
print(DF2)
#metodo Loc
print(DF2.loc['Lunes'])
print(DF2.loc[{'Lunes','Martes'}])
#print(DF2.loc[0]) No se puede 
#Metodo iloc
print(DF2.iloc[-1])
print(DF2.iloc[[0,2]])

