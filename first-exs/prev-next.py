#Create a program to show the number before and the number after.
#Example:
#('O antecessor de {} é {} e o sucessor é {}'.format(n , (n-1) , (n+1)))

n = int(input('Digite um número inteiro '))
s = n + 1
a = n - 1

print('O antecessor de {} é {}'.format(n, a), end='')
print(' e o seu sucessor é {}'.format(s))
