qntd = 0
qntp = 0
menor_Valor_F = -99999999
nome_F = ''
qntF = 0
qnt_C = 0
print('\033[36m-=\033[m'*25)
print('\033[36m      ======MINI MERCADO DE LELEO======\033[m')
print('\033[36m-=\033[m'*25)
while True:
    codigo = int(input('Informe o código do cliente: '))
    nome = str(input('Informe o seu nome: '))
    qnt_C += 1
    sexo = str(input('Informe o sexo o [M - Masculino / F - Feminino]: ')).upper()
    produto = str(input('Informe o nome no produto: '))
    qntp += 1
    valor = float(input('Informe o valor do produto: '))
    qnt = int(input('Informe a quantidade desejada: '))
    qntd += qnt
    dia = str(input('O dia foi encerrado? o [S-Sim / N-Não]')).upper()
    print()

    if sexo == 'F':
        valorT = valor * qnt
        if valorT > menor_Valor_F:
            menor_Valor_F = 0
            menor_Valor_F += valorT
            nome_M = ''
            nome_M += nome
    if sexo == 'M':
        qntF += 1

    if dia == 'S':
        break

media = qntd / qntp
perc = (qntF * 100) / qntp
print()
print('\033[36m-=\033[m'*45)
print(f'A quantidade de clientes que realizou compras foi de {qnt_C}.')
print('\033[36m-=\033[m'*45)
print(f'A média da quantidade de produtos vendidos por compras realizadas durante o expediente {media}.')
print('\033[36m-=\033[m'*45)
print(f'Nome do cliente (sexo feminino) com maior valor de compra foi {nome_F}, com o valor de {menor_Valor_F}R$')
print('\033[36m-=\033[m'*45)
print(f'O Percentual de clientes do sexo masculino que realizou compras no dia foi {perc:.2f}%')
print('\033[36m-=\033[m'*45)
