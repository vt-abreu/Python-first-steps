#Create a program that converts R$ to €.

n = float(input('Digite quanto deseja converter (R$):'))

euro = n / 6.40

print('Você é capaz de obter €{:.2f}'.format(euro))