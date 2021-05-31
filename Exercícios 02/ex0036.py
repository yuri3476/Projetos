print('\033[33m-==-\033[m' * 20)
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salário do comprador: '))
ano = int(input('Digite em quantos anos ele vai pagar? '))
print('\033[33m-==-\033[m' * 20)

meses = ano * 12
prestacao = valor / meses
porcentagem = salario * 0.30

if prestacao > porcentagem:
    print('\033[31mInfelizmente você não pode financiar esta casa\033[m')

else:
    print('\033[32mO valor da prestação mensal será de R${:.3f}\033[m '.format(prestacao))




