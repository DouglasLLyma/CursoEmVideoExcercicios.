# Crie um programa que leia o nome completo
# de uma pessoa e mostre:
# O nome com todos as letras maiúsculas.
# O nome com todas as letras minúsculas.
# Quantas letras [sem espaço].
# Quantas letras tem o primeiro nome.
nome= str(input('Digite sem nome Completo: ')).strip()
print('O nome em Maiúsculo:{}!'.format(nome.upper()))
print('O nome em Minúsculo:{}!'.format(nome.lower()))
variavel = nome.replace(' ','')
print('A frase contém {} caracteres!'.format(len(variavel)))
var = nome.split()
print('O primeiro nome contém {} caracteres!'.format(len(var[0])))


