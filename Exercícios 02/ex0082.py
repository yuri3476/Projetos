lista = []
pares = []
impar = []
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impar.append(n)

    cont = str(input('Quer continuar: [S/N] ')).upper()
    if cont == 'N':
        break
print('=' * 50)
print('A lista completa é: ', lista)
print('A lista de pares é: ', pares)
print('A lista de ímpares é: ', impar)

