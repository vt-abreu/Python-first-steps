#Fazer um programa que pergunte a quantidade de km rodados por um carro
#a quantidade de dias que este carro foi alugado
#e que calcule o preço a ser pago, sabendo que
#cada dia custa 60€ e cada km custam 0.15€
km = float(input('Digite quantos quilometros foram rodados: '))
d = int(input('Digite quantos dias foram utilizados '))
#p = (km * 0.15) + d * 60
print('O valor a ser pago é de: €{:.2f}'.format((km * 0.15) + d * 60))