nome = str(input('Informe o nome do produto: '))
preco = float(input('Informe o preço do produto: '))
quant = int(input('Informe a quantidade comprada: '))
precoT = preco * quant
if quant <= 10:
    valorT = precoT * quant
    print('-='*20)
    print(f'O valor total a ser pago é: {valorT}')
elif quant >= 11 and quant <= 20:
    desc1 = precoT * 0.1
    valorT2 = precoT - desc1
    print('-='*20)
    print(f'O valor total a ser pago é: {valorT2}')
elif quant >= 21 and quant <= 50:
    desc2 = precoT * 0.2
    valorT3 = precoT - desc2
    print('-='*20)
    print(f'O valor total a ser pago é: {valorT3}')
elif quant > 50:
    desc3 = precoT * 0.25
    valorT4 = precoT - desc3
    print('-='*20)
    print(f'O valor total a ser pago é: {valorT4}')
print(f'O produto foi: {nome}')
print('-=' * 20)
