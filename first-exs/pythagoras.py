#Create a program to calculate the hypotenuse.

from math import hypot

c = float(input('Digite o valor do cateto adjacente: '))
co = float(input('Digite o valor do cateto oposto: '))
h = hypot(c , co)


print('A hipotenusa corresponde a: {:.3f}'.format(h))


