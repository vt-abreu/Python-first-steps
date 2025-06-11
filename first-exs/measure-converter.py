#Fazer um programa que converta uma medida em metros para dm, cm e mm
m = float(input('Digite o valor da medida em metros: '))
#d = medida * 10
#c = medida * 100
#mm = medida * 1000
#print('{} decímetros'.format(d))
#print('{} centímetros'.format(c))
#print('{} milímetros'.format(mm))
print('{} metros equivalem a\n{:.0f} decímetros\n{:.0f} centímetros e\n{:.0f} milímetros'
      .format(m , m * 10 , m * 100 , m * 1000))
