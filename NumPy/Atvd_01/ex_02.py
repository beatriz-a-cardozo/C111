'''
    Crie dois NumPy Arrays unidimensionais: um de números pares de 0 à 51
    e outro também de números pares de 100 até 50.
'''
import numpy as np

arr_1 = np.arange(0,51,2) # definindo um array com: first element=0, last element=51, step=2
#print(arr_1) # testando

arr_2 = np.arange(100,50,-2) # definindo um array com: first element=100, last element=50, step=-2
#print(arr_2) # testando

'''
    Em seguida, os concatene e mostre o resultados ordenados
'''
arr_resultado = np.concatenate((arr_1,arr_2)) # concatena os dois arrays definidos e os armazena em arr_resultado
print(arr_resultado) # imprime o resultado do arr_resultado no terminal

'''
    se quiser ver o processo, é só remover os comentários que estão marcados
    como testando !
'''