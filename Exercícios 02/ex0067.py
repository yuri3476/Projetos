while True:
    n1 = int(input('Digite um número: '))
    if n1 < 0:
        break
    for i in range(0, 11):
        soma = n1 * i
        print('{} x {} = {}'.format(n1, i, soma))
print('FIM')
