import pandas as pd
#Tabla dinamica
#pivot table
diccionario = {
    'co2': [95, 90, 99, 104, 105, 94, 99, 104],
    'model': ['Citigo', 'Fabia', 'Fiesta', 'Rapid', 'Focus', 'Mondeo', 'Octavia', 'B-Max'],
    'car': ['Skoda', 'Skoda', 'Ford', 'Skoda', 'Ford', 'Ford', 'Skoda', 'Ford']
}

df1 = pd.DataFrame(diccionario)
print(df1)
pt = pd.pivot_table(df1, index='car', columns = 'model') 
print(pt)
pt = pd.pivot_table(df1, index='car', aggfunc=[len, max, min, sum])
print(pt)