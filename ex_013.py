# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.
salario = float(input('Salário atual: '))
aumento = ((salario/100)*15+salario)
print('Novo salário {}'.format(aumento))