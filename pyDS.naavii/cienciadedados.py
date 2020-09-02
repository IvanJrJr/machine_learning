import pandas as pd

data = {
        'Alunos': ['João', 'Caio', 'Joana'],
        'Idade': [15, 16, 15],
        'Notas': [6.5, 6.7, 9.0]
        }

df = pd.DataFrame(data, columns=['Alunos', 'Idade', 'Notas'])

df.describe() # Descreve media, mediana, quantidade de linhas.

df.count() # Descreve a quantidade de linhas.

df.columns # quantidade de colunas que foram programadas 

df.shape # Linhas e colunas

df.max() # Maior valor, com strings mostra em ordem alfabetica descrescente

df['Idade'].max() # Valor maximo de idade

df.min() # Menor valor 

df['Notas'].min() # valor minimo de nota

df.mean() # media 

df.median() # mediana

df.sum() # concatena strings e soma todos os valores

df['Notas'].add(10) # soma o valor 10 a um determinada coluna 'Notas'

df['Notas'].sub(10) # subtrai o valor 10 a uma determinad coluna

df['Notas'].mul(10) # multiplica o valor 10 a uma determinad coluna

df['Notas'].div(10) # divide o valor 10 a uma determinad coluna

xnota = df['Notas'][2]

df.head() #mostra as 5 primeiras linhas

df.tail() # mostra as 5 ultimas linhas

df.loc[df['Notas'] <= 8] # busca valores especificos

