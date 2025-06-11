#Fazer um programa que leia o preço do produto e calcule 5% de desconto
n = float(input('Digite o valor do produto: '))
desconto = n * 0.05
print('O valor do desconto será: {}'.format(desconto))
print('Novo total: {}'.format(n - desconto))