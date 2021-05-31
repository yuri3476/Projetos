
vel = float(input('Qual foi a velocidade atual do carro? '))
if vel > 80.0:
    multa = vel - 80.0
    pagar = multa * 7.00
    print('Você foi multado! Deverá pagar uma multa de {} R$ '.format(pagar))
else:
    print('Está no limite permitido!')

print('\nTenha um Bom dia! Dirija com segurança!')


