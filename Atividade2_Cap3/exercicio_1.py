# Crie uma lista preenchida com os 5 primeiros colocados de um Campeonato 
# de Futebol, na ordem de colocação.

colocados = ['Real Madrid', 'Barcelona','Bayern de Munique','Liverpool','Manchester City']

# Mostre o 3 primeiros colocados:
print(colocados[:3])
# Mostre os ultimos 2 colocados:
print(colocados[3:])
# Motre uma lista com o times em ordem alfabetica
colocados.sort()
print(colocados)
# Em que posicao da lista se encontra o Barcelona:
colocado = colocados.index('Barcelona')
print('Na lista de colocados normal: ' + str(colocado))

