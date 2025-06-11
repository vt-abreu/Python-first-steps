#Fazer um programa que converta a temperatura de celcius para fahrenheits
t = float(input('Informe a temperatura em Celsius: '))
f = 9 * t / 5 + 32
#Lembrar da ordem de precedência
print('A temperatura {} em Fahrenheits equivale a {:.1f}'.format(t , f))
