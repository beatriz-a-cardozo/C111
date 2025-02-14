# faca um programa que leia o nome e peso de 3 pessoas

i = 0
dados = []
for i in range(3):
    nome  = input('insira o nome do paciente: ')
    peso = float(input('insira o peso deste paciente: '))

    dados.append({'nome' : nome, 'peso' : peso})
    
    i += 1
# no final mostre o nome da pessoa mais pesada e a mais leve
j = 1
for j in range(3):
    
    if dados[j]['peso'] > dados[j-1]['peso']:
        pesada = dados[j]['nome']
    elif dados[j]['peso'] < dados[j-1]['peso']:
        leve = dados[j]['nome']
    j += 1

print('O paciente mais pesado e: ' + pesada)
print('O paciente mais leve e: ' + leve)