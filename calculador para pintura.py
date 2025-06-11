#Fazer um programa que leia a altura e a largura de uma parede em metros
#depois calcule a sua área e a quantidade necessária de tinta para pintá-la
#considere que cada litro pinta 2m quadrados
import math
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
#A quantidade de tinta vai ser a àrea a dividir por 2
area = math.ceil(area / 2)
print('Cada galão de tinta pinta 2m quadrados, logo, ', end='')
print('precisará de {} galões para pintar a parede.'.format(area))
