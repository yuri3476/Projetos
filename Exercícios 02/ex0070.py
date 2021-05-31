print('-' * 24)
print('  LOJA SUPER BARATÃO')
print('-' * 24)
totalg = 0
maior1 = 0
menor = 0
nom = ''
qnt = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço: R$ '))
    totalg += preco
    qnt += 1
    if qnt == 1:
        menor = preco
        nom = nome
    else:
        if preco < menor:
            menor = preco
            nom = nome

    if preco > 1000:
        maior1 += 1

    n = input('Deseja continuar? [S/N] ').upper()
    while n != 'S' and n != 'N':
        n = input('Deseja continuar? [S/N] ').upper()
    if n == 'N':
        break
    else:
        continue


print('======FIM DA COMPRA======')
print(f'O total de compra foi R$ {totalg}')
print(f'Temos {maior1} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nom} que custa R$ {menor}')

