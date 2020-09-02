import pandas as pd

df = pd.read_csv('translacao.csv')

df.count()

df = df.drop('Series_title_3', axis= 1)