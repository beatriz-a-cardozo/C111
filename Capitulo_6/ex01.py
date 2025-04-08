import numpy as np
import matplotlib.pyplot as plt

'''
    1. Por meio do dataset paises.csv, trace dois gráficos de linhas em um 
    mesmo plano cartesiano um mostrando a taxa de mortalidade (Deathrate) 
    e outro a taxa de natalidade (Birthrate) dos países da América de Norte.
'''

dataset = np.loadtxt('Python\C111\Capitulo_6\paises.csv', delimiter=';', dtype=str, encoding='utf-8')

# separando os países da América do Norte dos outros
dt_na = dataset[dataset[:,1]=='NORTHERN AMERICA                   ']

y = dt_na[:,16].astype(float) # criando y com os valores de Deathrate
y2 = dt_na[:,15].astype(float) # criando y2 com os valores de Birthrate

line,columns = dt_na.shape # armazenando o tamanho da matriz dt_na
x = np.arange(0,line,1)

plt.plot(x,y,'r-',x,y2,'b--')
plt.show() # mostrando o gráfico

'''
    2. Por meio do dataset space.csv, trace um gráfico em barras mostrando 
    quantas empresas espaciais diferentes os EUA e a CHINA possuem.
'''
# importando o dataset de space.csv
dataset2 = np.loadtxt('Python\C111\Capitulo_6\space.csv', delimiter=';', dtype=str, encoding='utf-8')

dt_eua = dataset2[np.char.endswith(dataset2[:, 2], 'USA')] # separando os dados que vem dos Estados Unidos
dt_ch = dataset2[np.char.endswith(dataset2[:, 2], 'China')] # separando os dados que vem da China

count_eua = len(np.unique(dt_eua[:,1])) # tamanho de empresas unicas
count_ch = len(np.unique(dt_ch[:,1])) # tamanho de empresas unicas

countries = ['Usa', 'China'] # separando em um array para o eixo x
count = [count_eua,count_ch] # separando a quantidade em um array para o eixo y
plt.bar(countries,count,color=['blue','red']) # gerando o gráfico de barras
plt.show() 

'''
    3. Por meio do dataset space.csv, trace um gráfico em torta ilustrando
    a porcentagem de missões da empresa Roscosmos que deram certo e que
    deram errado.
'''

rosco = dataset2[dataset2[:,1]=='Roscosmos'] # slicing dos dados da empresa roscosmos

success = len(rosco[rosco[:,7]=='Success']) # quantidade de sucessos
failed = len(rosco[rosco[:,7]=='Failure']) # quantidade de falhas
partial_failure = len(rosco[rosco[:,7]=='Partial Failure']) # quantidade de falhas parciais

plt.pie(
    x=[success,partial_failure,failed],
    labels=['Sucedidas','Parcialmente falhas','Falhas'],
    colors=['green','orange','red'],autopct='%1.1f%%'
    ) # gerando o gráfico torta
plt.show()



