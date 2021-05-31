
atletas = []
infantil_B = []
qnt_adultos = 0
qnt_total_atletas = 0
qnt_juvenilA = 0
while True:
    codigo_inscricao = int(input('Informe o código de inscrição do atleta (-1 para finalizar): '))
    if codigo_inscricao == -1:
        break
    nome = input('Informe o nome do atleta: ')
    idade = int(input('Informe a idade do atleta: '))
    qnt_total_atletas += 1
    if idade == 8 or idade == 9 or idade == 10:
        infantil_B += [f'Nome: {nome}']
    if idade >= 18:
        qnt_adultos += 1
    if idade == 11 or idade == 12 or idade == 13:
        qnt_juvenilA += 1

    peso = float(input('Informe o peso do atleta: '))
    altura = float(input('Informe a altura do atleta: '))
    imc = (peso / altura**2)
    atletas += [f'Nome: {nome} | IMC: {imc:.2f}']
    print()
perc = ((qnt_juvenilA * 100) / qnt_total_atletas)
print()
print('\033[36m-=\033[m'*30)
for k in range(0, len(atletas)):
    print(atletas[k])
print('\033[36m-=\033[m'*30)
print('ATLETAS ALOCADOS NA CATEGORIA INFANTIL B:')
print()
for k in range(0, len(infantil_B)):
    print(infantil_B[k])
print('\033[36m-=\033[m'*30)
print(f'A quantidade de atletas alocados na categoria Adulto é {qnt_adultos}.')
print('\033[36m-=\033[m'*30)
print(f'O percentual de atletas alocados na categoria Juvenil A foi de {perc:.2f}%')
print('\033[36m-=\033[m'*30)
