
import numpy as np
import pandas as pd
'''
    1. Carregue o Dataset paises.csv e em seguida mostre:
'''

dbPaises = pd.read_csv('Python\C111\Capitulo_5\paises (1).csv', delimiter=';')

'''
        a. Quais são os países da OCEANIA?
'''

# armazena as linhas do database, caso o campo Região contenha OCEANIA
paises_oceania = dbPaises[dbPaises['Region'].str.contains('OCEANIA                            ')]

print('Questao 1, letra a:')
print('Paises da Oceania:')
print(paises_oceania['Country'].to_string(index=False)) # mostra no terminal apenas os países da Oceania

'''
        b. Quantos países são da OCEANIA?
'''

print('\nQuestao 1, letra b:')
print(f'{len(paises_oceania)} paises sao da Oceania.') # calcula e printa a quantindade de paises no array

'''
    2. Encontre o nome e a região do país que possui a maior população segundo 
    este Dataset
'''

maior_pais = np.argmax(dbPaises['Population'].astype(float))

print('\nQuestao 2:')
print(f"O pais com a maior populacao eh a {dbPaises.loc[maior_pais,'Country']} que fica na região da {dbPaises.loc[maior_pais,'Region']}")

'''
    3. Agrupe os países por Regiões. Em seguida, mostre a média de alfabetização
    (Literacy(%)) de cada região do planeta.
'''

group_region = dbPaises.groupby('Region') # agrupando por região
media_lit = group_region['Literacy (%)'].mean() # calcula media de alfabetização de cada região
print('\nQuestao 3')
print('Media da alfabetizacao de cada regiao:')
print(media_lit) # mostrando a média de alfabetizaão por região

'''
    4. Busque o nmome de todos os países do Dataset que não possuem costa 
    marítima (Coastline(coast/area ratio)==0) e guarde-os em um novo arquivo
    chamado noCoast.csv.
'''

noCoast = dbPaises[dbPaises['Coastline (coast/area ratio)']==0] # pega os paises que tem Coastline==0
noCoast['Country'].to_csv('noCoast.csv',sep=';') # salva o arquivo

print('\nQuestao 4')
print('Documento salvo com sucesso!')

'''
    5. Faça uma função que receba a taxa de mortalidade de cada país 
    (Deathrate) e retorne o texto 'Balanced' caso o calor seja < 9 e 'Urgent'
    caso contrário. Em seguida, crie um campo no Dataset chamado 'Humanitarian
    Help' que receba estes valores para cada país. No final, mostre o Dataset
    para verificar se a inserção da nmova coluna foi feita com sucesso.
'''

dbPaises['Humanitarian Help'] = '' # gerando uma nova coluna

i = 0

while i<len(dbPaises):

    deathrate = dbPaises.loc[i,'Deathrate'] # pega o valor de Deathrate

    if deathrate < 9:
        dbPaises.loc[i,'Humanitarian Help'] = 'Balanced'

    else:
        dbPaises.loc[i,'Humanitarian Help'] = 'Urgent'

    i += 1

print('\nQuestao 5')
print('Aqui esta o Database com uma nova coluna:')
print(dbPaises)
