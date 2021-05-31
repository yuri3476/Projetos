import math
x = int(input('Digite o comprimento do cateto maior: '))
y = int(input('Digite o comprimento do cateto menor: '))

cma = x ** 2
cme = y ** 2
soma = cma + cme
raiz = math.sqrt(soma)

print('A hipotenusa é {:.2f}'.format(raiz))












