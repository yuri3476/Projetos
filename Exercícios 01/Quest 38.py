qnt_E = 0
qnt_P = 0
qnt_O = 0
menor_obitos = 9999999999999
menor_estado = ''
qnt_P1 = []
qnt_O1 = []
print('\033[36m-=\033[m'*30)
print('\033[31m     =====DADOS RELATIVOS À PANDEMIA NO BRASIL=====\033[m')
print('\033[36m-=\033[m'*30)
while True:
    codigo = int(input('Digite o código do estado: '))
    if codigo == -1:
        break
    nome = str(input('Informe o nome do estado: '))
    qnt_E += 1
    qnt = int(input('Informe a quantidade de pacientes que testaram positivo para COVID-19: '))
    qnt_P += qnt
    qnt_P1.append(qnt)
    obitos = int(input('Informe a quantidade de óbitos decorrentes do agravamento desta doença: '))
    qnt_O += obitos
    qnt_O1.append(obitos)

    if obitos < menor_obitos:
        menor_obitos = 0
        menor_obitos += obitos
        menor_estado = ''
        menor_estado += nome
    print()

soma = qnt_P + qnt_O
media = soma / qnt_E
soma1 = qnt_P1[0] + qnt_O1[0]
perc = (soma1 * 100) / soma
print('\033[36m-=\033[m'*40)
print(f'A média de pacientes infectados nos estados cadastrados foi de {media:.2f}')
print('\033[36m-=\033[m'*40)
print(f'O estado de  {menor_estado} apresentou o menor número de óbitos de {menor_obitos} em virtude do COVID-19')
print('\033[36m-=\033[m'*40)
print(f' O percentual de pacientes infectados no primeiro estado foi de {perc:.2f}%')
print('\033[36m-=\033[m'*40)

