import pandas as pd
df1 = pd.read_csv('surveys.csv')
df2 = df1['month'] #crea un subconjunto del dataframe
print(df2, type(df2))
df3 = df1[['species_id', 'plot_id']] #crea un subconjunto del dataframe
print(df3, type(df3))
print(df1[50:61]) #filas de 50 a 60
print(df1)
print(df1.iloc[1]) #devuelve el registro en la posicion 1
print(df1.iloc[1,7]) #devuelve el registro en la posicion 1 y la columna 7
print(df1.iloc[0:4,1:3]) 
print(df1.iloc[[0,3,9,10],:] ) #devuelve los registros en la posicion 0,3,9 y 10
#filtrar por condiciones
print(df1[df1.year == 1985])
print(df1[df1.year>=1985]) & (df1.year<=1995) # and:& , or: |, not: ~
