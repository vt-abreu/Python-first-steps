#Create a program to randomly pick one variable.
#And create a random list with the variables.

import random

a = str('Álvaro')
b = str('Braga')
c = str('Carlos')
d = str('Dumbledore')

n = [a ,b ,c , d]
r = random.choice(n)

random.shuffle(n)

print('Selecionando aleatoriamente um nome obtêm-se: {}\n'.format(r))
print('Formando uma lista em ordem aleatória obtêm-se: ')
for list in n:
    print(list)
