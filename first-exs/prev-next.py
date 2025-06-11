#Fazer um programa que indique o antecessor e o sucessor de um número
n = int(input('Digite um número inteiro '))
sucessor = n + 1
antecessor = n - 1
print('O antecessor de {} é {}'.format(n, antecessor), end='')
print(' e o seu sucessor é {}'.format(sucessor))
#print('O antecessor de {} é {} e o sucessor é {}'.format(n , (n-1) , (n+1)))
