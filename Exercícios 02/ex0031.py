dist = float(input('Digite a distância de sua viagem KM: '))
if dist <= 200.0:
    preco = 0.50 * dist
    print('Você irá pagar em sua viagem {} R$'.format(preco))
else:
    preco1 = 0.45 * dist
    print('Você irá pagar em sua viagem {} R$'.format(preco1))

print('---FIM---')
