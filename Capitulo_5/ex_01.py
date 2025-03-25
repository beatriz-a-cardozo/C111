import pandas as pd
import numpy as np
'''
    Crie duas Séries com os seguintes valores:
        - seriesAno1:{'Java': 16.25, 'C': 16.04, 'Python': 9.85}
        - seriesAno2:{'C': 16.21, 'Python': 12.12, 'Java': 11.68}
'''

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68}) 

print('Questao 1:')
print('seriesAno1:')
print(seriesAno1)
print('\nseriesAno2:')
print(seriesAno2)

'''
    Os valores das Series criadas na Questão 1 representam as fatias de mercado 
    (porcentagem) de 3 linguagens de programação populares em dois anos 
    consecutivos. Para cada ano, apresente a porcentagem total que elas juntas 
    representam no mercado.
'''

print('\nQuestao 2:')
print(f'Portcentagem total do ano 1: {np.sum(seriesAno1)}')
print(f'Portcentagem total do ano 2: {np.sum(seriesAno2)}')

'''
    Apresente o crescimento/declínio no mercado de cada linguagem do primeiro
    ano para o segundo ano.
'''

diferenca = seriesAno2.sub(seriesAno1)
print('\nQuestao 3')
print('Aqui esta a diferenca das linguagens do ano 1 para o ano 2:')
print(diferenca)

'''
    Baseado nos resultados da Questão 3, mostre apenas os dados das linguagens
    que tiveram crescimento.
'''

print('\nQuestao 4')
print('O(s) dado(s) que teve/tiveram um crescimento foi/foram: ')
print(diferenca[diferenca>0])

'''
    Se estas porcentagens de crescimentos/declínio se mantivessem iguais para
    os próximos 2 anos, qual seria a linguagem mais popular?
'''

futuro = seriesAno2.add(2*diferenca)
print('\nQuestao 5')
print('Assim ficariam as porcentagens das linguagens caso o crescimento/declinio continuasse o mesmo:')
print(futuro)

'''
    Utilizando do DataFrame exemplo do tópico 5.3 deste material, calcule a 
    média dos elementos da coluna X que são menores que 30.
'''
np.random.seed(10)

df = pd.DataFrame(
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['W', 'X', 'Y', 'Z'],
    data=np.random.randint(1, 50, [5, 4])
    )

media = df[df['X'] < 30]['X'].mean()
print('\nQuestao 6')
print(f'A media dos elementos da coluna X menores que 30 é: {media}')

'''
    Utilizando do mesmo DataFrame, apresente a média dos elementos da tinha D
    usando a função loc() como base e a soma dos elementos da linha E usando a
    função iloc() como base
'''

linha_d = np.mean(df.loc['D'])
linha_e = np.sum(df.iloc[4])
print('\nQuestao 7')
print(f'A media dos elementos da linha D eh: {linha_d}')
print(f'A soma dos elementos da linha E eh: {linha_e}')

'''
    Faça um Slicing na matriz mostrando apenas as linhas A, C e E juntamente
    com as colunas X e Y. Em seguida, mostre qual seria a soma dos elementos 
    de cada uma destas linhas e cada uma destas colunas
'''

slicing = df.loc[['A','C','E'],['X','Y']]
print('\nQuestao 8')
print('A soma das linhas eh:')
print(slicing.sum(axis=1))
print(f'A soma das colunas eh:')
print(slicing.sum(axis=0))