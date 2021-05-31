produto = float(input('Digite o valor do produto: '))
print('\033[34m-=-\033[m' * 15)
print('CONDIÇÃO DE PAGAMENTO:')
cond = input('[1] (à vista dinheiro/cheque)\n[2] (à vista no cartão)\n[3] (2x no cartão)\n[4] (3x ou mais no cartão): ')
print('\033[34m-=-\033[m' * 15)
if cond == '1':
    valor = produto * 0.10
    valorp = produto - valor
    print('\033[36mO valor a ser pago será R$ {}! Com 10% de desconto.\033[m'.format(valorp))
elif cond == '2':
    valor2 = produto * 0.05
    valort = produto - valor2
    print('\033[36mO valor a ser pago será R$ {}! Com 5% de desconto.\033[m'.format(valort))
elif cond == '3':
    parcela = int(input('Quantas parcelas? (Em até 2x no cartão)'))
    print('\033[36mO valor a ser pago será R$ {}!\033[m'.format(produto))
    parcl = produto / parcela
    print('\033[36mO valor parcelado será R$ {}!\033[m'.format(parcl))
elif cond == '4':
    parcelas = int(input('Quantas parcelas? '))
    valor3 = produto * 0.20
    valorg = produto + valor3
    print('\033[36mO valor a ser pago será R$ {}! \033[m'.format(valorg))
    parc = valorg / parcelas
    print('\033[36mO valor parcelado será R$ {}!\033[m'.format(parc))




