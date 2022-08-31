# Crie um algoritmo que lei um número e mostre o seu dobro,
# triplo e a raiz quadrada
n = int(input('Digite um número: '))
print ('O número é {}!\n'
       'O seu dobro é {}!\n'
       'O seu triplo é {}!\n'
       'E a raiz é {:.2f}!'.format(n,(n*2), (n*3), (n**(1/2))))