salario = float(input('Digite o seu salário R$: '))
if salario > 1250.0:
    aumento = salario * 0.10
    sal = salario + aumento
    print('O seu novo salário com aumento será de {:.2f} R$'.format(sal))
else:
    aumento1 = salario * 0.15
    sal1 = salario + aumento1
    print('O seu novo salário com aumento será de {:.2f} R$'.format(sal1))


