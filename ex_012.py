# Faça um algoritmo que leia o preço de um produto e mostre
# seu novo preço, com 5% de desconto
preco = float(input('Qual o valor do produto: '))
des = (preco/100)*95
print('O Valor com desconto é {:.2f}'.format(des))
