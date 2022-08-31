# Faça um programa que leia a largura e a altura de uma parede
# em metros, calcule a sua área e quantidade de tinta necessária pra
# pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}X{} e sua área é de {}m.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar sua parede, você precisa de {}L de tinta'.format(tinta))
