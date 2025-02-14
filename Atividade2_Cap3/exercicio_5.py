# desenvolva um programa que leia o nome, idade e sexo de n pessoas
flag = True 
dados = []
total_idade = 0
contador = 0
m_menor20 = 0

while flag:
    nome = input('insira o nome: ')
    idade = int(input('insira a idade: '))
    
    wrong = True
    while wrong:
        sexo = input('insira o sexo (M) ou (H): ').upper()

        if sexo != 'M' and sexo != 'H':
            print('entrada invalida, tente novamente.')
        else:
            wrong = False
    
    dados.append({'nome' : nome, 'idade' : idade, 'sexo' : sexo})
    contador += 1
    total_idade += idade

    if sexo=='M' and idade<20:
        m_menor20 += 1

    aux = input('deseja adicionar mais alguem para a pesquisa? (sim/nao)').lower()

    if aux!='sim':
        flag = False
    
# mostre a media de idade do grupo e quantas mulheres tem menos de 
# 20 anos
if contador>0:
    media_total = total_idade/contador
    print(f'a medida de idades do grupo e: {media_total:.2f}')
else:
    print('nenhum dado foi inserido')

print(f'a quantidade de mulheres com menos de 20 anos e: {m_menor20}')
