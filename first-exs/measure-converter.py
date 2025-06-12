#Create a program to convert m to dm, cm and mm.
#d = m * 10
#c = m * 100
#mm = m * 1000
#print('{} dm'.format(d))
#print('{} cm'.format(c))
#print('{} mm'.format(mm))

m = float(input('Digite o valor da medida em metros: '))

print('{} metros equivalem a\n{:.0f} decímetros\n{:.0f} centímetros\
 e\n{:.0f} milímetros'
      .format(m, m * 10, m * 100, m * 1000))
