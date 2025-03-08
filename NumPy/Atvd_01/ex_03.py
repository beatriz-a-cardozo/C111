'''
    MINI CAMPO MINADO
    a. Crie um NumPy Array 2x2 formado por apenas 0's
'''

import numpy as np

mtz = np.zeros([2,2]) # matriz 2x2 com apenas 0's
print(mtz) # testando

'''
    b. Em seguida, adicione um número 1 em uma posição aleatória dessa matriz.
'''
# flag é igual a True se o usuário quiser o teste rápido (s)
flag = str(input('deseja fazer um teste rápido [s/n]?')) == 's'
if flag:
    mtz[1,0] = 1
    print('O laoyout da matriz está abaixo: ')
    print(mtz) # testando
else:
    ran_column = np.random.randint(0,2) # gera um número aleatório entre 0 e 1 para a coluna
    ran_line = np.random.randint(0,2) # gera um número aleatório entre 0 e 1 para a linha

    mtz[ran_line,ran_column] = 1
    print(mtz) # testando

'''
    c. Faça uma entrada de dados para solicitar o usuário que faça uma jogada
    (selecione uma posição da matriz)
        i. se ele selecionar todas as posições em que o número não se encontra,
        moste a mensagem "Congratulations! You beat the game! :)"
        ii. senão, se dentro das 3 primeiras jogadas ele achar o número 1,
        mostre a mensagem "Game Over! :( Try Again!"
'''

# saida de dados bonitinha
print(' _______________________________________')
print('|                                       |')
print('|    Bem vindo ao Mini Campo Minado!!!  |')
print('|_______________________________________|')
print('')

print('... Nesse jogo, temos uma matriz 2x2 composta por 3 zeros e 1 um.')
print('    Os números estão escondidos atrás das letras a, b, c, d.')
print('    Encontre todos os zeros, mas não pode clicar no um!')

campo = '''
 ___________
|  a  |  b  |
| __________|
|  c  |  d  |
|___________|
'''

a = 0
b = 0
c = 0
d = 0
counter = 0

while True:
    print(campo)
    print()
    print('... selecione uma opção [a/b/c/d] ou desistir [q].')
    option = input('> ')

    if option=='a':

        if mtz[0,0]==0 and a==0:
            a=1
            counter += 1
            print('Nice job! Você achou um zero :)')

            campo = '''
                     ___________
                    |  0  |  b  |
                    | __________|
                    |  c  |  d  |
                    |___________|
                    '''

            if counter == 3:
                print('Congratulations! You beat the game! :)')
                break
            else:
                continue

        elif mtz[0,0]==0 and a==1:
            print('Você já escolheu a opção a, insira outra.')
        else:
            print('Game Over! :( Try Again!')
            campo = '''
                     ___________
                    |  1  |  b  |
                    | __________|
                    |  c  |  d  |
                    |___________|
                    '''
            break
    
    elif option=='b':

        if mtz[0,1]==0 and b==0:
            b=1
            counter += 1
            print('Nice job! Você achou um zero :)')

            campo = '''
                   ___________
                    |  a  |  0  |
                    | __________|
                    |  c  |  d  |
                    |___________|
                    '''

            if counter == 3:
                print('Congratulations! You beat the game! :)')
                break
            else:
                continue

        elif mtz[0,1]==0 and b==1:
            print('Você já escolheu a opção b, insira outra.')
        else:
            print('Game Over! :( Try Again!')
            campo = '''
                     ___________
                    |  a  |  1  |
                    | __________|
                    |  c  |  d  |
                    |___________|
                    '''
            break

    elif option=='c':

        if mtz[1,0]==0 and c==0:
            c=1
            counter += 1
            print('Nice job! Você achou um zero :)')

            campo = '''
                     ___________
                    |  a  |  b  |
                    | __________|
                    |  0  |  d  |
                    |___________|
                    '''

            if counter == 3:
                print('Congratulations! You beat the game! :)')
                break
            else:
                continue

        elif mtz[1,0]==0 and c==1:
            print('Você já escolheu a opção c, insira outra.')
        else:
            print('Game Over! :( Try Again!')
            campo = '''
                     ___________
                    |  a  |  b  |
                    | __________|
                    |  1  |  d  |
                    |___________|
                    '''
            break   
    
    elif option=='d':

        if mtz[1,1]==0 and d==0:
            d=1
            counter += 1
            print('Nice job! Você achou um zero :)')

            campo = '''
                     ___________
                    |  a  |  b  |
                    | __________|
                    |  c  |  0  |
                    |___________|
                    '''

            if counter == 3:
                print('Congratulations! You beat the game! :)')
                break
            else:
                continue

        elif mtz[1,1]==0 and d==1:
            print('Você já escolheu a opção d, insira outra.')
        else:
            print('Game Over! :( Try Again!')
            campo = '''
                     ___________
                    |  a  |  b  |
                    | __________|
                    |  c  |  1  |
                    |___________|
                    '''
            break 

    elif option=='q':
        print('Espero que tenha se divertido! See you soon!')
        break

    else:
        print('Opção inválida, tente novamente.')
            