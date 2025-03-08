'''
    Crie uma matriz de tamanho 4x4 formada por números aleatórios inteiros
    entre 1 e 50 (use seed = 10 antes)
'''

import numpy as np

np.random.seed(10) # permite que os números aleatórios sejam produzidos iguais
mtz = np.random.randint(1,50,[4,4]) # gera uma matriz 4x4 com números inteiros aleatórios

print(mtz) # testando

'''
    a. Mostre o resultado da média de cada linha e cada coluna da matriz 
    gerada
'''

md_lines = mtz.mean(axis=1) # calcula a média de cada linha
md_columns = mtz.mean(axis=0) # calcula a média de cada coluna

print('Média de cada linha: ')
print(md_lines) # imprime o valor da média de cada linha
print('Média de cada coluna: ')
print(md_columns) # imprime o valor da média de cada coluna da matriz

'''
    b. Apresente o maior valor das médias das linhas e também das colunas
'''

max_md_lines = np.max(md_lines)  # maior valor das médias das linhas
max_md_columns = np.max(md_columns)  # maior valor das médias das colunas

print('Maior média das linhas: ')
print(max_md_lines)
print('Maior média das colunas: ')
print(max_md_columns)

'''
    c. Mostre a quantidade de aparições de cada um dos números gerados na matriz.
    Em seguida, mostre apenas os números que aparecem 2 vezes.
'''

unique_numbers, counts = np.unique(mtz, return_counts=True) #conta a quantidade de aparições de cada número na matriz

print('Quantidade de aparições de cada número:')
for number, count in zip(unique_numbers, counts):
    print(f'Número {number}: {count} vez(es)')


numbers_appearing_twice = unique_numbers[counts == 2] # filtra os números que aparecem exatamente 2 vezes
print('Números que aparecem 2 vezes:')
print(numbers_appearing_twice)