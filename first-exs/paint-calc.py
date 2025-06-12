#Create a program to read the height and the width of a wall.
#Calculate the area and quantity of paint necessary.
#Consider each liter of paint enough for two squares meters.

import math

altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))

area = altura * largura
galao = math.ceil(area / 2)

print('Cada galão de tinta pinta 2m quadrados, logo, ', end='')
print('precisará de {} galões para pintar a parede.'.format(galao))
