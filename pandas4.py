import pandas as pd
df1 = pd.read_csv('surveys.csv')
df2 = df1['month'] #crea un subconjunto del dataframe
print(df2, type(df2))
df3 = df1[['species_id', 'plot_id']] #crea un subconjunto del dataframe
print(df3, type(df3))