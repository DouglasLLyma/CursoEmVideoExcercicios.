# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
digite = input('Digite algo: ')
print('É um número; {}'.format(digite.isnumeric()))
print('É uma palavra; {}'.format(digite.isalpha()))
print('Contém números e letras: {}'.format(digite.isalnum()))
print('Só tem espaços? {}'.format(digite.isspace()))
print('Está em maiúsculas? {}'.format(digite.isupper()))
print('Está em minusculo? {}'.format(digite.islower()))
print('Está capitalizada? {}'.format(digite.istitle()))


