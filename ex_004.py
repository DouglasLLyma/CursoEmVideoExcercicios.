# Faça um programa que leia algo pelo teclado e mostre
# na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
digite = input('Digite algo: ')
print('É um número; ',digite.isalnum())
print('É uma palavra; ',digite.isalpha())
print('Contém números e letras: ',digite.isalnum())