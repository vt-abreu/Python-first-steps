#Create a program to read the price and calculate 5% of discount.

n = float(input('Digite o valor do produto: '))
d = n * 0.05

print('\nO valor do desconto será: {}\n'.format(d))
print('Novo total: {}'.format(n - d))