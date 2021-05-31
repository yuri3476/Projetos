soma = 0
for i in range(0, 6):
    n1 = int(input('Digite o número: '))
    n = (n1 % 2)

    if n == 0:
        soma = soma + n1

print('A soma dos números pares é {}!'.format(soma))

