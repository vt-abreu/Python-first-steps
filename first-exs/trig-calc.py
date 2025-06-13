#Create a program to calculate the sine, cosine and tangent of an angle.

from math import cos
from math import sin
from math import tan

a = int(input('Digite o valor do ângulo: '))

print('O cosseno de {} é {:.0f},\n'.format(a , cos(a)))
print('O seno de {} é {:.0f},\n'.format(a , sin(a)))
print('A tangente de {} é {:.0f}'.format(a , tan(a)))

