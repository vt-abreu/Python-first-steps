#Create one times table.

n = int(input('Digite um número inteiro: '))
for z in range(1 , 11):
    print('{} * {} = {}'\
          .format(n , z , n * z))


