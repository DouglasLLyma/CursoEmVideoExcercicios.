# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
n = float(input('Quando dinheiro você tem: '))
dolar = n / 5.11
print('Você tem R$ {:.2f} , equivalente a U$ {:.2f}'.format(n, dolar))