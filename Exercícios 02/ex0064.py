n = 1
qnt = 0
soma = 0
while n != 999:
    n = int(input('Digite um valor [999 para parar]: '))
    if n != 999:
        qnt += 1
        soma = soma + n

print('\nA quantidade de valores digitados foi {}!'.format(qnt))
print('A soma entre os valores digitados é {}!'.format(soma))


