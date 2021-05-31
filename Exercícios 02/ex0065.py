r = 'S'
med = 0
qnt = 0
maxi = []
maior = menor = 0

while r in 'Ss':
    n = int(input('Digite um valor: '))
    med = med + n
    qnt += 1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if qnt == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

media = med / qnt
print(f'A média dos valores digitados é {media}')
print(f'O maior número é {maior} e o menor número é {menor}!')

