# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida a primeiro e o último nome separadamente.
n = str(input('Digite seu nome: ')).strip()
nome = n.split()
print('Prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu Ultimo nome é {}'.format(nome[len(nome)-1]))