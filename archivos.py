import pandas as pd
#lectura de archivos
df1 = pd.read_csv('C:/Users/David7/Desktop/Python/ejemplo1.csv')
print(df1,  '\n')

#Crear un archivo csv

diccionario = {
    'first_name': ['Sigrid', 'Joe', 'Theodoric','Kennedy', 'Beatrix', 'Olimpia', 'Grange', 'Sallee'],
    'last_name': ['Mannock', 'Hinners', 'Rivers', 'Donnell', 'Parlett', 'Guenther', 'Douce', 'Johnstone'],
    'age': [27, 31, 36, 53, 48, 36, 40, 34],
    'amount_1': [7.17, 1.90, 1.11, 1.41, 6.69, 4.62, 1.01, 4.88],
    'amount_2': [8.06,  "?", 5.90,  "?",  "?", 7.48, 4.37,  "?"]
}

df2 = pd.DataFrame(diccionario)
print(df2, '\n')

df2.to_csv('archivo.csv') #guardar archivo csv
df2.to_csv('C:/Users/David7/Desktop/Python/archivo2.csv')

#leer el archivo de casos covid
#df3 = pd.read_csv('casos_covid.csv', header=None)
#print(df3.string()) visualiza todas las lineas
#print(df3)

df4 = pd.read_csv('C:/Users/David7/Desktop/Python/archivo2.csv', skiprows=1, names=['first_name', 'last_name', 'age', 'amount_1', 'amount_2'], sep=';', na_values='?')
print(df4, '\n')