# Escreva um programa que pergunta a quantidade de KM
# percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro
# custa R$ 60 por dia e R$ 0,15 por km rodado.
km = float(input('Quantos km rodados: '))
dias = int(input('Quantos dias: '))
pg = (km*0.15)+(dias*60)
print('Você rodou {}km por {} dias e o preço a pagar é de R${:.2f}:'.format(km, dias, pg))
