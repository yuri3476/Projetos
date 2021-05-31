
qnt_Masc = 0
soma = 0
qnt_Fem = 0
M_salario = []

while True:
    cpf = int(input('Informe o seu CPF: '))
    if cpf == 0:
        break
    nome = str(input('Informe o seu nome completo: '))
    sexo = input('Informe o seu sexo: (0- [F] | 1- [M]): ')
    idade = int(input('Informe sua idade: '))
    salario = int(input('Informe seu salário: '))
    M_salario.append(salario)
    qnt_M = int(input('Informe a quantidade de filhos de cada habitante: '))
    qnt_Masc += qnt_M
    qnt_F = int(input('Informe a quantidade de filhas de cada habitante: '))
    qnt_Fem += qnt_F
    print()

soma = qnt_Masc + qnt_Fem
perc = (qnt_Fem * 100) / soma
menor = min(M_salario)
print()
print('\033[36m-=\033[m'*40)
print(f'Quantidade de filhos do sexo masculino dos habitantes da cidade {qnt_Masc}.')
print('\033[36m-=\033[m'*40)
print(f'O percentual de filhas do sexo feminino em relação a quantidade total de filhos dos habitantes da cidade foi {perc:.2f}%.')
print('\033[36m-=\033[m'*40)
print(f'Menor salário dos habitantes foi {menor}.')
print('\033[36m-=\033[m'*40)
