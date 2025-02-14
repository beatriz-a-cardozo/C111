# faca um programa que leia o nome e a media de um aluno e guarde-os
# em um dicionario.

nome = input('Insira o nome completo do aluno: ')
media = int(input('Insira a media dele(a): '))

dados = {'nome' : nome, 'media' : media}

# em seguida, a partir da media (para ser aprovado deve ter media 
# >= 50), gere a situacao final do aluno ('AP' ou 'RP'), que 
# tambem dever ser guardada neste dicionario.

if media>=50:
    dados['status'] = 'AP'
else:
    dados['status'] = 'RP'

# No final, mostre todo o conteudo deste dicionario
print(dados)