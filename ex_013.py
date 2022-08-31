# Faça um algoritmo que leia o salário de um funcionário e mostre
# seu novo salário, com 15% de aumento.
salario = float(input('Salário atual: '))
aumento = salario + (salario*15/100)
print('Um funcionario que ganha {:.2f}, com 15% de aumento passa a receber {:.2f}.'.format(salario,aumento))