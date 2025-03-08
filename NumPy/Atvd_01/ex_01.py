''' Crie dois NumPy Arrays unidimensionais de tamanho 8: um formado apenas por 1's e
    outro fomado por números aleatórios entre 0 e 9. Some estes dois NumPy Arrays 
    e guarde o resultado dentro de um terceiro NumPy Array.'''

import numpy as np

arr_1 = np.array([1,1,1,1,1,1,1,1]) # definindo o array de 1's
arr_2 = np.random.randint(0,10,8) # definindo o array de números aleatórios

#print(arr_1) # testando
#print(arr_2) #testando

arr_soma = np.array(arr_1 + arr_2) # soma dos dois arrays
#print(arr_soma) # testando

''' Por fim, se a soma de todos os elementos do Array resultande for >=40,
    remodele esse NumPy Array para se tornar uma matriz com mais linhas do que 
    colunas. Senão, remodele para que se torne uma matriz com mais colunas que
    linhas.'''

soma_elem = arr_soma.sum() # soma os elementos do array somado
#print(soma_elem) # testando

if soma_elem>=40: # caso a soma dos elementos do array_soma seja maior ou igual a 40:
    mtz = arr_soma.reshape(4,2) # remodela o array para uma matriz 4x2
else: # caso não:
    mtz = arr_soma.reshape(2,4) # remodela o array para uma matriz 2x4

print(mtz) # imprime a resposta final

'''
    se quiser ver o processo, é só remover os comentários que estão marcados
    como testando !
'''

