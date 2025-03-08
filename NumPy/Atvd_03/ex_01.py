'''
    Baseado nos comandos que vimos até o momento e no Dataset fornecido,
    crie scripts em Python que respondam às seguintes perguntas:
'''
import numpy as np

dataset = np.loadtxt('Atvd_03\space.csv',delimiter=';',dtype=str,encoding='utf-8') # carrega o arquivo do  Dataset fornecido
# print(dataset) # testando

'''
    1. Apresente a porcentagem de missões que deram certo.
'''
lines, columns = dataset.shape # usado para verificar o tamanho da matriz 
# print(lines, columns) # testando 
mission_su = np.char.find(dataset[1:,7], 'Success') # procura por casos de 'Sucesso' na coluna 7 do dataset
# print(mission_su) # testando

success = np.sum(mission_su != -1) # soma todos os casos de sucesso que foraam encontrados

# cálculo da porcentagem de sucesso
porcent =  (success/(lines-1)) * 100 # explicando o por que do '-1', a função linha conta a quantidade
                                     # de linhas totais, mas no arquivo também tem o cabeçalho

print(f'Missões sucedidas: {porcent} %') # imprime a porcentagem de missões que edram certo
'''
    2. Qual a media de gastos de uma missão espacial se baseando em missões que 
    possuam valores disponíveis (>0)?
'''

# filtra pela coluna de custos, transforma seus valores em float e filtra os valores maiores que 0 para calcular a média
md_cost = np.mean(dataset[1:,6].astype(float)[dataset[1:,6].astype(float)>0])

print(f'A média de gastos de uma missão espacial: $ {md_cost}')

'''
    3. Encontre quantas missões espaciais neste Dataset foram realizadas pelos 
    Estados Unidos (EUA).
'''

mission_usa = np.char.endswith(dataset[:,2],'USA') # procura na coluna de localização (2) por strings que terminam com USA
print(f'Número de missões realizadas pelos EUA: {np.sum(mission_usa)}') # imprime a soma dos valores (já que False = 0 e True = 1, a soma é a quantidade missões no EUA)

'''
    4. Encontre qual foi a missão  mais cara realizada pela empresa "SpaceX"
'''
spacex = dataset[dataset[:, 1]=='SpaceX'] # separa as missões da SpaceX em uma matriz diferente
# print(spacex) # testando
spacex_exp = spacex[:,6].argmax() # guarda o indice da missão da spacex que custou mais cara
# print(spacex_exp) # testando

# imprime qual foi a missão da spacex que custou mais cara e mostra alguns detalhes adicionais
print(f'A missão mais cara realizada pela Space X foi a missão {spacex[19,0]}, que custou {spacex[19,6]} e ocorreu em {spacex[19,3]}')

'''
    5. Mostre o nome das empresas que já realizaram missões espaciais, juntamente
    com suas respectivas quantidade de missões (use o for no final para mostrar 
    as informações)
'''
companies, counts = np.unique(dataset[1:,1], return_counts=True) # retorna as empresas unicas que aparecem no dataset e a frequencia

for company, count in zip(companies, counts):
    print(f'{company}: {count} vez(es)') # imprime caa compania e quantas vezes apareceu

