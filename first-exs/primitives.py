#Fazer um programa que indique o tipo primitivo de uma str
n = (input('Digite algo '))
print('O tipo primitivo de "{}" é'.format(n), type(n))
print('"{}" É um número?'.format(n), n.isnumeric())
print('"{}" É uma letra?'.format(n), n.isalpha())
print('"{}" Está minúsculo?'.format(n), n.islower())
print('"{}" Está maiúsculo?'.format(n), n.isupper())
print('"{}" É um decimal?'.format(n), n.isdecimal())
print('"{}" É alfanumérico?'.format(n), n.isalnum())
print('"{}" Está capitalizado?'.format(n), n.istitle())





