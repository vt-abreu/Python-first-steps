#Fazer um programa que leia o preço do produto e calcule 5% de desconto
n = float(input('Digite o valor do produto: '))
d = n * 0.05
print('O valor do desconto será: {}'.format(d))
print('Novo total: {}'.format(n - d))