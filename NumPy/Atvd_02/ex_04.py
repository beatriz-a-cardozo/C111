'''
    Crie uma matriz de tamanho qualquer. Extraia seu número de linhas e colunas,
    multiplique-os, e diga se esta matriz poderia se tornar um vetor unidimensional
    com número par ou ímpar de elementos.
'''

import numpy as np

mtz = np.ones([2,8]) # matriz de tamanho qualquer

lines, columns = mtz.shape # extrai o número de linhas e de colunas

total = lines * columns # multiplica o número ed colunas pelo núemro de linhas

print(total) # testando

if total % 2 == 0:
    print('A matriz poderia se tornar um vetor unidimensional com número par de elementos')
else:
    print('A matriz poderia se tornar um vetor unidimensional com número impar de elementos')
