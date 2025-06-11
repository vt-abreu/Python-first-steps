#Fazer um programa que calcule o dobro, tripo e a raíz de um número
n = int(input('Digite um número inteiro: '))
dobro = n * 2
triplo = n * 3
raiz = n**1/2
#pow(n,(1/2))
print('O dobro de {} é {},\no triplo é {},\ne a sua raíz é {:.2f}'
      .format(n, dobro, triplo, raiz))