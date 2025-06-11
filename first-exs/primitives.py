#Fazer um programa que indique o tipo primitivo de uma str
dado = (input('Digite algo '))
print('O tipo primitivo de "{}" é'.format(dado), type(dado))
print('"{}" É um número?'.format(dado), dado.isnumeric())
print('"{}" É uma letra?'.format(dado), dado.isalpha())
print('"{}" Está minúsculo?'.format(dado), dado.islower())
print('"{}" Está maiúsculo?'.format(dado), dado.isupper())
print('"{}" É um decimal?'.format(dado), dado.isdecimal())
print('"{}" É alfanumérico?'.format(dado), dado.isalnum())
print('"{}" Está capitalizado?'.format(dado), dado.istitle())





