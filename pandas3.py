import pandas as pd
df1 =pd.read_csv('surveys.csv')
print(df1)
print(df1.head(20))
print(df1.tail(10))
print(df1.shape)
print(df1.columns)
print(pd.unique(df1['species_id'])) #devielve una lista con los valores unicos de una columna 
print(df1['species_id'].value_counts()) #devuelve una lista con los valores unicos de una columna y su cantidad
print(df1['weight'].mean()) #devuelve una lista con los valores unicos de una columna y su cantidad
print(df1.groupby('species_id')['plot_id','sex'].count()['BA']) #devuelve la cantidad de registros que cumplen con una condicion
