import pandas as pd

path = 'Demandas_Produtos.csv'
df = pd.read_csv(path)

for column in df.columns:
    
    df_stats = df[[column]].describe()
    df_stats.to_csv(f'{column}_stats.csv')