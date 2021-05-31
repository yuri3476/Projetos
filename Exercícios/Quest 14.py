salario = float(input('Valor do salário: '))
print('-='*20)
if salario < 200:
    inss = salario * 0.08
    print(f'O valor do desconto do INSS é {inss}R$.')
elif salario >= 200 and salario < 500:
    inss = salario * 0.085
    print(f'O valor do desconto do INSS é {inss}R$.')
elif salario >= 500 and salario < 1000:
    inss = salario * 0.09
    print(f'O valor do desconto do INSS é {inss}R$.')
elif salario >= 1000:
    inss = salario * 0.095
    print(f'O valor do desconto do INSS é {inss}R$.')
print('-='*20)








