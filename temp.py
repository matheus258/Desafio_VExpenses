# Desafio VExpenses Dados 
# Importando biblioteca pandas

import pandas as pd
arquivo_csv = pd.read_csv('netflix_titles.csv')


print("Vamos começar o desafio !!")
print()
"""  
    Nome das colunas que estão presentes no dataset, armazenadas na variavel 
    'nomes_colunas' como array.
"""
nomes_colunas = list(arquivo_csv.columns)
print(f"Colunas presentes: {nomes_colunas}")
print()

# Contar quantas vezes o valor 'Movie' aparece na coluna 'type'
quantidade_movies = (arquivo_csv['type'] == 'Movie').sum()

# Exibir o resultado quantidade de filmes
print(f"Quantidade de filmes disponíveis na Netflix: {quantidade_movies}.")
print()

# Contar quantas vezes cada diretor aparece
diretores_contagem = arquivo_csv['director'].value_counts()

# Filtrar os 5 diretores com mais filmes/séries
top_diretores = diretores_contagem.head(5)

# Exibir o resultado
print("Top 5 diretores com mais filmes na plataforma da Netflix: ")
print(top_diretores)
print()

# Diretores que atuam 

# Verificar quais diretores também atuaram em suas produções
diretores_que_atuaram = arquivo_csv[
    arquivo_csv.apply(lambda row: row['director'] in row['cast'].split(', ') if isinstance(row['cast'], str) else False, axis=1)
]

# Obter os nomes dos diretores únicos que atuaram
diretores_unicos = diretores_que_atuaram['director'].unique()

# Exibir os resultados
print("Diretores que também atuaram em suas produções:")
for diretor in diretores_unicos:
    print(diretor)

#
print('Gostei da forma que todas as informações dos títulos são mostradas e a descrição dos títulos listados é algo muito interessante, como a duração de cada conteúdo, pois é uma informação muito importante, e também quando se trata de série, a quantidade de temporadas.')
