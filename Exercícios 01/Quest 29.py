lista = []
par = []
impar = []
for i in range(0, 20):
    num = int(input('Informe um número inteiro: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print()
print('Números digitados: ', lista)
print('Números pares: ', par)
print('Números impares: ', impar)




