'''
    Baseado no dataset 'paises.csv' fornecido, crie códigos em Python que respondam
    às seguintes perguntas.
'''

import numpy as np

dataset = np.loadtxt('Python\C111\Exercicio_extra\paises.csv', delimiter=';', dtype=str, encoding='utf-8')

'''
    1. Faça um slicing no dataset para mostrar apenas o País(Country), Região(Region),
    População(Population) e Area(Area (sq.mi.)) dos países contidos nele.
'''

# [0] Country; 
# [1] Region; 
# [2] Population; 
# [3] Area (sq. mi.);
# [4] Pop. Density (per sq. mi.); 
# [5] Coastline (coast/area ratio); 
# [6] Net migration;
# [7] Infant mortality (per 1000 births);
# [8] GDP ($ per capita);
# [9] Literacy (%);
# [10] Phones (per 1000);
# [11] Arable (%);
# [12] Crops (%);
# [13] Other (%);
# [14] Climate;
# [15] Birthrate;
# [16] Deathrate;
# [17] Agriculture;
# [18] Industry;
# [19] Service

dataset_red = dataset[:, :4] # slicing de dados para mostrar apenas os 4 primeiros
                             # índices do dataset original

print('Questao 1')
print('Segue as primeiras linhas do dataset reduzido:')
print(dataset_red[:5,:])

'''
    2. Conte e em seguida mostre quais são as diferentes regiões do planeta segundo
    este dataset.
'''

regions = np.unique(dataset[1:,1]) # guarda cada valor (str) diferente que aparece
                                   # na coluna 1

print('\nQuestao 2')
for region in regions:
    print(region)

'''
    3. Mostre qual a taxa média de alfabetização (Literacy(%)) do planeta segundo
    este dataset.
'''

taxa = np.mean(dataset[1:,9].astype(float)) # calcula a média dos valores da
                                            # coluna 9 (Literacy)

print('\nQuestao 3')
print(f'A media de alfabetizacao d planeta eh: {taxa:.2f}%')

'''
    4. Conte quantos paises são da América do Norte (Northern America) segundo
    este dataset
'''

find_na = np.char.find(dataset[1:,1], 'NORTHERN AMERICA                   ')
find_na += 1

print('\nQuestao 4')
print(f'A quantidade de paises que sao da America do Norte sao: {find_na.sum()}')


'''
    5. Encontre qual país da América do Sul e Caribe(LATIN AMER & CARIB) possui a 
    maior renda per capita(GDP($ per capita))
'''

biggest_gdp = np.argmax(dataset[1:,8].astype(float)[dataset[1:,1]=='LATIN AMER. & CARIB    '])+1

print('\nQuestao 5')
print(f'O pais com a maior renda per capita é o(a) {dataset[biggest_gdp,0]}com {dataset[biggest_gdp,8]} de renda per capita')