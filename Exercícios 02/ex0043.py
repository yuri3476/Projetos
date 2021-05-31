peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))

imc = (peso / altura ** 2)
print('Seu IMC é de {:.2f}!'.format(imc))
if imc < 18.5:
    print('ABAIXO DO PESO')
elif imc >= 18.5 and imc < 25:
    print('PESO IDEAL')
elif imc >= 25 and imc < 30:
    print('SOBREPESO')
elif imc >= 30 and imc < 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MÓRBIDA')



