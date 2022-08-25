# Desenvolva um programa que leia as duas notas de um aluno,
# calcule e mostre a sua média.
nota1 = float(input('Nota 1° Semestre; '))
nota2 = float(input('Nota 2° Semestre: '))
media = float((nota1+nota2)/2)
print('1° Nota  = {}, 2° Nota {} . Média {}'.format(nota1, nota2, media))
