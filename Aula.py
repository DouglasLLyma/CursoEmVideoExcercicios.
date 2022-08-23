#AULA - 05 (Tipo Primitivos)
# Usando a função 'type' para descobrir o tipo
# primitivo de valor
# n1 = input('Digite um Valor: ')
# print(type(n1))

# Acrecentando a função 'int' para transformar uma string em número inteiro.
# n2 = int(input('Digite um Valor: '))
# print(type(n2))

# AULA - 06
# float transforma o valor em um valor flutuante.
# n = float(input('Digite um valor: '))
# print(n)

# Para efeito de teste;
# no caso do Bool, como estamos pedindo a insersão de um númeor
# Quando digitado algo ele retorna 'True' e caso no o resultado seria 'False'
# n = bool(input('Digite um número: '))
# print(n)

# Usando o metodo 'isnumeric' é possivel saber se um valor str pode ser convertido para int, por exemplo.
# n = input('Digite Algo: ')
# print(n.isnumeric())

# Usando o metodo 'alpha' podemos constatar se é uma palavra ou não.
# n = input('Digite Algo: ')
#print(n.isalpha())

# Usando o 'isalnum' podemos saber que um determinado campo contém números e letras.
# n = input('Digite Algo: ')
# print(n.isalnum())

# Existem vários tipos de metodo 'is', geralmente esse metodo é usando para testar tipos no python.

# AULA - 07 Operações Aritmética.
# + Adição
# - Subtração
# * Multiplicação
# / Divisão
# ** Potência
# // Divisão Inteira
# % Resto da Divisão
# = Sinal de atribuição(recebe)
# == Sinal de 'Igual'

# Ordem de Precedência
# 1° ()
# 2° **
# 3° *, /, //, %
# 4° + , -

n1 = 5
n2 = 2
n3 = 3
procedencia = (n1 + n3 * n2)
print('Nessa operação primeiro faremos {} * {} + {} que é igual a {}'.format(n3,n2,n1,procedencia))
print('Resultado;'
    '\nSoma= {}'
    '\nSubtração= {}'
    '\nMultiplicação= {}'
    '\nDivisão= {}'
    '\nPotência= {}'
    '\nDivisão Inteira= {}'
    '\nResto da Divisão= {}'
    .format(n1+n2, n1-n2, n1*n2, n1/n2, n1**n2, n1//n2, n1%n2))

