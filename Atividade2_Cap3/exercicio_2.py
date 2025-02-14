# Crie dois conjuntos, um para cada loja. Identifique quais
# modelos de smartphones cada uma delas vendem.

loja_a = {'iphone', 'samsung', 'motorola', 'xiaomi'} 
loja_b = {'samsung', 'nokia', 'motorola'}

# Em seguida, mostre quais modelos no total voce tera a opcao
# de comprar se visita-las.
print(loja_a | loja_b)

# Quais modelos se encontram disponiveis ambas as lojas
print(loja_a & loja_b)