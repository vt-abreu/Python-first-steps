#Fazer um programa que calcule o dobro, tripo e a raíz de um número
n = int(input('Digite um número inteiro: '))
db = n * 2
tp = n * 3
sqrt = pow(n, (1/2))
#pow(n,(1/2))
print('O dobro de {} é {},\no triplo é {},\ne a sua raíz é {:.2f}'
      .format(n, db, tp, sqrt))